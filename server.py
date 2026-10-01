import json
import re
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).parent
STATIC_FILE = ROOT / "dist" / "index.html"
STALE_AFTER = 25  # seconds without a heartbeat before someone drops off the radar

lock = threading.Lock()
presence = {}       # id -> {id, name, intent, available, lastSeen}
profiles = {}       # id -> full profile; outlives presence so you can still view a contact's profile
conversations = {}  # convoKey -> {id, participants:[a,b], names:{id:name}, initiator, status, log:[{who,text,ts}]}
plans = {}          # id -> {id, name, city, area, when, slot, mealType, restaurant, active, updatedAt}

PROFILE_FIELDS = ("name", "age", "job", "bio", "gender", "city", "photo")
PROFILE_LISTS = ("cuisines", "hobbies")


def clean_profile(data):
    """Whitelist + size-cap whatever the client sent, so one client can't bloat the store."""
    out = {}
    for key in PROFILE_FIELDS:
        value = data.get(key)
        if isinstance(value, str):
            # photos arrive as small downscaled data URLs; everything else is short text
            out[key] = value[:200000] if key == "photo" else value[:200]
    for key in PROFILE_LISTS:
        value = data.get(key)
        if isinstance(value, list):
            out[key] = [str(v)[:40] for v in value[:12]]
    out["verified"] = bool(data.get("verified", True))
    return out


def public_profile(pid):
    """Profile as other members see it, always including an id and a display name."""
    p = dict(profiles.get(pid) or {})
    p["id"] = pid
    p.setdefault("name", presence.get(pid, {}).get("name", "?"))
    return p


def convo_key(a, b):
    return "|".join(sorted([a, b]))


