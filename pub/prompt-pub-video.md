# EatSolo — « Never EatSolo Again »
## Prompt de production vidéo IA — pub 20 s (7 plans) · film complet 43 s (12 plans)

---

## 0. LA PUB — 20 secondes, 7 plans

**C'est cette version qu'on produit.** Les 12 plans décrits plus bas restent le film complet
(43 s) : utile pour une page d'accueil ou une présentation investisseurs, trop long pour de la
diffusion. Pour la pub, on ne génère que ces 7 plans-là, avec exactement les mêmes prompts que
ci-dessous — seule la durée de montage change.

| # | Plan source | Durée | Ce que ça raconte |
|---|---|---|---|
| 1 | **Plan 2** — L'installation de fortune | 3 s | Seul, de passage, une serviette de bain en guise de nappe. Tout est posé en un plan. |
| 2 | **Plan 4** — Et paf | 3 s | Une bouchée, et tout tombe sur le lit. |
| 3 | **Plan 5** — La frite collante | 2 s | Doigt collant, télé nulle. Le point le plus bas. |
| 4 | **Plan 7** — La fenêtre | 4 s | La bascule. Intouchable : c'est la charnière du film. |
| 5 | **Plan 9** — Le téléphone | 2 s | EatSolo s'ouvre. Le seul plan produit. |
| 6 | **Plan 11** — Le chien | 3 s | Quelqu'un en face. |
| 7 | **Plan 12** — Le trinquement | 3 s | Les deux verres se touchent. Plus rien ne colle. |

**Total : 20 s + 3 s de carton final = 23 s.** Format natif pour Instagram, TikTok et YouTube
en préroll désactivable.

**Deux coupes plus courtes, sans rien régénérer :**
- **15 s** — on retire les plans 3 et 5 du tableau (la frite collante et le téléphone) et on
  passe le plan 7 à 3 s. On perd l'appli à l'image : le carton final doit alors montrer
  l'interface, pas seulement le logo.
- **6 s (bumper)** — uniquement les plans 4 et 7 du tableau (la fenêtre, puis le trinquement),
  2,5 s chacun, carton d'1 s. Pas d'histoire, juste le contraste.

**Ce qu'on perd en passant de 43 s à 20 s**, pour que ce soit un choix et pas un accident :
l'arrivée dans la chambre, le gobelet renversé, le geste de jeter la commande à la poubelle et
la descente des marches. C'est le geste de rupture de la poubelle qui manque le plus — si tu
veux le garder, c'est 2 s de plus (plan 8) à prendre sur le plan 7.

---

## 1. Le pitch en trois lignes

Un homme rentre dans sa chambre avec sa livraison, bricole une table avec une serviette de bain sur son lit, et tout se renverse : la sauce, le soda, la soirée. Un bruit l'attire à la fenêtre : trois étages plus bas, les terrasses rient, trinquent et mangent des choses magnifiques.
Il jette la commande à peine entamée, ouvre EatSolo, descend, et s'assoit en face de quelqu'un qui sait vivre : un chien en chemise de lin.
Tout le film est vu par ses yeux — on ne verra jamais son visage, seulement ses mains : les mêmes mains qui étalaient une serviette de bain lèvent un verre en terrasse.

---

## 2. Bloc de style global

> **Mode d'emploi.** On colle le bloc de style **en tête du prompt de plan**, puis le prompt du plan dessous. Les prompts de plan ne redécrivent pas le décor ni la lumière : ils appellent les étiquettes `DÉCOR A / LUMIÈRE A / DÉCOR B / LUMIÈRE B / CHIEN`. Seule la ligne **MAINS** est répétée mot pour mot dans chaque plan, volontairement : c'est l'ancre de continuité du héros.
> **Les négatifs ne vont JAMAIS dans la description** : ils vont dans le champ *negative prompt* dédié (Kling, Runway, Luma). Si le modèle n'en a pas (Sora, Veo en texte simple), coller la liste négative en toute dernière ligne du prompt, jamais au milieu.

### Version française

```
=== BLOC DE STYLE GLOBAL — FR ===
RÈGLE ABSOLUE : film publicitaire intégralement en VUE SUBJECTIVE (POV première
personne). La caméra EST les yeux du héros. Visage jamais visible, jamais de reflet,
jamais de contrechamp, jamais de plan extérieur sur lui : on ne voit que ses mains et
ses avant-bras, qui entrent dans le cadre par le bas.
MAINS : mains adultes, ongles courts et nets, aucune bague, bracelet de montre en cuir
noir usé au poignet gauche, manches d'un hoodie gris chiné remontées aux avant-bras.
DÉCOR A (plans 1 à 9) : studio meublé impersonnel de 12 m², type résidence hôtelière bas
de gamme. Murs beige fatigué, moquette gris souris, lit simple avec housse de couette
gris anthracite froissée, commode en mélaminé chêne clair, télé LCD 32 pouces posée
dessus, valise ouverte au sol, fenêtre à un seul battant avec rideau fin blanc, radiateur
dessous, petite poubelle à pédale en plastique gris près de la porte de salle de bain.
LUMIÈRE A : nuit, aucun plafonnier. Seule source forte : l'écran de télé, bleu-cyan
clignotant, 5600 K. Plus un halo d'enseigne bleue par la fenêtre. Contraste dur, ombres
bouchées, image presque désaturée.
DÉCOR B (plans 10 à 12) : rue de ville européenne au pied de l'immeuble, pavés humides,
terrasse de bistrot, chaises en rotin, petites tables rondes, nappes en papier,
guirlandes d'ampoules, carafes, autres convives attablés à l'arrière-plan.
LUMIÈRE B : tungstène chaud 2700 K, guirlandes en gros bokeh rond, bois et peau dorés,
contraste bas, enveloppant.
CHIEN (plans 11 et 12) : golden retriever anthropomorphe photoréaliste, poil sable
soyeux, museau brillant, truffe humide, yeux bruns très expressifs et bienveillants,
sourcils mobiles, assis comme un humain sur une chaise de bistrot, chemise en lin blanche
à col ouvert et manches retroussées, serviette sur les genoux, pattes avant utilisées
comme des mains, échelle d'un adulte de 1,80 m. Attachant et crédible. Jamais cartoon,
jamais inquiétant, jamais grotesque.
OPTIQUE : 24 mm f/2.0 en intérieur, 35 mm f/2.0 en extérieur, légère distorsion de bord,
profondeur de champ courte, bokeh doux, grain argentique 35 mm fin, halation légère.
MOUVEMENT : caméra portée, hauteur d'yeux 1,70 m debout / 1,10 m assis, micro-tremblements
de respiration, balancement léger au rythme des pas. Jamais de secousse, jamais de
travelling mécanique, jamais de ralenti, aucune coupe à l'intérieur d'un plan.
RENDU : photoréaliste, matière avant tout (gras, buée, condensation, fibres, poussière).
FORMAT : 9:16 (décliner en 16:9 pour le web), 24 im/s. Aucun dialogue, aucune voix off.
Aucun texte ni logo généré par le modèle : tout l'habillage est ajouté au montage.

NEGATIVE PROMPT GLOBAL (champ dédié) : visage, visage du héros, miroir, reflet, selfie,
caméra à la troisième personne, contrechamp, bouche, ralenti, texte, sous-titres, logo,
marque, watermark, main à six doigts, doigts fondus, chien cartoon, chien inquiétant,
dents humaines, langue pendante, costume complet, chapeau, changement de décor,
changement de lumière.
```

