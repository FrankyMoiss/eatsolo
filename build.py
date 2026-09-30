#!/usr/bin/env python3
"""Build dist/eatsolo_app_final.html and dist/index.html from the template + assets/."""
import base64
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
DIST = ROOT / "dist"


def b64(path):
    return base64.b64encode(path.read_bytes()).decode("ascii")


def main():
    template = (ROOT / "eatsolo_app_template.html").read_text(encoding="utf-8")

    replacements = {
        "__BALOO_B64__": b64(ASSETS / "fonts" / "baloo2.woff2"),
        "__INTER_B64__": b64(ASSETS / "fonts" / "inter.woff2"),
        "__SOURCESERIF_B64__": b64(ASSETS / "fonts" / "sourceserif.woff2"),
        "__SPACEGROTESK_B64__": b64(ASSETS / "fonts" / "spacegrotesk.woff2"),
        "__LOGO_B64__": b64(ASSETS / "logo_neon.jpg"),
        "__LOGO_GOLDEN_B64__": b64(ASSETS / "logo_golden.jpg"),
        "__LOGO_NIGHT_B64__": b64(ASSETS / "logo_night.jpg"),
    }

    for placeholder, value in replacements.items():
        assert placeholder in template, f"missing placeholder: {placeholder}"
        template = template.replace(placeholder, value)

    # mqtt.js is inlined as-is (not base64) so the page stays self-contained
    mqtt_js = (ASSETS / "mqtt.min.js").read_text(encoding="utf-8")
    assert "</script" not in mqtt_js, "mqtt.js would close the script tag"
    assert "__MQTT_JS__" in template, "missing placeholder: __MQTT_JS__"
    template = template.replace("__MQTT_JS__", mqtt_js)

    DIST.mkdir(exist_ok=True)
    (DIST / "eatsolo_app_final.html").write_text(template, encoding="utf-8")

    icon_b64 = b64(ASSETS / "app_icon.png")
    full_doc = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<title>EatSolo</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, maximum-scale=1, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="EatSolo">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#0a0a0d">
<link rel="apple-touch-icon" href="data:image/png;base64,{icon_b64}">
<link rel="icon" href="data:image/png;base64,{icon_b64}">
</head>
<body>
{template}
</body>
</html>
"""
    (DIST / "index.html").write_text(full_doc, encoding="utf-8")
    print(f"Built dist/eatsolo_app_final.html ({len(template)} chars)")
    print(f"Built dist/index.html ({len(full_doc)} chars)")


if __name__ == "__main__":
    main()