def prune_presence():
    now = time.time()
    dead = [pid for pid, p in presence.items() if now - p["lastSeen"] > STALE_AFTER]
    for pid in dead:
        del presence[pid]


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass

    def _send_json(self, obj, status=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        if length == 0:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw)
        except Exception:
            return {}

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/api/ping":
            return self._send_json({"ok": True})

        if path == "/api/people":
            me = (qs.get("id") or [""])[0]
            with lock:
                prune_presence()
                out = []
                for pid, p in presence.items():
                    if pid == me or not p.get("available"):
                        continue
                    entry = public_profile(pid)
                    entry["intent"] = p.get("intent", "diner")
                    out.append(entry)
            return self._send_json({"people": out})

        if path == "/api/profile":
            who = (qs.get("who") or [""])[0]
            if not who:
                return self._send_json({"error": "missing who"}, 400)
            with lock:
                return self._send_json({"profile": public_profile(who)})

        if path == "/api/conversations":
            me = (qs.get("id") or [""])[0]
            with lock:
                out = []
                for c in conversations.values():
                    if me not in c["participants"]:
                        continue
                    other = [p for p in c["participants"] if p != me][0]
                    last = c["log"][-1] if c["log"] else None
                    out.append({
                        "convo": c["id"],
                        "otherId": other,
                        "otherName": c["names"].get(other, "?"),
                        "status": c["status"],
                        "iAmInitiator": c["initiator"] == me,
                        "preview": (last["text"] if last else ""),
                        "logLength": len(c["log"]),
                    })
            return self._send_json({"conversations": out})

        if path == "/api/thread":
            me = (qs.get("id") or [""])[0]
            other = (qs.get("with") or [""])[0]
            key = convo_key(me, other)
            with lock:
                c = conversations.get(key)
                if not c:
                    return self._send_json({"status": None, "log": [], "otherName": ""})
                return self._send_json({
                    "status": c["status"],
                    "iAmInitiator": c["initiator"] == me,
                    "otherName": c["names"].get(other, "?"),
                    "log": c["log"],
                })

        if path == "/api/plans":
            me = (qs.get("id") or [""])[0]
            with lock:
                out = []
                for pid, p in plans.items():
                    if pid == me or not p.get("active"):
                        continue
                    entry = dict(p)
                    entry["profile"] = public_profile(pid)
                    out.append(entry)
            return self._send_json({"plans": out})

        return self._send_json({"error": "not found"}, 404)

    def do_POST(self):
        path = urlparse(self.path).path
        data = self._read_json()

        if path == "/api/presence":
            pid = data.get("id")
            if not pid:
                return self._send_json({"error": "missing id"}, 400)
            with lock:
                presence[pid] = {
                    "id": pid,
                    "name": (data.get("name") or "Invité")[:40],
                    "intent": data.get("intent") or "diner",
                    "available": bool(data.get("available", True)),
                    "lastSeen": time.time(),
                }
                profile = clean_profile(data)
                profile.setdefault("name", presence[pid]["name"])
                profiles[pid] = profile
                prune_presence()
            return self._send_json({"ok": True})

        if path == "/api/hello":
            me, my_name, target = data.get("id"), data.get("name", "?"), data.get("targetId")
            if not me or not target:
                return self._send_json({"error": "missing id"}, 400)
            key = convo_key(me, target)
            with lock:
                c = conversations.get(key)
                if not c:
                    other_name = presence.get(target, {}).get("name", "?")
                    c = conversations[key] = {
                        "id": key, "participants": [me, target],
                        "names": {me: my_name, target: other_name},
                        "initiator": me, "status": "pending", "log": [],
                    }
                c["log"].append({"who": "system", "text": f"{my_name} a dit bonjour 👋", "ts": time.time()})
            return self._send_json({"ok": True})

        if path == "/api/respond":
            me, target, accept = data.get("id"), data.get("targetId"), bool(data.get("accept"))
            key = convo_key(me, target)
            with lock:
                c = conversations.get(key)
                if not c:
                    return self._send_json({"error": "no such conversation"}, 404)
                if accept:
                    c["status"] = "accepted"
                    my_name = c["names"].get(me, "quelqu'un")
                    c["log"].append({"who": "system", "text": f"{my_name} a accepté de discuter 🎉", "ts": time.time()})
                else:
                    c["status"] = "declined"
            return self._send_json({"ok": True})

        if path == "/api/message":
            me, target, text = data.get("id"), data.get("targetId"), (data.get("text") or "").strip()
            if not text:
                return self._send_json({"error": "empty"}, 400)
            key = convo_key(me, target)
            with lock:
                c = conversations.get(key)
                if not c or c["status"] != "accepted":
                    return self._send_json({"error": "not accepted"}, 409)
                c["log"].append({"who": me, "text": text[:500], "ts": time.time()})
            return self._send_json({"ok": True})

        if path == "/api/meeting":
            me, target = data.get("id"), data.get("targetId")
            venue, when = data.get("venue", "?"), data.get("time", "?")
            key = convo_key(me, target)
            with lock:
                c = conversations.get(key)
                if not c or c["status"] != "accepted":
                    return self._send_json({"error": "not accepted"}, 409)
                c["log"].append({"who": "system", "text": f"Rendez-vous proposé · {venue} à {when}", "ts": time.time()})
            return self._send_json({"ok": True})

        if path == "/api/plan":
            pid = data.get("id")
            if not pid:
                return self._send_json({"error": "missing id"}, 400)
            with lock:
                plans[pid] = {
                    "id": pid,
                    "name": (data.get("name") or "Invité")[:40],
                    "city": (data.get("city") or "")[:60],
                    "area": (data.get("area") or "")[:60],
                    "when": (data.get("when") or "")[:40],
                    "slot": (data.get("slot") or "")[:40],
                    "date": (data.get("date") or "")[:20],
                    "minPeople": str(data.get("minPeople") or "")[:3],
                    "maxPeople": str(data.get("maxPeople") or "")[:3],
                    "pitch": (data.get("pitch") or "")[:300],
                    "mealType": (data.get("mealType") or "diner")[:20],
                    "restaurant": (data.get("restaurant") or "")[:120],
                    "active": True,
                    "updatedAt": time.time(),
                }
            return self._send_json({"ok": True})

        if path == "/api/plan/clear":
            pid = data.get("id")
            with lock:
                if pid in plans:
                    plans[pid]["active"] = False
            return self._send_json({"ok": True})

        return self._send_json({"error": "not found"}, 404)


class QuietThreadingHTTPServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


if __name__ == "__main__":
    import sys
    import os
    port = int(os.environ.get("PORT") or (sys.argv[1] if len(sys.argv) > 1 else 8765))
    os.chdir(ROOT)

    # serve static index.html for everything that isn't /api/*
    class StaticOrApi(Handler):
        def do_GET(self):
            if self.path.startswith("/api/"):
                return Handler.do_GET(self)
            return self._serve_static()

        def _serve_static(self):
            fp = STATIC_FILE
            body = fp.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    srv = QuietThreadingHTTPServer(("0.0.0.0", port), StaticOrApi)
    print(f"listening on 0.0.0.0:{port}")
    srv.serve_forever()