### English version

```
=== GLOBAL STYLE BLOCK — EN ===
HARD RULE: commercial film shot entirely in FIRST-PERSON POV. The camera IS the hero's
eyes. His face is never visible, no reflection, no reverse shot, never any third-person
coverage of him: we only see his hands and forearms entering frame from the bottom.
HANDS: adult hands, short clean nails, no rings, a worn black leather watch strap on the
left wrist, heather-grey hoodie sleeves pushed up to the forearms.
SET A (shots 1 to 9): impersonal 12 sqm furnished studio, cheap extended-stay hotel style.
Tired beige walls, mouse-grey carpet, single bed with a crumpled charcoal-grey duvet
cover, light-oak melamine dresser, 32-inch LCD TV on top of it, open suitcase on the
floor, single-pane window with a thin white curtain, radiator under it, small grey plastic
pedal bin by the bathroom door.
LIGHT A: night, no ceiling light. Only strong source: the TV screen, flickering cyan-blue,
5600 K. Plus a blue sign glow through the window. Harsh contrast, crushed shadows, nearly
desaturated image.
SET B (shots 10 to 12): European city street at the foot of the building, wet cobblestones,
bistro terrace, rattan chairs, small round tables, paper tablecloths, festoon bulb lights,
water carafes, other diners seated in the background.
LIGHT B: warm 2700 K tungsten, large round bokeh bulbs, golden wood and skin, low
contrast, enveloping.
DOG (shots 11 and 12): photorealistic anthropomorphic golden retriever, silky sand-coloured
fur, glossy muzzle, wet nose, very expressive kind brown eyes, mobile brows, sitting like a
human on a bistro chair, white open-collar linen shirt with rolled sleeves, napkin on his
lap, front paws used as hands, scaled like a 1.80 m adult. Endearing and believable. Never
cartoonish, never creepy, never grotesque.
LENS: 24 mm f/2.0 indoors, 35 mm f/2.0 outdoors, slight edge distortion, shallow depth of
field, soft bokeh, fine 35 mm film grain, light halation.
MOVEMENT: handheld, eye level 1.70 m standing / 1.10 m seated, micro breathing shake, gentle
sway with each step. Never shaky, never a mechanical dolly, no slow motion, no cuts inside a
shot.
LOOK: photoreal, texture first (grease, steam, condensation, fibres, dust).
FORMAT: 9:16 (16:9 version for web), 24 fps. No dialogue, no voice-over. No text and no logo
generated by the model: all graphics are added in post.

GLOBAL NEGATIVE PROMPT (dedicated field): face, hero's face, mirror, reflection, selfie,
third-person camera, reverse shot, mouth, slow motion, text, subtitles, logo, brand,
watermark, six-fingered hand, melted fingers, cartoon dog, creepy dog, human teeth, lolling
tongue, full suit, hat, change of set, change of lighting.
```

---

## 3. Les plans

> **Note de production commune à tous les plans :** générer chaque plan en 8 ou 10 secondes (minimum du modèle), puis retailler au montage à la durée indiquée. Prévoir les points d'entrée et de sortie, ne jamais compter sur les 8 secondes entières.

### Plan 1 — L'arrivée — 3 s

**Intention :** il rentre, carte magnétique à la main, sa commande au bout du bras : en trois secondes on sait qu'il est seul et de passage.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 1. POV première personne, 24 mm f/2.0, caméra portée à hauteur d'yeux (1,70 m),
micro-tremblements de respiration, deux pas d'avance. MAINS : mains adultes, ongles courts,
aucune bague, bracelet de montre en cuir noir usé au poignet gauche, manches de hoodie gris
chiné remontées. ACTION : la main droite glisse une carte magnétique dans la serrure d'une
porte de chambre, petit voyant vert, et pousse la porte ; la main gauche tient par les anses
un sac de livraison en plastique blanc noué, lourd, qui se balance et froisse. La caméra
avance d'environ 1,5 m dans la pièce et s'arrête, la porte se referme derrière elle.
DÉCOR A. LUMIÈRE A, plus un filet de lumière jaune de couloir derrière la caméra au début du
plan. MATIÈRE : plastique brillant et tendu du sac, laiton rayé de la poignée, moquette rase,
poussière en suspension. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 1. First-person POV, 24 mm f/2.0, handheld camera at eye level (1.70 m), micro breathing
shake, two steps forward. HANDS: adult hands, short nails, no rings, worn black leather watch
strap on the left wrist, heather-grey hoodie sleeves pushed up. ACTION: the right hand slides
a keycard into a room door lock, small green light, and pushes the door open; the left hand
holds the handles of a knotted white plastic food-delivery bag, heavy, swinging and crinkling.
The camera moves about 1.5 m into the room and stops, the door swinging shut behind it.
SET A. LIGHT A, plus a thread of yellow corridor light behind the camera at the top of the
shot. TEXTURE: taut glossy plastic bag, scratched brass handle, low-pile carpet, dust floating
in the air. 9:16.
```

**Son :** bip sec du badge, déclic du pêne, grincement de la porte, froissement du sac, pas sur la moquette, porte qui claque et réverbère dans une pièce vide. Mixage **mono étroit, filtré passe-bas** : on est enfermé avec lui. Aucune mélodie, seulement un sub-bass à 45 Hz qui s'installe sous le silence.

---

### Plan 2 — L'installation de fortune — 4 s

**Intention :** il installe ce qu'il peut avec ce qu'il a : une serviette de bain sur le lit en guise de nappe, et la télé en guise de compagnie.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 2. POV première personne, 24 mm f/2.0, caméra portée à hauteur d'yeux, puis descente de
60 cm en s'asseyant. MAINS : mains adultes, ongles courts, aucune bague, bracelet de montre en
cuir noir usé au poignet gauche, manches de hoodie gris chiné remontées. ACTION : les deux
mains déplient une serviette de bain blanche un peu grise et l'étalent maladroitement sur la
housse de couette gris anthracite froissée, en guise de nappe, puis posent dessus le sac de
livraison blanc et un grand gobelet de soda en carton avec couvercle et paille. La caméra
descend et se stabilise, le héros vient de s'asseoir au bord du lit, face à la télé LCD posée
sur la commode à 2,50 m, dont le bleu clignotant est déjà la seule lumière de la pièce.
DÉCOR A. LUMIÈRE A. MATIÈRE : coton bouclette un peu raide de la serviette, couette pelucheuse
qui s'affaisse, condensation sur le gobelet, poussière sur la dalle de l'écran. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 2. First-person POV, 24 mm f/2.0, handheld camera at eye level, then dropping 60 cm as he
sits. HANDS: adult hands, short nails, no rings, worn black leather watch strap on the left
wrist, heather-grey hoodie sleeves pushed up. ACTION: both hands unfold a greyish white bath
towel and spread it clumsily over the crumpled charcoal-grey duvet cover as a makeshift
tablecloth, then set on it the white delivery bag and a large cardboard soda cup with a lid and
a straw. The camera lowers and settles as the hero sits on the edge of the bed, facing the LCD
TV on the dresser 2.5 m away, whose flickering blue is already the only light in the room.
SET A. LIGHT A. TEXTURE: slightly stiff looped cotton towel, fuzzy duvet sinking under the
weight, condensation on the cup, dust on the screen panel. 9:16.
```

**Son :** très gros plan tactile : la serviette éponge qu'on secoue puis qu'on frotte sur le synthétique du lit, sommier qui grince, gobelet posé sur la serviette. Derrière, la télé n'est qu'une bouillie étouffée et indistincte, comme sortie d'un haut-parleur de 3 cm. Le sub monte d'un demi-ton. Toujours aucune mélodie.

---

### Plan 3 — L'ouverture — 3 s

**Intention :** le moment où il pense être bien : la boîte s'ouvre, le burger est énorme, la mayo est partout. Variantes possibles : sushis + sauce soja, ou bol de ramen.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 3. POV première personne, 24 mm f/2.0, caméra à hauteur d'yeux d'un homme assis
(1,10 m), penchée vers le bas de 30°, mise au point proche, faible profondeur de champ.
MAINS : mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir usé au
poignet gauche, manches de hoodie gris chiné remontées. ACTION : les mains ouvrent le sac de
livraison blanc posé sur la serviette de bain, en sortent une boîte en carton kraft neutre,
soulèvent le couvercle qui résiste et se décolle d'un coup : à l'intérieur, un gros burger
débordant de salade verte et de mayonnaise épaisse, un cornet de frites et deux sachets de
sauce. Les deux mains saisissent le burger et le soulèvent vers le haut du cadre ; le pain se
comprime, la salade glisse déjà.
DÉCOR A, télé LCD allumée hors foyer au fond du cadre. LUMIÈRE A, reflets bleutés sur la
mayonnaise et le carton. MATIÈRE : carton kraft gras et mou, pain brillant, salade luisante,
mayonnaise crémeuse, frites molles collées entre elles, buée de chaleur. Aucun logo de marque
sur l'emballage. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 3. First-person POV, 24 mm f/2.0, camera at the eye level of a seated man (1.10 m), tilted
30° down, close focus, shallow depth of field. HANDS: adult hands, short nails, no rings, worn
black leather watch strap on the left wrist, heather-grey hoodie sleeves pushed up. ACTION: the
hands open the white delivery bag resting on the bath towel, pull out a plain kraft cardboard
box, lift the stiff lid which peels off at once: inside, a huge burger overflowing with green
lettuce and thick mayonnaise, a carton of fries and two sauce sachets. Both hands grip the
burger and lift it toward the top of frame; the bun compresses, the lettuce is already sliding.
SET A, LCD TV on and out of focus at the back of frame. LIGHT A, blue sheen on the mayonnaise
and the cardboard. TEXTURE: greasy soft kraft cardboard, glossy bun, glistening lettuce, creamy
mayonnaise, limp fries stuck together, heat haze. No brand logos on the packaging. 9:16.
```

**Son :** le couvercle plastifié qui se décolle du carton — son le plus net du film jusqu'ici, poussé jusqu'à l'inconfort. Papier gras, frites qui s'écrasent, respiration un peu lourde. Un seul accord de piano très bas et réverbéré sous la nappe grave. La télé continue de parler dans le vide, étouffée.

---

### Plan 4 — Et paf — 5 s

**Intention :** le plan pivot de la première moitié : le burger redescend avec une seule bouchée manquante, et tout le contenu tombe sur le lit.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 4. POV première personne, 24 mm f/2.0, caméra à hauteur d'yeux d'un homme assis
(1,10 m), penchée vers le bas de 40°, léger recul de la tête au moment de l'accident. MAINS :
mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir usé au poignet
gauche, manches de hoodie gris chiné remontées. ACTION : les deux mains redescendent le burger
dans le cadre, une seule bouchée manquante dans le pain ; le pain du dessus glisse, et une
grosse masse de mayonnaise, de salade et de jus orangé s'échappe par le bas et tombe en une
seule coulée épaisse sur la serviette de bain blanche puis sur la housse de couette gris
anthracite, où la tache s'élargit en auréole sombre et s'imprègne. La main gauche tente de
rattraper, étale, aggrave. Les doigts se séparent avec difficulté, luisants, des fils de sauce
tendus entre eux.
DÉCOR A, télé LCD allumée hors foyer au fond. LUMIÈRE A, la graisse accroche des reflets bleus.
MATIÈRE : mayonnaise épaisse qui file, sauce brune translucide, tissu qui boit le liquide et
fonce, doigts brillants et collants. Pas d'effet comique exagéré. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 4. First-person POV, 24 mm f/2.0, camera at the eye level of a seated man (1.10 m), tilted
40° down, a small head recoil at the moment of the spill. HANDS: adult hands, short nails, no
rings, worn black leather watch strap on the left wrist, heather-grey hoodie sleeves pushed up.
ACTION: both hands bring the burger back down into frame, a single bite missing from the bun;
the top bun slides off and a thick mass of mayonnaise, lettuce and orange juices escapes from
the bottom and falls in one heavy run onto the white bath towel and then onto the charcoal-grey
duvet cover, where the stain spreads into a dark halo and soaks in. The left hand tries to
catch it, smears it, makes it worse. The fingers peel apart with difficulty, glossy, strings of
sauce stretching between them.
SET A, LCD TV on and out of focus at the back. LIGHT A, grease catching blue highlights.
TEXTURE: thick stringing mayonnaise, translucent brown sauce, fabric drinking the liquid and
darkening, shiny tacky fingers. No exaggerated comedy. 9:16.
```

**Son :** le cœur sonore du film. Splat mouillé très détaillé, deux impacts de gouttes amplifiés jusqu'à l'absurde sur le tissu, et surtout le **claquement collant des doigts qui se décollent**, en très gros plan, presque obscène. Un soupir court et résigné (expiration, pas une voix). Le sub descend d'un cran, comme un ventre qui se creuse. Aucune musique mélodique : seulement la masse grave.

---

### Plan 5 — Il y a que de la merde à la télé — 3 s

**Intention :** il zappe avec un doigt collant, et une frite molle refuse de quitter son index. Point le plus sombre du film.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 5. POV première personne, 24 mm f/2.0, caméra à hauteur d'yeux d'un homme assis (1,10 m),
quasi immobile, mise au point verrouillée sur la main au premier plan. MAINS : mains adultes,
ongles courts, aucune bague, bracelet de montre en cuir noir usé au poignet gauche, manches de
hoodie gris chiné remontées. ACTION : au premier plan en bas du cadre, la main droite luisante
de graisse tient une télécommande noire bon marché et appuie deux fois, laissant des traces
brillantes sur le plastique ; une frite molle noyée de mayonnaise reste collée à l'index, pendue,
et refuse de tomber malgré deux secousses du poignet. Au fond, à 2,50 m, la télé LCD change de
chaîne : un plateau criard, une publicité saturée, des images génériques volontairement floues et
sans aucun texte lisible.
DÉCOR A, housse de couette tachée de sauce et serviette maculée au premier plan flou. LUMIÈRE A,
l'écran bat sur les murs à chaque changement de chaîne. MATIÈRE : plastique gras de la
télécommande, sauce filante, peau brillante, pixels visibles. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 5. First-person POV, 24 mm f/2.0, camera at the eye level of a seated man (1.10 m), almost
static, focus locked on the hand in the foreground. HANDS: adult hands, short nails, no rings,
worn black leather watch strap on the left wrist, heather-grey hoodie sleeves pushed up. ACTION:
in the lower foreground, the right hand, shiny with grease, holds a cheap black remote and
presses twice, leaving glossy smears on the plastic; a limp fry drowned in mayonnaise stays
stuck to the index finger, dangling, refusing to drop despite two flicks of the wrist. Behind,
2.5 m away, the LCD TV flips channels: a garish talk-show panel, an over-saturated commercial,
generic deliberately blurred images with no legible text anywhere.
SET A, sauce-stained duvet cover and soiled towel blurred in the foreground. LIGHT A, the screen
pulsing on the walls with each channel change. TEXTURE: greasy remote plastic, stringing sauce,
shiny skin, visible pixels. 9:16.
```

**Son :** deux clics secs, et à chaque clic un extrait ridicule et saturé coupé net : rire enregistré, jingle de pub. Tout en mono étroit, filtré, comme venu d'un haut-parleur minuscule. Entre les clics, le vide. Sous tout ça, le point le plus bas du film : nappe sinusoïdale ultra grave, une note de piano préparé qui résonne longuement, un souffle. Petit bruit collant quand les doigts s'écartent.

---

### Plan 6 — Le gobelet — 3 s

**Intention :** il se lève pour aller se laver les mains, et le gobelet se renverse. La petite humiliation de trop.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 6. POV première personne, 24 mm f/2.0, caméra qui se relève de 1,10 m à 1,70 m (le corps
quitte le bord du lit) avec un léger tangage, puis bascule brusquement vers le bas. MAINS :
mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir usé au poignet
gauche, manches de hoodie gris chiné remontées. ACTION : les deux mains sont tenues écartées du
corps, paumes vers le haut, doigts ouverts, visiblement poisseux et luisants, pour ne rien
toucher ; en se levant, le genou hors champ accroche le grand gobelet de soda posé sur la
serviette de bain : le gobelet bascule, le couvercle saute, un liquide brun mousseux se répand
en nappe sur la housse de couette gris anthracite et coule jusqu'au sol. La caméra plonge d'un
coup vers la flaque et s'immobilise, les mains restent suspendues en haut du cadre, impuissantes.
DÉCOR A, télé LCD allumée hors foyer. LUMIÈRE A, reflets bleus dans la flaque. MATIÈRE : mousse
brune, glaçons qui roulent, tissu qui s'assombrit en absorbant, moquette qui boit, gouttes qui
tombent une par une. Pas de slapstick appuyé. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 6. First-person POV, 24 mm f/2.0, camera rising from 1.10 m to 1.70 m (the body gets up off
the edge of the bed) with a slight sway, then tipping down sharply. HANDS: adult hands, short
nails, no rings, worn black leather watch strap on the left wrist, heather-grey hoodie sleeves
pushed up. ACTION: both hands are held away from the body, palms up, fingers spread, visibly
sticky and glossy, so as not to touch anything; as he stands, his off-screen knee catches the
large soda cup sitting on the bath towel: the cup tips over, the lid pops off, foamy brown liquid
floods across the charcoal-grey duvet cover and drips to the floor. The camera snaps down to the
puddle and holds, the hands still hanging at the top of frame, helpless.
SET A, LCD TV on and out of focus. LIGHT A, blue reflections in the puddle. TEXTURE: brown foam,
rolling ice cubes, fabric darkening as it absorbs, thirsty carpet, droplets falling one by one.
No broad slapstick. 9:16.
```

**Son :** sommier qui grince, pas sur la moquette, puis le choc sourd du gobelet, le glouglou du liquide qui se vide, les glaçons qui roulent, les gouttes au sol une par une. Aucun effet comique au son : la nappe grave reste tenue, imperturbable. Deux secondes de silence habité sur la flaque.

---

### Plan 7 — La fenêtre — 5 s

**Intention :** la bascule du film : un bruit dehors, et la lumière ambre des terrasses remonte et dore ses propres mains sur le châssis, dans le même plan.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 7. POV première personne, 24 mm f/2.0, caméra portée à hauteur d'yeux, deux pas d'avance
vers la fenêtre, puis bascule vers le bas de 60°, mise au point qui glisse du rideau à la rue en
contrebas. MAINS : mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir
usé au poignet gauche, manches de hoodie gris chiné remontées. ACTION : la caméra traverse la
pièce en deux pas vers la fenêtre à un seul battant ; le dos du poignet pousse le rideau fin
blanc et la main se pose à plat sur le châssis pour le refermer, puis s'arrête net. Le regard
plonge par-dessus l'appui, trois étages plus bas, sur une rue de ville européenne pavée et
humide : deux terrasses de bistrot avec guirlandes d'ampoules, nappes en papier, des convives
attablés qui rient la tête en arrière, lèvent des verres de vin rouge et des demis de bière,
trinquent, se partagent de grands plats fumants ; un serveur slalome avec un plateau.
PREMIÈRE MOITIÉ DU PLAN : LUMIÈRE A, bleu froid clignotant sur les mains et le rideau. DEUXIÈME
MOITIÉ : la lumière ambre 2700 K des terrasses remonte et DORE LES MAINS SUR LE CHÂSSIS, la
saturation revient, les ampoules passent en gros bokeh rond, le cadre s'ouvre.
MATIÈRE : vitre sale piquée de pluie séchée, peinture écaillée de l'appui, voile du rideau, pavés
luisants, vapeur des plats, buée des verres. Aucun reflet du héros dans la vitre. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 7. First-person POV, 24 mm f/2.0, handheld camera at eye level, two steps forward to the
window, then a 60° tilt down, focus racking from the curtain to the street below. HANDS: adult
hands, short nails, no rings, worn black leather watch strap on the left wrist, heather-grey
hoodie sleeves pushed up. ACTION: the camera crosses the room in two steps toward the single-pane
window; the back of the wrist pushes the thin white curtain aside and the hand lies flat on the
sash to close it, then stops dead. The gaze drops over the sill, three floors down, onto a wet
cobbled European city street: two bistro terraces strung with festoon bulbs, paper tablecloths,
diners laughing with their heads thrown back, raising glasses of red wine and beer, clinking
them, sharing big steaming dishes; a waiter weaves through with a tray.
FIRST HALF OF THE SHOT: LIGHT A, cold flickering blue on the hands and the curtain. SECOND HALF:
the amber 2700 K light of the terraces rises and GILDS THE HANDS ON THE SASH, saturation returns,
the bulbs bloom into large round bokeh, the frame opens up.
TEXTURE: dirty glass speckled with dried rain, flaking paint on the sill, sheer curtain,
glistening cobblestones, steam off the plates, fogged glasses. No reflection of the hero in the
glass. 9:16.
```

**Son :** le pivot de mixage. D'abord un bruit sourd et lointain derrière la vitre — un éclat de rire filtré passe-bas, mono, comme à travers un mur. La fenêtre s'ouvre d'un cran et le filtre s'ouvre d'un coup : **bascule franche vers le stéréo large** — brouhaha chaleureux, rires francs, verres qui trinquent, couverts sur la porcelaine, une guitare lointaine, un scooter. **Ne pas réharmoniser : la vie EST la musique ici, on ne lui ajoute rien.** La nappe grave ne s'arrête pas, elle se résout en un seul accord majeur chaud, très doux, et continue dessous.

---

### Plan 8 — La poubelle — 3 s

**Intention :** le geste de rupture : il jette la commande à peine entamée, une seule bouchée manquante, et la musique meurt sur le claquement du couvercle.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 8. POV première personne, 24 mm f/2.0, caméra à hauteur d'yeux penchée vers le bas, un
demi-tour sur place puis trois pas. MAINS : mains adultes, ongles courts, aucune bague, bracelet
de montre en cuir noir usé au poignet gauche, manches de hoodie gris chiné remontées. ACTION : la
caméra se retourne vers le lit ; les deux mains raflent d'un seul geste décidé la boîte en carton
kraft avec le burger à peine entamé — une seule bouchée manquante —, le cornet de frites molles
et le gobelet renversé, les empilent dans le sac de livraison blanc, trois pas vers le coin de la
pièce, un pied hors champ appuie sur la pédale et les mains lâchent tout d'un coup sec dans la
petite poubelle en plastique gris ; le couvercle claque.
DÉCOR A, housse de couette tachée de sauce et de soda, serviette de bain maculée, télé LCD
toujours allumée hors foyer, fenêtre entrouverte. LUMIÈRE A, mais une première lame de lumière
ambre 2700 K entre par la fenêtre entrouverte et coupe la pièce en deux. MATIÈRE : carton gras et
mou, sauce qui file, plastique du sac, plastique mat de la poubelle. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 8. First-person POV, 24 mm f/2.0, camera at eye level tilted down, a half-turn on the spot
then three steps. HANDS: adult hands, short nails, no rings, worn black leather watch strap on
the left wrist, heather-grey hoodie sleeves pushed up. ACTION: the camera turns back toward the
bed; both hands sweep up in one decisive move the kraft cardboard box with the barely touched
burger — a single bite missing —, the carton of limp fries and the tipped-over cup, stack them
inside the white delivery bag, three steps to the corner of the room, an off-frame foot presses
the pedal and the hands drop the whole thing in one sharp motion into the small grey plastic bin;
the lid snaps shut.
SET A, duvet cover stained with sauce and soda, soiled bath towel, LCD TV still on and out of
focus, window ajar. LIGHT A, but a first blade of warm amber 2700 K light comes through the open
window and cuts the room in two. TEXTURE: greasy soft cardboard, stringing sauce, plastic bag,
matte plastic bin. 9:16.
```

**Son :** froissement rageur, carton qu'on rafle, pédale, et le **claquement du couvercle sur lequel la nappe grave s'arrête NET, en pleine phrase**. Puis deux temps de silence habité : il ne reste que la rue en bas, lointaine et chaude, par la fenêtre entrouverte. C'est ce silence qui rend sa décision audible.

---

### Plan 9 — Le téléphone — 2 s

**Intention :** le seul plan produit du film : il prend son téléphone, ouvre EatSolo, attrape ses clés. C'est l'appli qui provoque la bascule.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 9. POV première personne, 24 mm f/2.0, caméra à hauteur d'yeux penchée sur les mains,
profondeur de champ très courte. MAINS : mains adultes, ongles courts, aucune bague, bracelet de
montre en cuir noir usé au poignet gauche, manches de hoodie gris chiné remontées. ACTION : la
main gauche attrape un smartphone noir posé sur la housse de couette tachée, le pouce droit
l'effleure et l'écran s'allume d'un halo propre et lumineux qui éclaire la paume — ÉCRAN
VOLONTAIREMENT NEUTRE ET SANS AUCUN TEXTE, surface lumineuse unie, l'interface sera incrustée en
post-production. La main droite balaie ensuite la commode et récupère un trousseau de clés.
DÉCOR A. LUMIÈRE A à gauche du cadre, lame de lumière ambre 2700 K venue de la fenêtre ouverte à
droite : deux températures qui s'affrontent sur les mains. MATIÈRE : traces de sauce sur l'écran,
halo du téléphone sur la peau, métal des clés. Aucun texte généré, aucune interface générée. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 9. First-person POV, 24 mm f/2.0, camera at eye level looking down at the hands, very
shallow depth of field. HANDS: adult hands, short nails, no rings, worn black leather watch strap
on the left wrist, heather-grey hoodie sleeves pushed up. ACTION: the left hand grabs a black
smartphone off the stained duvet cover, the right thumb brushes it and the screen wakes with a
clean bright halo lighting the palm — SCREEN DELIBERATELY NEUTRAL AND COMPLETELY TEXT-FREE, a
plain glowing surface; the app UI will be composited in post. The right hand then sweeps the
dresser and picks up a keyring.
SET A. LIGHT A on the left of frame, a blade of warm amber 2700 K light from the open window on
the right: two colour temperatures fighting across the hands. TEXTURE: sauce smears on the
screen, phone glow on skin, metal keys. No generated text, no generated interface. 9:16.
```

**Son :** le silence habité du plan 8 se prolonge une demi-seconde, puis un **« ding » EatSolo** clair et net — premier son aigu et propre du film — et le cliquetis des clés, libérateur. La musique chaude naît là : contrebasse pincée, un balai de batterie qui démarre.

---

### Plan 10 — La descente — 3 s

**Intention :** quelques marches, une porte vitrée, et la lumière chaude lui tombe dessus d'un coup.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 10. POV première personne, 35 mm f/2.0, caméra portée à hauteur d'yeux, descente d'escalier
avec balancement vertical marqué à chaque marche. MAINS : mains adultes, ongles courts, aucune
bague, bracelet de montre en cuir noir usé au poignet gauche, manches de hoodie gris chiné
remontées. ACTION : la main gauche glisse sur une rampe en bois vernis tandis que la caméra
descend une volée de petites marches d'immeuble ancien, carrelage à motifs, minuterie jaunâtre ;
la main droite pousse une lourde porte vitrée et la caméra débouche dans la rue.
Transition de lumière franche : de la minuterie jaune de la cage d'escalier à DÉCOR B / LUMIÈRE B,
guirlandes d'ampoules en gros bokeh rond, pavés humides qui renvoient l'ambre, terrasse de bistrot
droit devant à cinq mètres avec ses convives attablés. La caméra avance vers la terrasse.
MATIÈRE : bois verni de la rampe, carrelage usé, verre épais de la porte, pavés luisants, buée des
verres. Aucune enseigne de marque réelle. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 10. First-person POV, 35 mm f/2.0, handheld camera at eye level, descending stairs with a
pronounced vertical bob on each step. HANDS: adult hands, short nails, no rings, worn black
leather watch strap on the left wrist, heather-grey hoodie sleeves pushed up. ACTION: the left
hand slides along a varnished wooden banister as the camera goes down a short flight of steps in
an old apartment building, patterned floor tiles, yellowish stairwell light; the right hand pushes
a heavy glazed door and the camera emerges onto the street.
Hard lighting transition: from the yellow stairwell light to SET B / LIGHT B, festoon bulbs in
large round bokeh, wet cobblestones throwing back the amber, a bistro terrace straight ahead five
metres away with its seated diners. The camera walks toward the terrace.
TEXTURE: varnished banister wood, worn tiles, thick door glass, glistening cobbles, condensation
on the glasses. No real brand signage. 9:16.
```

**Son :** pas qui descendent, main qui frotte la rampe, porte vitrée lourde et son ferme-porte pneumatique, puis la rue qui s'ouvre en grand stéréo : brouhaha, rires, couverts, cuisine au fond, un vélo. Le morceau s'étoffe : guitare, contrebasse ronde, tempo médium, chaleureux. Aucun mot intelligible : c'est de la texture humaine, pas du dialogue.

---

### Plan 11 — Le chien — 5 s

**Intention :** il s'assoit, et en face il y a quelqu'un : un chien en chemise de lin, bonne tête, qui lui pousse la corbeille de pain — et à la table voisine, des humains lèvent leur verre vers lui.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 11. POV première personne, 35 mm f/2.0, caméra à hauteur d'yeux qui descend de 1,70 m à
1,10 m en s'asseyant puis se stabilise, légère avance de 20 cm, micro-tremblements de respiration
apaisée. MAINS : mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir usé
au poignet gauche, manches de hoodie gris chiné remontées. ACTION : les mains tirent une chaise en
rotin, la caméra s'assoit à une petite table ronde de terrasse à nappe de papier, et découvre
assis en face, à 80 cm, LE CHIEN (voir bloc) : il relève la tête de son menu, incline les
oreilles, plisse les yeux de plaisir en signe de bienvenue et pousse d'une patte une corbeille de
pain vers la caméra, tandis que la main droite du héros se pose à plat sur la table. À la table
voisine, nette mais au second plan, un petit groupe de convives humains se tourne une demi-seconde
vers la caméra et lève son verre en souriant.
DÉCOR B. LUMIÈRE B, guirlandes en gros bokeh rond derrière le chien, poil doré en contre-jour.
MATIÈRE : lin froissé de la chemise, poil fin et brillant, truffe humide, rotin tressé, papier de
la nappe, buée de la carafe. Le chien ne parle pas, pas de synchro labiale, pas de sourire humain.
9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 11. First-person POV, 35 mm f/2.0, camera at eye level lowering from 1.70 m to 1.10 m as he
sits, then settling, a slight 20 cm push in, micro shake of calmed breathing. HANDS: adult hands,
short nails, no rings, worn black leather watch strap on the left wrist, heather-grey hoodie
sleeves pushed up. ACTION: the hands pull out a rattan chair, the camera sits down at a small
round terrace table with a paper tablecloth, and discovers, seated opposite at 80 cm, THE DOG
(see block): he lifts his head from his menu, tilts his ears, crinkles his eyes with pleasure in
welcome and nudges a bread basket toward the camera with one paw, while the hero's right hand
settles flat on the table. At the next table, sharp but in the second plane, a small group of
human diners turns toward the camera for half a second and raises their glasses with a smile.
SET B. LIGHT B, large round bokeh bulbs behind the dog, fur rim-lit gold. TEXTURE: creased linen
shirt, fine glossy fur, wet nose, woven rattan, paper tablecloth, condensation on the carafe. The
dog does not speak, no lip sync, no human smile. 9:16.
```

**Son :** chaise en rotin qu'on tire sur les pavés, soupir d'installation, nappe en papier, corbeille de pain posée sur la table, un petit grognement amical et un souffle de chien, rires des tables voisines, couverts, un bouchon qui saute au loin. Le morceau s'ouvre en grand, chaud et généreux.

---

### Plan 12 — Le trinquement — 4 s

**Intention :** il mange enfin, le chien se régale, et les deux verres se touchent au centre du cadre : plus rien ne coule, plus rien ne colle.

**Prompt FR**
```
[BLOC DE STYLE GLOBAL — FR]
PLAN 12. POV première personne, 35 mm f/2.0, caméra à hauteur d'yeux d'un homme assis (1,10 m),
stable, micro-tremblements de respiration, légère avance de 10 cm sur le trinquement. MAINS :
mains adultes, ongles courts, aucune bague, bracelet de montre en cuir noir usé au poignet gauche,
manches de hoodie gris chiné remontées. ACTION : sur la petite table ronde à nappe de papier, deux
assiettes généreuses et magnifiques fument ; en face, à 80 cm, LE CHIEN (voir bloc) mange de bon
appétit, gourmand et joyeux, et se tamponne le museau avec sa serviette ; puis il saisit un verre
à pied posé devant lui, le lève et le tend vers la caméra. La main droite du héros lève son propre
verre et les deux verres se touchent exactement au centre du cadre, en pleine lumière. Le vin
oscille, la lumière des ampoules traverse le verre.
DÉCOR B. LUMIÈRE B, guirlandes en gros bokeh derrière le chien, reflets ambrés dans le vin.
MATIÈRE : vin profond et translucide, verre fin, lin froissé, poil doré, vapeur des plats.
Rien ne se renverse, rien ne colle. Le chien ne parle pas, pas de synchro labiale. 9:16.
```

**Prompt EN**
```
[GLOBAL STYLE BLOCK — EN]
SHOT 12. First-person POV, 35 mm f/2.0, camera at the eye level of a seated man (1.10 m), steady,
micro breathing shake, a slight 10 cm push in on the toast. HANDS: adult hands, short nails, no
rings, worn black leather watch strap on the left wrist, heather-grey hoodie sleeves pushed up.
ACTION: on the small round table with its paper tablecloth, two generous beautiful plates are
steaming; opposite, 80 cm away, THE DOG (see block) eats with gusto, happy and greedy, and dabs
his muzzle with his napkin; then he takes a stemmed glass standing in front of him, raises it and
holds it out toward the camera. The hero's right hand lifts his own glass and the two glasses meet
exactly at the centre of frame, in full light. The wine sways, bulb light passes through the glass.
SET B. LIGHT B, large bokeh bulbs behind the dog, amber refractions in the wine.
TEXTURE: deep translucent wine, thin glass, creased linen, golden fur, steam off the plates.
Nothing spills, nothing sticks. The dog does not speak, no lip sync. 9:16.
```

**Son :** plein régime chaleureux : couverts, mastication heureuse et discrète du chien, queue qui tape contre le bois de la chaise, serviette, rires au loin, vin qu'on verse. Puis tout se retire d'un coup sur le dernier geste : le **« cling » des deux verres reste seul**, net, isolé, avec une queue de réverbération.

---

## 4. La fin, et comment arrive « Never EatSolo Again »

Le **cling** du plan 12 est le dernier son du film. Rien ne vient par-dessus : pas de voix off, pas de slogan dit, aucun dialogue sur les 43 secondes. C'est le trinquement qui justifie la phrase, pas l'inverse.

1. **Coupe franche sur le cling**, fondu au noir chaud : un noir profond piqué de deux ou trois ampoules de guirlande encore en bokeh, récupérées du plan 12 et désaturées vers l'ambre. Le brouhaha de la terrasse continue **une seconde dans le noir**, légèrement filtré, comme si on s'éloignait.
2. **Sur ce fond, 3 secondes de carton final, entièrement monté en post-production** (After Effects / DaVinci), jamais généré par le modèle. La baseline se compose en deux temps :
   - « **Never Eat Solo** » s'écrit, en blanc, sans-serif fin, centré ;
   - le mot « **Again** » vient se poser — et dans le même mouvement **l'espace entre « Eat » et « Solo » se referme** pour former le logotype : **NEVER EATSOLO AGAIN**.
   C'est la baseline qui apprend la marque, en un seul geste typographique.
3. **Dernière demi-seconde** : les ampoules s'éteignent une par une, le noir se ferme. Il ne reste que le logo EatSolo et, tout en bas en petit, les pictos App Store / Google Play. Le même petit « ding » que celui du téléphone au plan 9 referme le film : c'est l'appli qui a provoqué la bascule, c'est elle qui signe.

**Total : 43 s de plans + 3 s de carton = 46 s.** Version réseaux de 35 s : couper les plans 3 et 9 et raccourcir le plan 5 — **jamais le plan 7**, c'est la charnière du film.

Comme il n'y a ni voix off ni dialogue, le film ne contient aucune langue : il s'exporte tel quel sur tous les marchés, seul le carton final change. La punchline reste **« Never EatSolo Again »** partout, y compris en France.

---

## 5. Les pièges connus des générateurs, et comment les contourner

**1. Le POV qui décroche.** C'est le risque numéro un : les modèles repassent spontanément en caméra tierce au milieu du plan, ou font apparaître un visage, un reflet dans la vitre ou l'écran. Parades cumulatives : la règle POV est répétée en tête de chaque prompt ; « visage, reflet, miroir, contrechamp, caméra à la troisième personne » sont dans le champ négatif dédié ; et si la dérive persiste, renforcer avec *« the camera is the character's eyes, the character is never visible, no reverse shot, no face anywhere in the frame »*, puis couper le plan avant la dérive. Toute prise où un visage ou un reflet apparaît est jetée sans discussion.

**2. La morsure, jamais filmée.** On ne demande à aucun moment au modèle de faire mordre le héros : c'est l'instruction qui déclenche le plus sûrement un contrechamp ou une bouche. La bouchée a lieu **entre** les plans 3 et 4 ; le plan 4 part du burger qui redescend dans le cadre avec une morsure manquante dans le pain. C'est un détail statique, sans mouvement de mâchoire, donc sans risque.

**3. Les mains.** Un film 100 % POV demande 43 secondes de mains qui manipulent des objets : doigts fondus, sixième doigt, objet qui traverse la paume. Parades : générer d'abord **une image fixe de référence des mains** (à partir du plan 3), la valider, et travailler **tous** les plans en image-to-video depuis des premières frames validées, jamais en text-to-video pur. Deux mains visibles en même temps multiplient les six doigts : privilégier une seule main dans le cadre quand l'action le permet. Prévoir 5 à 10 générations sur les plans 3, 4, 8 et 12.

**4. La continuité du chien.** Deux pièges : la cohérence entre les plans 11 et 12 (museau, pelage, chemise), et la vallée de l'étrange — un chien qui mâche en gros plan devient vite inquiétant ou grotesque, exactement ce que le client refuse. Parades : fabriquer le chien **une seule fois** en image fixe jusqu'à obtenir LA bonne tête, l'enregistrer comme **référence de personnage** (character reference / élément de référence) et l'utiliser en image-to-video sur les deux plans ; garder le chien à 80 cm et jamais en très gros plan ; limiter la mastication à une seconde ; préférer un geste lisible (serviette, corbeille de pain, verre levé) à une animation de gueule complexe. Certains modèles refusent d'habiller un animal : reformuler en *« anthropomorphic golden retriever wearing a linen shirt »*, jamais « déguisé ».

**5. La patte et le verre à pied.** Faire saisir, lever et trinquer un verre fin par une patte avant est le geste le plus fragile du film — et il porte toute la fin. Deux parades : le verre est **déjà posé devant le chien** (il le prend, il ne le sort pas de nulle part) ; et plan B si l'échec persiste : le chien pose simplement la patte à côté du verre déjà posé et c'est **la main du héros** qui vient le toucher, le cling reste identique au montage. Attention aussi aux filtres alcool de certains générateurs, qui se déclenchent davantage sur un animal : remplacer le vin par un verre d'eau ambrée ou une limonade si le prompt est refusé.

**6. Les liquides.** La coulée du plan 4 et le gobelet du plan 6 sont de la simulation fluide : les modèles produisent souvent une tache qui apparaît par magie plutôt qu'un écoulement crédible (Veo s'en sort le mieux, Runway beaucoup moins). Parades : cadrer serré, accepter 1,5 seconde utile sur 8, et porter le reste du collant **au son** (succion des doigts, splat) plutôt qu'à l'image. Repli : générer la tache déjà formée que les doigts viennent toucher. Repli ultime et imbattable : tourner ces deux plans en vrai, iPhone en POV — deux heures de tournage.

**7. La continuité du décor.** Neuf plans dans la même chambre donneront neuf chambres différentes en text-to-video. Parade obligatoire : générer d'abord le plan 2, en extraire **une image clé de la chambre**, la verrouiller et la réutiliser comme première frame des plans 1, 3, 4, 5, 6, 8 et 9, même seed ; même méthode avec une image clé de terrasse pour les plans 10 à 12. Faire progresser les taches dans l'ordre (petite au plan 4, large à partir du 6) et prévoir un étalonnage final commun (froid 5600 K sur 1-9, chaud 2700 K sur 10-12) pour rattraper les écarts.

**8. Le texte à l'écran.** Ne jamais demander au modèle d'écrire « Never EatSolo Again », le logo, ou une interface d'application : il produira du charabia typographique et des lettres fantômes. Le plan 9 est généré avec un **écran de téléphone volontairement vide et lumineux**, l'interface EatSolo est incrustée en post. Tout le carton final est monté. Même logique pour les emballages : exiger explicitement « aucun logo de marque », sinon un faux McDonald's ou un faux Uber Eats peut apparaître — problème juridique immédiat vu le positionnement du film contre les plateformes de livraison.

**9. Les négatifs au bon endroit.** Les listes « à éviter » écrites en prose dans le corps d'un prompt ne sont pas traitées comme des négations et peuvent au contraire convoquer le reflet ou le watermark. Elles vont dans le **champ negative prompt dédié** (Kling, Runway, Luma). Si le modèle n'en a pas, les coller en toute dernière ligne, jamais au milieu de la description.

**10. La télé du plan 5.** Les écrans dans l'écran dérapent toujours : texte illisible, logos de chaînes inventés. Rester sur des images abstraites, floues, cadrées de biais, ou incruster un plateau générique en post.

**11. Les durées.** Les modèles tiennent mal un timing précis et rendent 5 à 10 secondes. Générer chaque plan en 8 s minimum et retailler au montage — le timing du plan 4 et du plan 8 se joue à la demi-seconde.

**12. Le plan 7, le plus difficile.** Deux pas, une main qui ouvre, un panoramique vertical de 60° et un changement de température de couleur dans le même plan. S'il ne tient pas, le couper en deux générations — 7a : la main et le châssis en froid ; 7b : la plongée sur les terrasses en chaud — et faire la jonction au montage, en prenant 2 secondes de plus.

**13. Le son n'est pas un habillage, c'est la colonne vertébrale.** Seul Veo génère un son natif exploitable, et il reste approximatif. Considérer le sound design comme un poste de post-production à part entière : enregistrer soi-même les froissements, le claquement des doigts collants et le cling des verres, puis construire les deux états — **mono étroit + passe-bas + sub 45 Hz** sur les plans 1 à 6, **bascule franche vers le stéréo large** au plan 7, nappe grave qui **s'arrête net** sur le couvercle de poubelle au plan 8. C'est là que le film se gagne, pas dans la génération d'images. Faire composer 20 secondes de drone original : la musique du début ne doit pas pasticher une bande-annonce identifiable.

**14. Budget réaliste.** Compter 10 à 15 générations par plan utile, soit 130 à 180 clips pour un film de 45 secondes qui tient debout. Si le budget est serré, prioriser les plans **4, 7, 11 et 12** : ce sont les quatre que le client reconnaîtra dans son mémo.