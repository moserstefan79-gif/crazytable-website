#!/usr/bin/env python3
"""Erzeugt die HTML-Seiten von crazytable.ch aus gemeinsamen Bausteinen.
Aufruf: python3 build.py  -> schreibt *.html ins gleiche Verzeichnis."""
import os
import hashlib as _h
CSSV = _h.md5(open('css/style.css','rb').read()).hexdigest()[:8]
ROOT = os.path.dirname(os.path.abspath(__file__))

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=DM+Sans:wght@400;500&display=swap" rel="stylesheet">'

def head(title, desc, active):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="/css/style.css?v={CSSV}">
<script src="/js/main.js" defer></script>
</head>
<body>
<div class="site-header-bar"><header class="site-header">
  <a class="logo" href="/" aria-label="crazytable – Startseite"><img src="/img/logo-wordmark.png" alt="crazytable"></a>
  <button class="nav-toggle" aria-label="Menü öffnen" aria-expanded="false" onclick="var n=document.getElementById('nav');n.classList.toggle('is-open');this.setAttribute('aria-expanded',n.classList.contains('is-open'))"><span></span><span></span><span></span></button>
  <nav class="nav" id="nav" aria-label="Hauptnavigation">
    <a href="/verein"{' class="is-active"' if active=='verein' else ''}>Verein</a>
    <a href="/anlaesse"{' class="is-active"' if active=='anlaesse' else ''}>Anlässe</a>
    <a href="/weinkeller"{' class="is-active"' if active=='weinkeller' else ''}>Weinkeller</a>
    <a href="/weinkarte"{' class="is-active"' if active=='weinkarte' else ''}>Weinkarte</a>
    <a href="https://app.crazytable.ch" class="nav-muted">Login</a>
    <a href="/mitglied-werden" class="nav-cta">Mitglied werden</a>
  </nav>
</header></div>
<main>
'''

FOOTER = '''</main>
<div class="site-footer-bar"><footer class="site-footer">
  <div class="footer-grid">
    <div>
      <img src="/img/logo-wordmark.png" alt="crazytable" style="width:170px;height:auto">
      <span style="color:#9A9E9E;line-height:1.6">Weinclub crazytable<br>Kirchberg BE</span>
    </div>
    <div><span class="h">Club</span><a href="/verein">Verein &amp; Vorstand</a><a href="/anlaesse">Anlässe</a><a href="/weinkeller">Weinkeller</a><a href="/weinkarte">Weinkarte</a></div>
    <div><span class="h">Mitmachen</span><a href="/mitglied-werden">Mitglied werden</a><a href="/verein#ideenbox">Ideenbox</a><a href="https://app.crazytable.ch">Mitglieder-Login</a></div>
    <div><span class="h">Kontakt</span><a href="mailto:stefan.moser@crazytable.ch">stefan.moser@crazytable.ch</a><a href="/mitglied-werden#kontakt">Kontaktformular</a></div>
  </div>
  <div class="footer-bottom">
    <span>© 2026 crazytable</span>
    <div><a href="/disclaimer">Disclaimer</a><a href="/datenschutz">Datenschutz</a></div>
  </div>
</footer></div>
</body>
</html>
'''

# Flickr-Vorschaubilder der bestehenden Alben (eigene Fotos des Clubs)
IMG = {
    'wallis': 'https://live.staticflickr.com/65535/54880879188_05c9672cb7_h.jpg',
    'spanien': 'https://live.staticflickr.com/65535/54111130562_cd2877fe50_h.jpg',
    'suedamerika': 'https://live.staticflickr.com/65535/52874320499_2cf5318c6c_b.jpg',
    'portugal': 'https://live.staticflickr.com/65535/53241396242_9f34a2e731_h.jpg',
    'bordeaux': 'https://live.staticflickr.com/65535/52875887701_20704ac5eb_b.jpg',
    'toskana': 'https://live.staticflickr.com/65535/55625556769_0d6940e498_h.jpg',
    'wild': 'https://live.staticflickr.com/65535/55625496583_50e0652477_h.jpg',
}
ALB = {'bordeaux':'https://www.flickr.com/photos/197768276@N04/albums/72177720308054037','portugal':'https://www.flickr.com/photos/197768276@N04/albums/72177720311759268','suedamerika':'https://www.flickr.com/photos/197768276@N04/albums/72177720321668673','spanien':'https://www.flickr.com/photos/197768276@N04/albums/72177720326339771','wallis':'https://www.flickr.com/photos/197768276@N04/albums/72177720329907542','toskana':'https://www.flickr.com/photos/197768276@N04/albums/72177720336438916','wild':'https://www.flickr.com/photos/197768276@N04/albums/72177720336449833'}

def ph(label, cls='ratio-45', img=None, alt=''):
    if img:
        return f'<div class="ph {cls}" style="padding:0;overflow:hidden"><img class="img-cover" src="{img}" alt="{alt}" loading="lazy"></div>'
    return f'<div class="ph {cls}"><span>[{label}]</span></div>'

NEXT_EVENT = '''
<section class="section grid-12" style="align-items:start">
  <div class="c1-3 stack-sm stack">
    <p class="overline">Nächster Anlass</p>
    <span style="font-family:var(--serif);font-size:72px;line-height:1">26.</span>
    <span style="font-size:15px;color:var(--text)">Mai 2027 — Mittwoch, 18.30–23 Uhr</span>
    <span style="font-size:15px;color:var(--muted)">Kargo68, Zuchwil / Solothurn</span>
  </div>
  <div class="c4-6 stack">
    <h2 style="font-size:44px">Doce Copas – zwölf Gläser Spanien</h2>
    <p class="lead" style="font-size:17px">Zwölf spanische Weine, ausgesucht mit Vinos de España aus der Region Solothurn, dazu eine kulinarische Begleitung zu jedem Glas und viel Zeit am Tisch.</p>
    <span class="small">Für Mitglieder · Details folgen im Frühjahr 2027</span>
  </div>
  <div class="c10-3 stack stack-sm" style="padding-top:6px">
    <a class="btn btn-dark" href="/anlaesse#doce-copas">Mehr Informationen</a>
    <a class="btn btn-ghost" href="https://app.crazytable.ch/app">Anmelden (Mitglieder)</a>
    <a class="btn btn-ghost" href="/termine.ics">In Kalender</a>
    <a class="arrow" href="/anlaesse" style="text-align:center;padding-top:8px">Alle Anlässe →</a>
  </div>
</section>'''

INDEX = head('crazytable – Weinclub in Kirchberg BE', 'Weinclub in Kirchberg BE: zwei Degustationen pro Jahr, Winzer persönlich kennenlernen, gemeinsamer Weinkeller. Maximal 25 Mitglieder.', 'home') + f'''
<section class="hero hero-grid" style="border-bottom:1px solid var(--line);max-width:1280px;margin:0 auto">
  <div class="hero-top stack stack-lg">
    <p class="overline">Weinclub — Kirchberg BE — seit 2023</p>
    <h1>Ein Tisch.<br>Viele Gläser.<br><em class="accent">Gute Geschichten.</em></h1>
  </div>
  <div class="hero-img">{ph('', img='/img/hero.jpg', alt='Weinkeller mit Barriques und Flaschenregal')}</div>
  <div class="hero-bottom stack stack-lg">
    <p class="lead" style="max-width:480px">Zweimal im Jahr kommen wir zusammen – zu einem Degustationsabend oder einer Reise, mit Weinen aus aller Welt und den Geschichten dahinter. Und Jahr für Jahr wächst unser gemeinsamer Keller voller Trouvaillen.</p>
    <div class="row">
      <a class="btn btn-primary" href="/anlaesse">Anlässe</a>
      <a class="btn btn-outline" href="/mitglied-werden">Mitglied werden</a>
      <a class="btn btn-ghost" href="/weinkeller">Weinkeller</a>
    </div>
  </div>
</section>

<div class="stats">
  <div class="stat"><b>2</b><span>Anlässe pro Jahr – Degustation oder Reise, immer mit Menü</span></div>
  <div class="stat"><b>12+</b><span>neue Weine pro Jahr im Glas</span></div>
  <div class="stat"><b>25</b><span>Mitglieder maximal – der Club bleibt ein Tisch</span></div>
  <div class="stat"><b>20 %</b><span>des Beitrags fliessen in den gemeinsamen Weinkeller</span></div>
</div>

<div class="wrap" style="padding:0">{NEXT_EVENT}

<section class="section grid-12" style="row-gap:56px">
  <div class="c1-4 stack">
    <p class="overline">Der Club</p>
    <h2>Vier Dinge, die uns ausmachen</h2>
  </div>
  <ol class="rules c6-7">
    <li><span class="n">01</span><h3>Die Idee</h3><p>Gemeinsame Aktivitäten rund um Wein und Weinproduktion. Wir pflegen das regionale Gemeinschaftsgefühl – und der Wein spielt dabei immer die Hauptrolle.</p></li>
    <li><span class="n">02</span><h3>Die Degustationen</h3><p>Zwei Anlässe pro Jahr – mal ein Degustationsabend, mal eine Reise. Jedes Mal ein Thema, mindestens sechs Weine im Glas und Menschen, die sie kennen: Winzer, Importeure, Weinfreunde. Dazu immer ein passendes Essen.</p></li>
    <li><span class="n">03</span><h3>Der Weinkeller</h3><p>Einmal im Jahr entscheiden wir an der Hauptversammlung gemeinsam, welche Trouvaille in den Clubkeller kommt – 20 % der Beiträge, Weine, die wir in ein paar Jahren zusammen öffnen.</p></li>
    <li><span class="n">04</span><h3>Der Verein</h3><p>Gegründet am 1. März 2023 in Kirchberg BE. Maximal 25 Mitglieder, CHF 350 Jahresbeitrag – darin enthalten: zwei Anlässe inklusive Essen und dein Anteil am Keller.</p></li>
  </ol>
</section>

<section class="section stack" style="gap:40px">
  <div class="between reveal">
    <h2>Rückblick</h2>
    <a class="link-u" href="/anlaesse">Alle Berichte und Fotos</a>
  </div>
  <div class="cards">
    <a class="card" href="/anlaesse#wild-2026">{ph('', img=IMG['wild'], alt='Wild on Tour, Solothurn, Oktober 2026')}<span class="meta">17. Oktober 2026 — Degustationstag</span><h3>Wild on Tour – vier Stationen durch Solothurn</h3></a>
    <a class="card" href="/anlaesse#toskana-2026">{ph('', img=IMG['toskana'], alt='Degustationsabend Toskana, Mai 2026')}<span class="meta">8. Mai 2026 — Degustationsabend</span><h3>Toskana – vier Weingüter im Glas</h3></a>
    <a class="card" href="/anlaesse#wallis-2025">{ph('', img=IMG['wallis'], alt='Degustationsreise ins Wallis, Oktober 2025')}<span class="meta">25. Oktober 2025 — Reise</span><h3>Ins Wallis und nach Gruyères</h3></a>
  </div>
</section>
</div>

<section class="band-green">
  <div class="wrap grid-12" style="padding:0;align-items:end">
    <div class="c1-8 stack stack-lg">
      <div class="tag"><span>…think wine <em>new</em></span><span>…discuss <em>viral</em></span><span>…experience the <em>taste</em></span></div>
      <h2>Komm mit uns auf eine <em>spannende Weinreise.</em></h2>
      <p class="lead">Lerne jedes Jahr mindestens zwölf neue Kreationen kennen, investiere in Trouvaillen und geniesse die Freundschaft am verrückten Tisch.</p>
    </div>
    <div class="c10-3 stack stack-sm">
      <a class="btn btn-light" href="/mitglied-werden">Mitglied werden</a>
      <span class="small" style="text-align:center">CHF 350 pro Jahr · auf Empfehlung</span>
    </div>
  </div>
</section>
''' + FOOTER

def card(anchor, meta, title, text, img, alt, fotos=None, key=None):
    album = ALB.get(key, 'https://www.flickr.com/photos/197768276@N04/albums')
    links = f'<a href="#{anchor}">Bericht →</a>' + (f'<a href="{album}" target="_blank" rel="noopener">{fotos} Fotos</a>' if fotos else '')
    return f'<article class="card">{ph("", img=IMG[key], alt=alt) if key else ph("Foto")}<span class="meta">{meta}</span><h3>{title}</h3><p>{text}</p><div class="links">{links}</div></article>'

ANLAESSE = head('Anlässe – crazytable', 'Degustationsabende und Reisen des Weinclubs crazytable: kommende Termine, Berichte und Fotos.', 'anlaesse') + f'''
<div class="wrap" style="padding:0">
<section class="section grid-12" style="padding-top:72px;padding-bottom:48px;align-items:end;border-bottom:0">
  <div class="c1-8 stack">
    <p class="overline">Anlässe</p>
    <h1 style="font-size:clamp(44px,6vw,80px)">Zwei Abende im Jahr. Und manchmal eine Reise.</h1>
    <p class="lead" style="max-width:640px">Jeder Anlass hat ein Thema – eine Region, ein Weingut, eine Traube. Hier findest du, was als Nächstes kommt, und die Berichte und Fotos der vergangenen Abende.</p>
  </div>
  <div class="c10-3" style="display:flex;justify-content:flex-end"><a class="btn btn-ghost" href="/termine.ics">Termine abonnieren</a></div>
</section>
{NEXT_EVENT}
<section class="section grid-12" style="align-items:start;padding-top:48px">
  <div class="c1-3 stack-sm stack">
    <p class="overline">Danach</p>
    <span style="font-family:var(--serif);font-size:72px;line-height:1">30.</span>
    <span style="font-size:15px;color:var(--text)">Oktober 2027 — Samstag, 11–18 Uhr</span>
    <span style="font-size:15px;color:var(--muted)">Kargo68, Zuchwil / Solothurn</span>
  </div>
  <div class="c4-6 stack">
    <h2 style="font-size:44px">Besenwirtschaft – ein Tag Württemberg</h2>
    <p class="lead" style="font-size:17px">Ein Tag wie in einer schwäbischen Besenwirtschaft: zwölf süddeutsche Weine, dazu passende Küche und viel Zeit am langen Tisch.</p>
    <span class="small">Für Mitglieder · Details folgen</span>
  </div>
  <div class="c10-3 stack stack-sm" style="padding-top:6px">
    <a class="btn btn-dark" href="#besenwirtschaft">Mehr Informationen</a>
    <a class="btn btn-ghost" href="/termine.ics">In Kalender</a>
  </div>
</section>

<section class="section stack" style="gap:48px" id="geplant">
  <div class="stack" style="gap:12px"><p class="overline">Die Idee dahinter</p><h2>Was wir für 2027 planen</h2><p class="lead">Stand November 2026 – Details, Preise und Anmeldung folgen jeweils einige Wochen vor dem Anlass.</p></div>

  <article class="grid-12 prose-block" id="doce-copas" style="row-gap:20px">
    <div class="c1-4 stack" style="gap:8px">
      <span class="meta">26. Mai 2027 — 18.30–23 Uhr</span>
      <h3 style="font-size:34px">Doce Copas</h3>
      <span class="small">Kargo68, Zuchwil / Solothurn · mit Vinos de España</span>
    </div>
    <div class="c6-7 prose" style="font-size:16px">
      <p>Zwölf Gläser, zwölf spanische Weine – vom Schaumwein über Weissweine bis zu kellerfähigen Roten aus verschiedenen Regionen. Die Auswahl treffen wir zusammen mit Vinos de España aus der Region Solothurn, die uns die Weine und die Geschichten dazu mitbringen.</p>
      <p>Die Küche steht im Zentrum: Zu jedem Glas gibt es eine kleine, passende kulinarische Begleitung, serviert am langen Tisch im Kargo68. Kein Quiz, keine Hektik – Wein für Wein, mit Zeit zum Vergleichen und Fachsimpeln.</p>
      <p>Offen ist noch, welche Regionen den Schwerpunkt bilden und ob ein Wein des Abends als Kandidat für den Clubkeller ins Rennen geht. Vorschläge gern über die Ideenbox.</p>
    </div>
  </article>

  <article class="grid-12 prose-block" id="besenwirtschaft" style="row-gap:20px;padding-top:40px;border-top:1px solid var(--line)">
    <div class="c1-4 stack" style="gap:8px">
      <span class="meta">30. Oktober 2027 — 11–18 Uhr</span>
      <h3 style="font-size:34px">Besenwirtschaft</h3>
      <span class="small">Kargo68, Zuchwil / Solothurn · Tagesanlass</span>
    </div>
    <div class="c6-7 prose" style="font-size:16px">
      <p>In Württemberg öffnen Winzerfamilien ein paar Wochen im Jahr ihre Stube, hängen einen Besen vor die Tür und schenken den eigenen Wein aus – dazu einfache, gute Küche. Diese Stimmung holen wir für einen Samstag ins Kargo68.</p>
      <p>Geplant sind zwölf süddeutsche Weine als Basis – Trollinger, Lemberger, Riesling und was die Region sonst hergibt – in lockerer Folge über den Nachmittag, mit Besenwirtschaft-Küche auf dem Tisch: Maultaschen, Schmalzbrot, Wurstsalat, Zwiebelkuchen. Kommen und gehen nach Lust, lange Tische, kein festes Programm.</p>
      <p>Die Weinauswahl ist noch offen und entsteht im Lauf des Jahres 2027.</p>
    </div>
  </article>
</section>

<section class="section grid-12 intermezzo-band" id="intermezzo" style="align-items:center">
  <div class="c1-5">
    <img src="/img/intermezzo-dark.svg" alt="Intermezzo – eine Flasche, ein Mittwoch, Atika Zuchwil" style="width:100%;max-width:420px;display:block">
  </div>
  <div class="c6-7 stack" style="gap:16px">
    <p class="overline" style="color:var(--cyan)">Neues Format</p>
    <h2 style="color:#fff">Intermezzo – das Zwischenspiel.</h2>
    <p class="lead">Zwischen den grossen Anlässen gibt es jetzt die kleine Form: eine einzelne, spannende Flasche, die man nicht jeden Tag öffnet – spontan, an einem Mittwochabend im Atika in Zuchwil. Die Einladung kommt kurzfristig, die Plätze sind begrenzt, wer zuerst zusagt, ist dabei.</p>
    <ul class="facts-inline">
      <li><b style="color:#fff">Wann</b> Ein Mittwoch, ab 18.30 Uhr – angekündigt wenige Tage vorher</li>
      <li><b style="color:#fff">Wo</b> Atika, Zuchwil</li>
      <li><b style="color:#fff">Was</b> Eine Flasche, eine Geschichte, ein Glas pro Person – manchmal mit einer Überraschung dazu</li>
      <li><b style="color:#fff">Preis</b> Immer separat, pro Abend – nicht im Mitgliederbeitrag enthalten</li>
    </ul>
    <p class="small">Einladung und Anmeldung laufen über den Mitgliederbereich.</p>
  </div>
</section>

<section class="section stack" style="gap:40px">
  <div class="between reveal">
    <h2>Rückblick</h2>
    <div class="chips"><span class="chip is-active">Alle</span><span class="chip">Degustationsabende</span><span class="chip">Reisen</span><span class="chip">Hauptversammlungen</span></div>
  </div>
  <article class="feature" id="wild-2026-card">
    {ph('', img=IMG['wild'], alt='Wild on Tour, Solothurn')}
    <div class="body">
      <span class="meta">17. Oktober 2026 — Degustationstag</span>
      <h3 style="font-size:40px">Wild on Tour – vier Stationen durch Solothurn</h3>
      <p style="color:var(--text)">Eine wandernde Wild-Degustation zu Fuss: Terrasse im Fleur de Soleure, Wurst und Brot überm Feuer im RiverYard, eine elegante Wildkreation im Atika und zum Schluss das Wildbuffet mit Käse vom Bucheggberg im Kargo68 – bei jeder Witterung.</p>
      <div class="links" style="display:flex;gap:18px;font-size:13px;letter-spacing:.04em"><a href="#wild-2026">Bericht lesen →</a><a href="{ALB['wild']}" target="_blank" rel="noopener">9 Fotos</a></div>
    </div>
  </article>
  <div class="cards">
    {card('toskana-2026','8. Mai 2026 — Degustationsabend','Toskana – vier Weingüter im Glas','Arillo in Terrabianca, Agricole Selvi, Castello di Bolgheri und Tenuta Pietranera – Chianti, Bolgheri und Maremma an einem Abend.',None,'Degustationsabend Toskana',17,'toskana')}
    {card('wallis-2025','25. Oktober 2025 — Degustationsreise','Premiere: Ins Wallis und nach Gruyères','Mit dem Car zur Cave du Rhodan in Salgesch, dann ins Chalet de Gruyère zu Raclette, Fondue und Tischgrill.',None,'Degustationsreise Wallis',22,'wallis')}
    {card('spanien-2025','23. Mai 2025 — Degustationsabend','Mit dem Al Andalus durch Spanien','Apéro im 1881-Waggon, Paella und die «Totenköpfe» – kraftvoll, magisch, intensiv in der Frucht.',None,'Degustationsabend Spanien',57,'spanien')}
    {card('suedamerika-2024','2. November 2024 — Degustationsabend','Südamerika: Mexiko und Argentinien','Chenin Blanc und Chardonnay aus Baja California, drei Rote von L.A. Cetto, dann Holzkohle und ein Malbec-Duell aus über 1000 m Höhe.',None,'Degustationsabend Südamerika',14,'suedamerika')}
    {card('alpen-2024','25. Mai 2024 — Hauptversammlung & Degustation','Bündnerland, Südtirol, Carnuntum','Drei Weingüter der Cave Amann im Wettstreit, Schöpsernes im Hauptgang – und zuvor die Jahresrechnung 2023.',None,'',None,None)}
    {card('portugal-2023','7. Oktober 2023 — Degustationsabend','In Gedanken nach Portugal','Mit Remo Aragão von Casa Lusitania: Vinho Verde, Alentejo, Eintopf im Stübli, Pastéis de Nata und ein gekühlter Port.',None,'Degustationsabend Portugal',28,'portugal')}
    {card('bordeaux-2023','6. Mai 2023 — Gründungsversammlung & Degustation','Bordeaux: Château Lestrille','Unsere erste Reise – mit Weinbauingenieurin Estelle Roumage, fünfte Generation, 15 km von Saint-Émilion.',None,'Degustationsabend Bordeaux',21,'bordeaux')}
    <article class="card card-dashed">
      <p class="overline">Deine Idee</p>
      <h3>Wohin soll die nächste Reise gehen?</h3>
      <p>Region, Winzer, Traube – schick uns deinen Vorschlag für einen kommenden Anlass.</p>
      <a class="arrow" href="/verein#ideenbox" style="color:var(--ink)">Zur Ideenbox →</a>
    </article>
  </div>
</section>

<section class="section" style="border-bottom:0">
  <p class="overline" style="margin-bottom:8px">Berichte</p>

  <article class="report prose" id="wild-2026">
    <div class="head"><span class="meta">17. Oktober 2026 — Degustationstag</span><h2 style="margin:0">Wild on Tour – vier Stationen durch Solothurn</h2></div>
    <p>Um 13 Uhr trafen wir uns am Bahnhof Solothurn – zehn Minuten zu Fuss, dann stand die erste Station: die Terrasse des Fleur de Soleure, leicht, weiblich, pflanzlich gedacht, mit den ersten Gläsern zum Einstimmen. Weiter ging es ans Wasser ins RiverYard, wo Wurst und Brot überm Feuer auf kraftvolle Rote trafen.</p>
    <p>Im Atika wurde es elegant: eine feine Wildkreation, dazu leichtere Rotweine und die Zigarrenterrasse für die, die wollten. Den Abschluss machte das Kargo68 mit einem Wildbuffet und Käse vom Bucheggberg. Vier Häuser, ein Thema, ein Nachmittag zu Fuss – und das Wetter spielte keine Rolle, weil es von Anfang an keine spielen durfte.</p>
  </article>

  <article class="report prose" id="toskana-2026">
    <div class="head"><span class="meta">8. Mai 2026 — Degustationsabend</span><h2 style="margin:0">Toskana – vier Weingüter im Glas</h2></div>
    <p>Vier Toskaner an einem Abend: Arillo in Terrabianca aus dem Chianti Classico, Agricole Selvi, Castello di Bolgheri von der Küste und Tenuta Pietranera. Degustiert wurde mit Degustationsblättern und Bestellformular – wer wollte, nahm seine Favoriten anschliessend mit nach Hause.</p>
    <p>[Hier zwei, drei Sätze zum Menü und zu den Höhepunkten des Abends ergänzen.]</p>
  </article>

  <article class="report prose" id="wallis-2025">
    <div class="head"><span class="meta">25. Oktober 2025 — Degustationsreise</span><h2 style="margin:0">Premiere: Ins Wallis und nach Gruyères</h2></div>
    <p>Am Mittag startete unser Weinclub zu seiner allerersten gemeinsamen Reise – ein Ereignis, auf das wir uns schon lange gefreut hatten. Mit dem Car machten wir uns auf den Weg ins Wallis. Der Himmel war grau, und strömender Regen begleitete uns von Anfang an – und sollte uns auch den ganzen Tag über nicht mehr verlassen. Doch unsere Vorfreude war ungetrübt.</p>
    <h3>Ankunft in Salgesch – Besuch bei Cave du Rhodan</h3>
    <p>Unser erstes Ziel war die renommierte Cave du Rhodan in Salgesch, wo wir herzlich von Corinne und Roger empfangen wurden. Zur Begrüssung gab es ein Glas Fendant, den typischen Walliser Weisswein – ein perfekter Auftakt. Trotz des Regens liessen wir es uns nicht nehmen, einen kurzen Spaziergang zu den Merlot-Reben direkt hinter dem Weingut zu unternehmen. Dort entdeckten wir eine kleine Herde Schafe, die friedlich zwischen den Rebzeilen grasten.</p>
    <h3>Ein Blick hinter die Kulissen</h3>
    <p>Zurück im Weingut erhielten wir eine spannende Kellerführung. Unter dem Gebäude verbirgt sich ein beeindruckendes Netzwerk aus Gärkellern, Barriquekellern und Lagerräumen. Roger erklärte uns mit viel Leidenschaft die einzelnen Produktionsschritte – von der Traube über die Gärung bis zur Abfüllung.</p>
    <h3>Degustation mit Charakter</h3>
    <p>Im Anschluss folgte das Herzstück unseres Besuchs: eine ausführliche Degustation der Weine aus dem Hause Rhodan. Wir probierten uns durch ein breites Spektrum – von frischen Weissweinen über elegante Rotweine bis hin zu charaktervollen Spezialitäten. Es wurde angeregt diskutiert, verglichen, gelobt – und viel gelacht. Einige von uns deckten sich mit ein paar edlen Tropfen für zu Hause ein.</p>
    <h3>Weiterfahrt nach Gruyères – Käse trifft Wein</h3>
    <p>Am Nachmittag führte uns die Reise weiter nach Gruyères, wo uns im Chalet de Gruyère bereits Lise erwartete. Ein langer, gedeckter Tisch stand bereit – mit Wein, Raclette, Fondue und Tischgrill in Hülle und Fülle. In gemütlicher Atmosphäre genossen wir die Köstlichkeiten der Region, und am Abend brachte uns Hans-Ueli, unser zuverlässiger Chauffeur, sicher zurück nach Kirchberg. Im Gepäck: köstlicher Wein, schöne Erinnerungen und die Vorfreude auf den nächsten Ausflug.</p>
    <p><em>Cave du Rhodan – Mounir Weine wird in dritter Generation von der Familie Mounir geführt und ist für nachhaltige, biodynamische Landwirtschaft und charaktervolle Walliser Weine bekannt.</em></p>
  </article>

  <article class="report prose" id="spanien-2025">
    <div class="head"><span class="meta">23. Mai 2025 — Degustationsabend</span><h2 style="margin:0">Mit dem Al Andalus durch Spanien</h2></div>
    <p>Jeder Wein ist eine einzigartige Mischung, wie sein visueller Ausdruck: Totenköpfe in all ihren Facetten von Farbe und Textur. Kraftvoll, magisch, strukturiert, geschmeidig, intensiv in der Frucht, mit geheimnisvollen Noten, die eine köstliche Komplexität offenbaren. Wir starteten mit einem kleinen Apéro im 1881-Waggon, fuhren mit dem Zug Al Andalus durch Spanien – und genossen anschliessend eine herrliche Paella und die verschiedenen Totenköpfe.</p>
  </article>

  <article class="report prose" id="suedamerika-2024">
    <div class="head"><span class="meta">2. November 2024 — Degustationsabend</span><h2 style="margin:0">Südamerika: Mexiko und Argentinien</h2></div>
    <p>Der Abend stand im Zeichen Südamerikas. Wir starteten mit zwei Weissweinen aus Mexiko – einem Chenin Blanc und einem klassischen Chardonnay aus dem Guadalupe-Tal in Baja California – und blieben mit drei Rotweinen aus dem Hause Vinícola L.A. Cetto im Land, inspiriert von Piemont, Toskana und Bordeaux.</p>
    <p>Danach wurde mit Holzkohle eingefeuert: Fleisch, Fisch und Beilagen vom Grill, dazu drei Rotweine aus Argentinien. Im Duell: zwei Malbecs, beide auf über 1000 Metern angebaut, und ein Blend.</p>
  </article>

  <article class="report prose" id="alpen-2024">
    <div class="head"><span class="meta">25. Mai 2024 — Hauptversammlung &amp; Degustation</span><h2 style="margin:0">Bündnerland, Südtirol, Carnuntum</h2></div>
    <p>Der Abend begann mit der Hauptversammlung und der statutarischen Agenda, im Fokus die Jahresrechnung 2023. Anschliessend war die Cave Amann SA zu Besuch – Generalimporteur mit 14 eigenen Weingütern in der Schweiz, Italien und Frankreich. Drei Weissweine und vier Rotweine aus drei Weingütern standen im Wettstreit: Komminoth Weine (Maienfeld, Graubünden), Kellerei Meran (Marling, Südtirol) und Weingut Böheim (Arbesthal, Carnuntum).</p>
    <p>Kulinarisch liessen wir uns von Bündner Spezialitäten inspirieren; im Hauptgang gab es Südtiroler Schöpsernes, zum Dessert eine süsse Spezialität.</p>
  </article>

  <article class="report prose" id="portugal-2023">
    <div class="head"><span class="meta">7. Oktober 2023 — Degustationsabend</span><h2 style="margin:0">In Gedanken nach Portugal</h2></div>
    <p>An unserem zweiten Degustationsabend reisten wir in Gedanken nach Portugal – begleitet von Remo Aragão von <a href="https://casalusitania.ch/" target="_blank" rel="noopener">Casa Lusitania</a>. Nach einem erfrischenden «Port Hibiscus Twist» folgten zwei Weissweine aus Vinho Verde und Alentejo und zwei Rotweine, dazu portugiesische Häppchen an der Weinbar, wo Remo Geschichten zu Regionen, Trauben und Weinen erzählte.</p>
    <p>Später wechselten wir im terroir vom Bistro ins Stübli zu einem traditionellen Eintopf und den zwei letzten Rotweinen. Den süssen Abschluss machten Pastéis de Nata und ein gekühlter Portwein – und am Ende öffneten wir unsere Favoriten und liessen den Abend beim Fachsimpeln ausklingen.</p>
  </article>

  <article class="report prose" id="bordeaux-2023">
    <div class="head"><span class="meta">6. Mai 2023 — Gründungsversammlung &amp; Degustation</span><h2 style="margin:0">Bordeaux: Château Lestrille</h2></div>
    <p>Unsere erste Reise führte nach Bordeaux – zu Estelle Roumage, diplomierte Weinbauingenieurin und fünfte Generation auf Château Lestrille, das sie mit ihrem Mann Jean-Louis in Saint-Germain-du-Puch führt, 15 Kilometer von Saint-Émilion. 40 Hektar Reben, zwei Drittel davon Merlot, ein Drittel Weissweine – vor allem Sauvignon Blanc mit etwas Sémillon und Muscadelle.</p>
    <p>Das Weingut sammelte in den letzten Jahren internationale Auszeichnungen: «World's Best Merlot» für den Le Secret de Lestrille 2010, «Coup de Cœur» im Guide Hachette für den Lestrille Capmartin Blanc 2013, «Best French Rosé» in New York für den Rosé 2015.</p>
  </article>
</section>
</div>
''' + FOOTER


# ---------- Wertentwicklung Weinkeller ----------
# Einstand = bezahlter Preis pro Einheit; markt = Richtwert Schweizer Händlerpreis inkl. MwSt (Stand Nov 2026). None = noch offen.
WERT = [
    dict(name='Château Pontet-Canet 2023', sub='Pauillac · Investment I', n=18, unit='Fl.', einstand=75.0, markt=84.0, quelle='Händler CH, Nov 2026'),
    dict(name='Château Giscours 2020, Impériale', sub='Margaux · 6 Liter', n=1, unit='Impériale', einstand=538.50, markt=580.0, quelle='Schätzung aus 75-cl-Preis + Formatzuschlag'),
    dict(name='Plansel Selecta Grande Escolha 2019', sub='Alentejo · Investment II', n=24, unit='Fl.', einstand=76.50, markt=79.0, quelle='Richtwert Händler CH'),
    dict(name='Rosso del Bepi 2016, Quintarelli', sub='Veneto · Investment III', n=12, unit='Fl.', einstand=155.0, markt=149.0, quelle='Händler CH, Nov 2026'),
]
def chf(x): return "CHF " + f"{x:,.0f}".replace(',', "'")
def wert_section():
    # Gruppierte Balken: Einstand (schwarz) vs. Marktwert (cyan) je Wein, Totalwerte
    W, H = 920, 420
    padL, padR, padT, padB = 64, 16, 28, 86
    plotW, plotH = W - padL - padR, H - padT - padB
    vals = [w['n'] * max(w['einstand'] or 0, w['markt']) for w in WERT]
    ymax = max(vals) * 1.18
    step = 500
    gw = plotW / len(WERT)
    bw = min(72, gw * 0.28)
    gap = 6
    def y(v): return padT + plotH - v / ymax * plotH
    def fmt(v): return f"{v:,.0f}".replace(',', "'")
    svg = []
    # Gitter
    v = 0
    while v <= ymax:
        yy = y(v)
        svg.append(f'<line x1="{padL}" x2="{W - padR}" y1="{yy:.1f}" y2="{yy:.1f}" class="grid"/><text x="{padL - 10}" y="{yy + 4:.1f}" class="ax" text-anchor="end">{fmt(v) if v else 0}</text>')
        v += step
    svg.append(f'<line x1="{padL}" x2="{W - padR}" y1="{y(0):.1f}" y2="{y(0):.1f}" class="base"/>')
    tot_e = tot_m = 0.0
    for i, w in enumerate(WERT):
        cx = padL + gw * (i + .5)
        e_tot = w['n'] * w['einstand'] if w['einstand'] else None
        m_tot = w['n'] * w['markt']
        if e_tot: tot_e += e_tot; tot_m += m_tot
        xe, xm = cx - bw - gap / 2, cx + gap / 2
        if e_tot:
            svg.append(f'<g class="bar-g" style="--d:{i * .12:.2f}s"><title>{w["name"]} – Einstand {w["n"]} × CHF {w["einstand"]:.2f} = CHF {fmt(e_tot)}</title>'
                       f'<rect x="{xe:.1f}" y="{y(e_tot):.1f}" width="{bw:.1f}" height="{plotH - (y(e_tot) - padT):.1f}" class="b-e"/>'
                       f'<text x="{xe + bw / 2:.1f}" y="{y(e_tot) - 8:.1f}" class="val" text-anchor="middle">{fmt(e_tot)}</text></g>')
        else:
            svg.append(f'<g class="bar-g" style="--d:{i * .12:.2f}s"><title>{w["name"]} – Einstandspreis folgt</title>'
                       f'<rect x="{xe:.1f}" y="{y(m_tot * .55):.1f}" width="{bw:.1f}" height="{plotH - (y(m_tot * .55) - padT):.1f}" class="b-na"/>'
                       f'<text x="{xe + bw / 2:.1f}" y="{y(m_tot * .55) - 8:.1f}" class="val muted" text-anchor="middle">?</text></g>')
        svg.append(f'<g class="bar-g" style="--d:{i * .12 + .06:.2f}s"><title>{w["name"]} – Marktwert ca. {w["n"]} × CHF {w["markt"]:.0f} = CHF {fmt(m_tot)} ({w["quelle"]})</title>'
                   f'<rect x="{xm:.1f}" y="{y(m_tot):.1f}" width="{bw:.1f}" height="{plotH - (y(m_tot) - padT):.1f}" class="b-m"/>'
                   f'<text x="{xm + bw / 2:.1f}" y="{y(m_tot) - 8:.1f}" class="val" text-anchor="middle">{fmt(m_tot)}</text></g>')
        # Beschriftung
        name = w['name'].split(',')[0].replace('Château ', '').replace('Selecta Grande Escolha', 'Selecta GE')
        svg.append(f'<text x="{cx:.1f}" y="{H - padB + 26}" class="lbl" text-anchor="middle">{name}</text>'
                   f'<text x="{cx:.1f}" y="{H - padB + 44}" class="ax" text-anchor="middle">{w["sub"].split(" · ")[0]} · {w["n"]} {w["unit"]}</text>')
        if e_tot:
            d = (w['markt'] - w['einstand']) / w['einstand'] * 100
            svg.append(f'<text x="{cx:.1f}" y="{H - padB + 70}" class="dl {"up" if d >= 0 else "down"}" text-anchor="middle">{"+" if d >= 0 else "−"}{abs(d):.0f} %</text>')
        else:
            svg.append(f'<text x="{cx:.1f}" y="{H - padB + 70}" class="dl na" text-anchor="middle">Einstand folgt</text>')
    # Mobile: horizontale Balken als HTML
    mx = max(vals)
    mrows = ''
    for w in WERT:
        e_tot = w['n'] * w['einstand'] if w['einstand'] else None
        m_tot = w['n'] * w['markt']
        d = ((w['markt'] - w['einstand']) / w['einstand'] * 100) if w['einstand'] else None
        dl = (f'<span class="dl {"up" if d >= 0 else "down"}">{"+" if d >= 0 else "−"}{abs(d):.0f} %</span>' if d is not None else '<span class="dl na">Einstand folgt</span>')
        be = (f'<div class="hb"><i class="b-e" style="width:{e_tot / mx * 80:.1f}%"></i><span>{fmt(e_tot)}</span></div>' if e_tot else
              f'<div class="hb"><i class="b-na" style="width:{m_tot * .55 / mx * 100:.1f}%"></i><span class="muted">?</span></div>')
        mrows += f"""
      <div class="mrow"><div class="between" style="align-items:baseline"><h3>{w['name'].split(',')[0].replace('Château ', '').replace('Selecta Grande Escolha', 'Selecta GE')}</h3>{dl}</div><span class="small">{w['sub']} · {w['n']} {w['unit']}</span>
        {be}<div class="hb"><i class="b-m" style="width:{m_tot / mx * 80:.1f}%"></i><span>{fmt(m_tot)}</span></div></div>"""
    tot_d = (tot_m - tot_e) / tot_e * 100
    chart = '\n'.join(svg)
    return f"""
<section class="section stack" style="gap:32px" id="wertentwicklung">
  <div class="stack reveal" style="gap:12px"><p class="overline">Wertentwicklung</p><h2>Was der Keller heute wert ist.</h2>
    <p class="lead">Wir kaufen zum Trinken, nicht zum Spekulieren – schauen aber trotzdem hin. Marktwerte sind Richtwerte aus aktuellen Schweizer Händlerpreisen (inkl. MwSt), kein Verkaufsangebot.</p></div>
  <div class="wert-total reveal">
    <div><span class="k">{chf(tot_e)}</span><span class="v">Einstand bezahlt</span></div>
    <div><span class="k">ca. {chf(tot_m)}</span><span class="v">Marktwert heute</span></div>
    <div><span class="k {"up" if tot_d >= 0 else "down"}">{"+" if tot_d >= 0 else "−"}{abs(tot_d):.0f} %</span><span class="v">Entwicklung seit Kauf</span></div>
  </div>
  <figure class="wert-chart reveal">
    <div class="legend"><span><i class="sw sw-e"></i>Einstand total</span><span><i class="sw sw-m"></i>Marktwert heute (ca.)</span><span class="small" style="margin-left:auto">CHF · Stand Nov. 2026</span></div>
    <svg viewBox="0 0 {W} {H}" role="img" aria-label="Balkendiagramm: Einstand und heutiger Marktwert je Wein im Clubkeller">
      <defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" stroke="#C9CAC8" stroke-width="2"/></pattern></defs>
      {chart}
    </svg>
    <div class="wert-mobile">{mrows}
    </div>
    <figcaption class="small">Werte je Position: Einstand × Anzahl Flaschen bzw. aktueller Händlerpreis × Anzahl. Wird jährlich zur Hauptversammlung aktualisiert.</figcaption>
  </figure>
</section>
"""

WEINKELLER = head('Weinkeller – crazytable', 'Der gemeinsame Weinkeller des Weinclubs crazytable: Kellerregel, Bestand, Reifeplan und die Abstimmungen der Hauptversammlung.', 'weinkeller') + f"""
<section class="band-green cellar-hero" style="background:linear-gradient(90deg,rgba(11,11,11,.92) 0%,rgba(11,11,11,.75) 50%,rgba(11,11,11,.45) 100%),url(/img/keller-bg.jpg) center/cover no-repeat">
  <div class="wrap grid-12" style="padding:0;align-items:end">
    <div class="c1-8 stack stack-lg">
      <p class="overline">Weinkeller</p>
      <h1 style="font-size:clamp(56px,9vw,120px)">Unsere <em>Trouvaillen.</em></h1>
      <p class="lead" style="max-width:560px">Einmal im Jahr kaufen wir gemeinsam Wein, den wir nicht heute trinken. Er liegt im Keller, wir schauen ihm beim Reifen zu – und irgendwann öffnen wir ihn zusammen.</p>
    </div>
    <div class="c10-3 cellar-rule">
      <span class="k">1</span><span class="v">Einkauf pro Jahr</span>
      <span class="k">ca. 20 %</span><span class="v">der Mitgliederbeiträge</span>
      <span class="k">1 Stimme</span><span class="v">pro anwesendes Mitglied, einfaches Mehr</span>
    </div>
  </div>
</section>

<div class="wrap" style="padding:0">

<section class="section stack" style="gap:40px">
  <div class="between reveal"><h2>Im Keller</h2><span class="small">Stand: Hauptversammlung [Mai 2026] — wird jährlich aktualisiert</span></div>
  <div class="bottles">
    <article class="bottle">
      <div class="bottle-img">{ph('', img='/img/pontet-canet.jpg', alt='Château Pontet-Canet, Pauillac')}<span class="status status-ok">In Subskription · 18 Flaschen · Lieferung 2026</span></div>
      <div class="bottle-body">
        <span class="meta">Investment I — HV 2023</span>
        <h3>Château Pontet-Canet 2023</h3>
        <span class="small">Pauillac, Bordeaux · 5ème Grand Cru Classé · biodynamisch</span>
        <p>Im Gründungsjahr en primeur gekauft. 2026 kommt die Lieferung – dann entscheiden wir: ein paar Flaschen öffnen oder alles weiter liegen lassen.</p>
        <dl class="facts"><dt>Flaschen</dt><dd>18 × 75 cl</dd><dt>Einstand</dt><dd>CHF 75 (CHF 1'350 total)</dd><dt>Trinkfenster</dt><dd>ab ca. [2033]</dd></dl>
        <details class="more"><summary>Mehr zum Weingut</summary><p>Pontet-Canet gehört seit 1975 der Familie Tesseron; Alfred Tesseron führt das Gut seit 1994. 81 Hektar in Pauillac, rund 62 % Cabernet Sauvignon und 32 % Merlot. Seit 2004 wird biodynamisch gearbeitet – als erstes grosses Bordeaux-Gut mit Bio-Zertifikat (2010) und seit Jahrgang 2014 Demeter. Ein Teil der Reben wird mit Pferden gepflügt, ein Teil des Weins reift in Amphoren aus dem eigenen Boden. Im Glas: ein Fünfter Cru, der regelmässig mit den Zweiten gemessen wird.</p></details>
      </div>
    </article>
    <article class="bottle">
      <div class="bottle-img">{ph('', img='/img/giscours.jpg', alt='Château Giscours, Margaux')}<span class="status status-ok">Im Keller · 1 Impériale</span></div>
      <div class="bottle-body">
        <span class="meta">Zukauf — Oktober 2023</span>
        <h3>Château Giscours 2020</h3>
        <span class="small">Margaux · 3ème Grand Cru Classé · 13,5 %</span>
        <p>Der Zweitplatzierte der ersten Abstimmung kam doch noch in den Keller – als Impériale mit sechs Litern in der Holzkiste. Eine Flasche für einen besonderen Abend.</p>
        <dl class="facts"><dt>Format</dt><dd>1 × 600 cl</dd><dt>Einstand</dt><dd>CHF 538.50</dd><dt>Trinkfenster</dt><dd>ab ca. [2030]</dd></dl>
        <details class="more"><summary>Mehr zum Weingut</summary><p>Giscours ist eines der ältesten Güter des Médoc – erstmals 1330 erwähnt, Wein seit 1552, Dritter Cru der Klassifikation von 1855. 102 Hektar in Margaux, rund 65 % Cabernet Sauvignon und 30 % Merlot, mit alten Reben, teils von 1926. Seit 1995 gehört es der niederländischen Familie Albada Jelgersma, die nach langem Rechtsstreit seit Ende 2023 Alleineigentümerin ist. Die Impériale mit sechs Litern reift langsamer als die Normalflasche – gut für einen Wein, der auf einen besonderen Abend wartet.</p></details>
      </div>
    </article>
    <article class="bottle">
      <div class="bottle-img">{ph('', img='/img/plansel.jpg', alt='Plansel Selecta Grande Escolha 2019')}<span class="status status-ok">Im Keller · 24 Flaschen</span></div>
      <div class="bottle-body">
        <span class="meta">Investment II — HV 2024</span>
        <h3>Plansel Selecta Grande Escolha 2019</h3>
        <span class="small">Quinta da Plansel · Alentejo · Touriga Nacional, Tinta Barroca, Touriga Franca</span>
        <p>Das Flaggschiff der Quinta da Plansel: handverlesene Trauben alter Reben, 24 Monate in neuen Barriques, 16 % – sehr dunkel, reife Wald- und Beerenfrüchte, tiefgründige Würze. Setzte sich 2024 gegen Brites Aguiar und Manoella Vinhas Velhas durch.</p>
        <dl class="facts"><dt>Flaschen</dt><dd>24 × 75 cl</dd><dt>Einstand</dt><dd>CHF 76.50 (CHF 1'836 total)</dd><dt>Trinkfenster</dt><dd>jetzt bis ca. 2035</dd></dl>
        <details class="more"><summary>Mehr zum Weingut</summary><p>Hinter der Quinta da Plansel in Montemor-o-Novo, rund 100 km östlich von Lissabon, steht eine deutsch-portugiesische Familiengeschichte: Jorge Böhm aus der Pfalz kam über ein Schiffsunglück vor der portugiesischen Küste zum Wein, kaufte 1975 die Quinta de São Jorge und erforschte die einheimischen Rebsorten. Seine Tochter Dorina Lindemann gründete 1997 das Weingut und setzte als eine der Ersten im Süden auf reinsortige Touriga Nacional. Rund 65 Hektar, vor allem Rotwein; der Grande Escolha ist das Flaggschiff aus den besten Parzellen alter Reben.</p></details>
      </div>
    </article>
    <article class="bottle">
      <div class="bottle-img">{ph('', img='/img/quintarelli.jpg', alt='Rosso del Bepi 2016, Giuseppe Quintarelli')}<span class="status status-ok">Im Keller · 12 Flaschen</span></div>
      <div class="bottle-body">
        <span class="meta">Investment III — HV 2025</span>
        <h3>Rosso del Bepi 2016</h3>
        <span class="small">Giuseppe Quintarelli · IGT Veneto · Corvina, Rondinella, Molinara</span>
        <p>Der «kleine Amarone» des legendären Quintarelli-Hauses in Negrar: Kompott, Gewürz, Tabak, schwarze Kirsche und Pfeffer, 15,5 % – ein Wein, der 15 bis 20 Jahre trägt.</p>
        <dl class="facts"><dt>Flaschen</dt><dd>12 × 75 cl</dd><dt>Einstand</dt><dd>CHF 155 (CHF 1'860 total)</dd><dt>Trinkfenster</dt><dd>jetzt bis ca. 2036</dd></dl>
        <details class="more"><summary>Mehr zum Weingut</summary><p>Giuseppe «Bepi» Quintarelli (1927–2012) machte das 1924 von seinem Vater gegründete Gut in Negrar zur Legende des Valpolicella: handgeschriebene Etiketten, Amarone mit mindestens sieben Jahren im grossen Holz, Riserva zehn – und in Jahren, die ihm nicht genügten, gab es schlicht keinen Amarone. Genau dann entsteht der Rosso del Bepi: dieselben getrockneten Trauben, dieselbe Zeit im Fass, nur ohne die Bezeichnung. Heute führen Tochter Fiorenza, ihr Mann Giampaolo Grigoli und die Enkel Francesco und Lorenzo das Haus.</p></details>
      </div>
    </article>
    <article class="bottle bottle-next">
      <div class="bottle-img"><div class="ph ratio-45" style="background:var(--black);align-items:center;justify-content:center"><span style="font-family:var(--serif);font-size:120px;color:var(--cyan);letter-spacing:0">?</span></div></div>
      <div class="bottle-body">
        <span class="meta">Investment IV — HV 26. Mai 2027</span>
        <h3>Spanien zur Wahl</h3>
        <p>Drei Kandidaten, drei Handschriften – entschieden wird an der Hauptversammlung im Mai 2027, am Abend von Doce Copas.</p>
        <a class="btn btn-primary" href="#wahl-2027" style="align-self:flex-start">Die Kandidaten</a>
      </div>
    </article>
  </div>
</section>

<section class="section stack" style="gap:32px">
  <div class="stack" style="gap:12px"><p class="overline">Reifeplan</p><h2>Wann öffnen wir was?</h2><p class="lead">Jede Linie ist ein Wein im Keller: von Kauf über Lieferung bis zum Trinkfenster. Jahreszahlen sind Schätzungen und werden an der HV überprüft.</p></div>
  <div class="timeline" role="img" aria-label="Zeitstrahl 2023 bis 2040 mit Kauf, Lieferung und Trinkfenster je Wein">
    <div class="tl-years"><span>2023</span><span>2026</span><span>2029</span><span>2032</span><span>2035</span><span>2038</span><span>2041</span></div>
    <div class="tl-row">
      <span class="tl-label">Pontet-Canet 2023</span>
      <div class="tl-track"><span class="tl-dot" style="left:0%" title="Kauf 2023"></span><span class="tl-dot" style="left:16.6%" title="Lieferung 2026"></span><span class="tl-wait" style="left:16.6%;width:38.9%"></span><span class="tl-bar" style="left:55.5%;width:44.5%">Trinkfenster ab ca. [2033]</span></div>
    </div>
    <div class="tl-row">
      <span class="tl-label">Giscours 2020 (6 l)</span>
      <div class="tl-track"><span class="tl-dot" style="left:0%" title="Kauf 2023"></span><span class="tl-wait" style="left:0%;width:38.9%"></span><span class="tl-bar" style="left:38.9%;width:44.4%">Trinkfenster ab ca. [2030]</span></div>
    </div>
    <div class="tl-row">
      <span class="tl-label">Plansel Selecta 2019</span>
      <div class="tl-track"><span class="tl-dot" style="left:5.5%" title="Kauf 2024"></span><span class="tl-bar" style="left:5.5%;width:61.1%">Trinkfenster bis 2035</span></div>
    </div>
    <div class="tl-row">
      <span class="tl-label">Rosso del Bepi 2016</span>
      <div class="tl-track"><span class="tl-dot" style="left:11.1%" title="Kauf 2025"></span><span class="tl-bar" style="left:11.1%;width:61.1%">Trinkfenster bis ca. 2036</span></div>
    </div>
    <div class="tl-row tl-ghost">
      <span class="tl-label">Investment IV (2027)</span>
      <div class="tl-track"><span class="tl-dot" style="left:22.2%" title="Entscheid Mai 2027"></span><span class="tl-wait" style="left:22.2%;width:77.8%"></span></div>
    </div>
    <div class="tl-legend"><span><i class="lg-dot"></i>Kauf / Lieferung</span><span><i class="lg-wait"></i>Reifen im Keller</span><span><i class="lg-bar"></i>Trinkfenster</span></div>
  </div>
</section>

<section class="section stack" style="gap:40px">
  <div class="stack" style="gap:12px" id="wahl-2027"><p class="overline">Nächste Abstimmung</p><h2>Zur Wahl im Mai 2027</h2><p class="lead">Drei spanische Lagerweine, alle mit 15 bis 20 Jahren Potenzial. Preise Stand November 2026, Schweizer Handel.</p></div>
  <div class="votes">
    <article class="vote">
      <div class="vote-head"><span class="meta">Ribera del Duero · ca. CHF 101</span><h3>Alión</h3></div>
      <p style="font-size:15px;color:var(--text)">100 % Tempranillo aus dem Haus Vega Sicilia – dichter und moderner als der Unico: wildes schwarzes Beerenobst, samtige, kräftige Tannine, sehr langer Abgang. Trinkbar bis 2043. Peñín 96, Parker 96, Suckling 95.</p>
      <p class="small">Der sichere Kauf: grosse Herkunft, verlässlich lagerfähig.</p>
    </article>
    <article class="vote">
      <div class="vote-head"><span class="meta">Priorat · ca. CHF 95–110</span><h3>Clos Mogador</h3></div>
      <p style="font-size:15px;color:var(--text)">René Barbiers Gründungswein des modernen Priorat von Schieferterrassen in Gratallops: 45 % Garnacha, 29 % Cariñena, 16 % Syrah, 10 % Cabernet. Dörrobst, Tabak, schwarze Olive, reife Tannine, dunkle Schokolade. Parker 99/100.</p>
      <p class="small">Der Charakterkopf – ein Wein, den man in zehn Jahren mit Stolz öffnet.</p>
    </article>
    <article class="vote">
      <div class="vote-head"><span class="meta">Ribera del Duero · ca. CHF 110</span><h3>Flor de Pingus</h3></div>
      <p style="font-size:15px;color:var(--text)">Peter Sisseks Zweitwein des Kult-Pingus, biodynamisch, Tinto Fino: harmonisch und elegant, seidige Tannine, kühl und fein eingebundenes Holz – mehr Burgund-Haltung als Bordeaux.</p>
      <p class="small">Das feine Gegenstück zu Alión: gleiche Region, andere Handschrift.</p>
    </article>
  </div>
  <p class="small">Eigene Vorschläge bis zur Hauptversammlung über die <a href="/verein#ideenbox" style="text-decoration:underline">Ideenbox</a>.</p>
</section>

<section class="section stack" style="gap:40px">
  <div class="stack" style="gap:12px"><p class="overline">Die Abstimmungen</p><h2>So haben wir entschieden</h2></div>
  <div class="votes">
    <article class="vote">
      <div class="vote-head"><span class="meta">Hauptversammlung — 6. Mai 2023</span><h3>Vier Kandidaten, ein Bordeaux</h3></div>
      <ol class="candidates">
        <li class="winner"><span class="n">1</span><span class="name">Château Pontet-Canet 2023</span><span class="tag">Gewählt · 18 Flaschen</span></li>
        <li><span class="n">2</span><span class="name">Château Giscours 2020</span><span class="tag">Später als Impériale gekauft</span></li>
        <li><span class="n">3</span><span class="name">Caiarossa 2019</span><span class="tag">Toskana</span></li>
        <li><span class="n">4</span><span class="name">Vivaltus 2016</span><span class="tag">Ribera del Duero</span></li>
      </ol>
    </article>
    <article class="vote">
      <div class="vote-head"><span class="meta">Hauptversammlung — 25. Mai 2024</span><h3>Drei Portugiesen zur Wahl</h3></div>
      <ol class="candidates">
        <li class="winner"><span class="n">1</span><span class="name">Plansel Selecta Grande Escolha</span><span class="tag">Gewählt · 24 Flaschen</span></li>
        <li><span class="n">2</span><span class="name">Manoella Vinhas Velhas</span><span class="tag">Douro</span></li>
        <li><span class="n">3</span><span class="name">Brites Aguiar DOC</span><span class="tag">Dão</span></li>
      </ol>
    </article>
    <article class="vote">
      <div class="vote-head"><span class="meta">Hauptversammlung — 23. Mai 2025</span><h3>Drei Venezianer, ein Quintarelli</h3></div>
      <ol class="candidates">
        <li class="winner"><span class="n">1</span><span class="name">Rosso del Bepi 2016, Giuseppe Quintarelli</span><span class="tag">Gewählt · 12 Flaschen</span></li>
        <li><span class="n">2</span><span class="name">Zenato Amarone della Valpolicella Classico DOCG</span><span class="tag">Valpolicella</span></li>
        <li><span class="n">3</span><span class="name">Decus Ripasso Valpolicella Classico Superiore DOC</span><span class="tag">Valpolicella</span></li>
      </ol>
    </article>
  </div>
</section>

<section class="section grid-12" style="border-bottom:0">
  <div class="c1-4 stack"><p class="overline">Ablauf</p><h2>So kommt ein Wein in den Keller</h2></div>
  <ol class="steps c6-7">
    <li><span class="n">1</span><strong>Vorschläge sammeln</strong><span class="t">Der Vorstand stellt drei bis vier Kandidaten mit Factsheet vor – gerne aus der Ideenbox.</span></li>
    <li><span class="n">2</span><strong>Degustieren und diskutieren</strong><span class="t">An der Hauptversammlung gibt es eine kleine Degustation, Preisentwicklung und Lagerpotenzial kommen auf den Tisch.</span></li>
    <li><span class="n">3</span><strong>Abstimmen</strong><span class="t">Einfaches Mehr der Anwesenden. Wer nicht da ist, gibt seine Präferenz vorab per Formular ab.</span></li>
    <li><span class="n">4</span><strong>Kaufen, lagern, später öffnen</strong><span class="t">Jedes Jahr schauen wir Inventar und Wert an und entscheiden, was verkauft, weiter gelagert oder gemeinsam degustiert wird.</span></li>
  </ol>
</section>
</div>
""" + FOOTER

def person(name, role, mail, img):
    pic = ph('', 'ratio-11', img=img, alt=name) if img.startswith('/') else ph(img, 'ratio-11')
    return f'<article class="person">{pic}<div class="stack-sm stack" style="gap:4px"><h3>{name}</h3><span class="role">{role}</span><a href="mailto:{mail}">{mail}</a></div></article>'

VEREIN = head('Verein & Vorstand – crazytable', 'Vorstand, Hauptversammlung und Ideenbox des Weinclubs crazytable in Kirchberg BE.', 'verein') + f'''
<div class="wrap" style="padding:0">
<section class="section stack" style="padding-top:72px;padding-bottom:56px;max-width:860px;border-bottom:0">
  <p class="overline">Verein</p>
  <h1 style="font-size:clamp(44px,6vw,80px)">Ein kleiner Verein mit einem grossen Tisch</h1>
  <p class="lead" style="max-width:none">Der Weinclub crazytable wurde am 1. März 2023 in Kirchberg BE gegründet. Wir sind bewusst klein: maximal 25 Mitglieder, damit an unseren Abenden alle am selben Tisch sitzen.</p>
</section>

<section class="section stack" style="gap:40px;padding-top:24px">
  <h2>Vorstand</h2>
  <div class="people people-board">
    {person('Stefan Moser','Präsident','stefan.moser@crazytable.ch','/img/stefan.jpg')}
    <p class="lead" style="max-width:none">Der Vorstand führt den Club mit leichter Hand: Jahresprogramm, Weinkeller, Hauptversammlung. Wer mitgestalten will – die Ideenbox ist offen.</p>
  </div>
  <div class="grid-12" style="padding-top:24px;border-top:1px solid var(--line)">
    <h3 class="c1-3" style="font-size:24px">Revisoren</h3>
    <div class="c4-6 revisoren">
      <div class="stack" style="gap:2px"><strong style="font-weight:500">Patrick Felder</strong><span class="small">Revisor</span></div>
      <div class="stack" style="gap:2px"><strong style="font-weight:500">Yves Schüpbach</strong><span class="small">Revisor</span></div>
    </div>
  </div>
</section>

<section class="section grid-12" id="hauptversammlung">
  <div class="c1-5 stack">
    <p class="overline">Hauptversammlung</p>
    <h2 style="font-size:40px">Einmal im Jahr: Rechnung, Programm – und der Kellerentscheid</h2>
    <p style="color:var(--text)">Die Hauptversammlung findet jeweils vor einem Degustationsabend statt. Wer am Abend nicht dabei sein kann, kann die Weine in den zehn Tagen danach mit 20 % Rabatt bestellen.</p>
    <div class="row"><a class="btn btn-ghost" href="/statuten.pdf">Statuten (PDF)</a></div>
  </div>
  <ol class="agenda c7-6">
    <li><span class="n">a</span>Wahl des Vorstandes und der Revisoren</li>
    <li><span class="n">b</span>Festsetzung und Änderung der Statuten</li>
    <li><span class="n">c</span>Abnahme der Jahresrechnung und des Revisorenberichts</li>
    <li><span class="n">d</span>Beschluss über das Jahresbudget</li>
    <li><span class="n">e</span>Inventar Weinkeller, Investitions- und Desinvestitionsentscheide</li>
    <li><span class="n">f</span>Beschluss über das Jahresprogramm</li>
    <li><span class="n">g</span>Festsetzung des Mitgliederbeitrags</li>
    <li><span class="n">h</span>Behandlung von Ausschlussrekursen</li>
  </ol>
</section>

<section class="section grid-12" id="ideenbox" style="border-bottom:0">
  <div class="c1-5 stack">
    <p class="overline">Ideenbox</p>
    <h2 style="font-size:40px">Welchen Abend würdest du gerne erleben?</h2>
    <p style="color:var(--text)">Eine Region, ein Weingut, ein Thema, eine Reise – schreib uns deine Idee. Der Vorstand nimmt sie in die Jahresplanung auf.</p>
  </div>
  <form class="form c7-6" name="ideenbox" method="POST" action="/danke" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="ideenbox">
    <p class="hidden"><label>Nicht ausfüllen: <input name="bot-field"></label></p>
    <div class="form-2">
      <div class="field"><label for="i-vn">Vorname</label><input id="i-vn" name="vorname" type="text" required></div>
      <div class="field"><label for="i-nn">Nachname</label><input id="i-nn" name="nachname" type="text" required></div>
    </div>
    <div class="field"><label for="i-em">E-Mail</label><input id="i-em" name="email" type="email" required></div>
    <div class="field"><label for="i-idee">Deine Idee</label><textarea id="i-idee" name="idee" rows="5" required></textarea></div>
    <button class="btn btn-primary" type="submit" style="align-self:flex-start">Idee abschicken</button>
  </form>
</section>
</div>
''' + FOOTER

MITGLIED = head('Mitglied werden – crazytable', 'Mitglied werden im Weinclub crazytable: CHF 350 pro Jahr, zwei Degustationen inklusive Menü, Anteil am Clubkeller. Aufnahme auf Empfehlung.', 'mitglied') + f'''
<div class="wrap" style="padding:0">
<section class="section grid-12" style="padding-top:72px;align-items:start">
  <div class="c1-5 stack stack-lg">
    <div class="stack">
      <p class="overline">Mitglied werden</p>
      <h1 style="font-size:clamp(44px,6vw,72px)">Nimm Platz am <em class="accent">verrückten Tisch.</em></h1>
      <p class="lead">Wir nehmen neue Mitglieder auf Empfehlung eines bestehenden Mitglieds auf – solange Platz am Tisch ist.</p>
    </div>
    <div class="terms">
      <div><span>Jahresbeitrag</span><b>CHF 350</b></div>
      <div><span>Degustationsabende inkl. Menü</span><strong>2 pro Jahr</strong></div>
      <div><span>Neue Weine im Glas</span><strong>mindestens 12</strong></div>
      <div><span>Anteil am Clubkeller</span><strong>20 % des Beitrags</strong></div>
      <div><span>Mitglieder</span><strong>max. 25</strong></div>
    </div>
    <p class="small" style="line-height:1.6">Noch Fragen, aber (noch) kein Mitglied? Schreib uns über das <a href="#kontakt" style="text-decoration:underline">Kontaktformular</a> oder direkt an <a href="mailto:stefan.moser@crazytable.ch" style="text-decoration:underline">stefan.moser@crazytable.ch</a>.</p>
  </div>
  <form class="form c7-6" name="anmeldung" method="POST" action="/danke" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="anmeldung">
    <p class="hidden"><label>Nicht ausfüllen: <input name="bot-field"></label></p>
    <h2 style="font-size:36px;margin-bottom:8px">Anmeldung</h2>
    <div class="form-2">
      <div class="field"><label for="a-vn">Vorname *</label><input id="a-vn" name="vorname" type="text" required></div>
      <div class="field"><label for="a-nn">Nachname *</label><input id="a-nn" name="nachname" type="text" required></div>
    </div>
    <div class="field"><label for="a-adr">Adresse *</label><input id="a-adr" name="adresse" type="text" required></div>
    <div class="form-2">
      <div class="field"><label for="a-plz">PLZ / Ort *</label><input id="a-plz" name="plz_ort" type="text" required></div>
      <div class="field"><label for="a-geb">Geburtsdatum *</label><input id="a-geb" name="geburtsdatum" type="date" required></div>
    </div>
    <div class="form-2">
      <div class="field"><label for="a-em">E-Mail *</label><input id="a-em" name="email" type="email" required></div>
      <div class="field"><label for="a-tel">Telefon *</label><input id="a-tel" name="telefon" type="tel" required></div>
    </div>
    <div class="field"><label for="a-emp">Auf Empfehlung von *</label><input id="a-emp" name="empfehlung" type="text" placeholder="Name des Mitglieds" required></div>
    <div class="field"><label for="a-msg">Bemerkung</label><textarea id="a-msg" name="bemerkung" rows="3"></textarea></div>
    <label class="check"><input type="checkbox" name="datenschutz" value="ja" required><span>Ich habe die <a href="/datenschutz">Datenschutzerklärung</a> gelesen und bin mit der Aufnahme in die Mitgliederliste einverstanden.</span></label>
    <button class="btn btn-primary" type="submit">Anmeldung abschicken</button>
    <span class="small" style="text-align:center">Der Vorstand meldet sich innert einer Woche.</span>
  </form>
</section>

<section class="section grid-12" id="kontakt" style="border-bottom:0">
  <div class="c1-5 stack">
    <p class="overline">Kontakt</p>
    <h2 style="font-size:40px">Eine Frage an den Verein?</h2>
    <p style="color:var(--text)">Für alles, was keine Anmeldung ist: Fragen zum Club, zu Anlässen oder zum Weinkeller.</p>
  </div>
  <form class="form c7-6" name="kontakt" method="POST" action="/danke" data-netlify="true" netlify-honeypot="bot-field">
    <input type="hidden" name="form-name" value="kontakt">
    <p class="hidden"><label>Nicht ausfüllen: <input name="bot-field"></label></p>
    <div class="form-2">
      <div class="field"><label for="k-vn">Vorname</label><input id="k-vn" name="vorname" type="text" required></div>
      <div class="field"><label for="k-nn">Nachname</label><input id="k-nn" name="nachname" type="text" required></div>
    </div>
    <div class="field"><label for="k-em">E-Mail</label><input id="k-em" name="email" type="email" required></div>
    <div class="field"><label for="k-msg">Nachricht</label><textarea id="k-msg" name="nachricht" rows="4" required></textarea></div>
    <button class="btn btn-outline" type="submit" style="align-self:flex-start">Nachricht senden</button>
  </form>
</section>
</div>
''' + FOOTER

def simple(title, desc, active, h1, body):
    return head(title, desc, active) + f'''
<div class="wrap" style="padding:0">
<section class="section stack" style="padding-top:72px;border-bottom:0;min-height:50vh">
  <h1 style="font-size:clamp(40px,5vw,64px)">{h1}</h1>
  <div class="prose">{body}</div>
</section>
</div>
''' + FOOTER

DANKE = simple('Danke – crazytable', 'Vielen Dank für deine Nachricht.', '', 'Danke, ist angekommen.',
    '<p>Deine Nachricht ist beim Vorstand eingetroffen. Wir melden uns innert einer Woche.</p><p><a class="link-u" href="/">Zur Startseite</a></p>')
DISCLAIMER = simple('Disclaimer – crazytable', 'Rechtliche Hinweise zur Website des Weinclubs crazytable.', '', 'Disclaimer',
    """<p><strong>Verantwortlich für diese Website</strong><br>Weinclub crazytable, Verein nach Art. 60 ff. ZGB, Kirchberg BE<br>Präsident: Stefan Moser · <a href="mailto:stefan.moser@crazytable.ch" style="text-decoration:underline">stefan.moser@crazytable.ch</a></p>
<h3>Inhalt</h3><p>Wir bemühen uns um richtige und aktuelle Informationen, übernehmen aber keine Gewähr für Richtigkeit, Vollständigkeit und Aktualität der Inhalte. Angaben zu Anlässen, Weinen, Preisen und Terminen können sich ändern; massgebend sind die Einladungen und Beschlüsse des Vereins. Haftungsansprüche wegen Schäden materieller oder immaterieller Art, die aus dem Zugriff auf diese Website oder der Nutzung der Inhalte entstehen, sind ausgeschlossen.</p>
<h3>Links</h3><p>Verweise auf Websites Dritter liegen ausserhalb unseres Verantwortungsbereichs. Wir haben keinen Einfluss auf deren Inhalte und lehnen jede Verantwortung dafür ab. Der Zugriff erfolgt auf eigene Verantwortung.</p>
<h3>Urheberrecht</h3><p>Texte, Bilder und Gestaltung dieser Website gehören dem Weinclub crazytable oder den genannten Rechteinhabern. Verwendung, auch auszugsweise, nur mit schriftlicher Zustimmung. Flaschenbilder und Logos von Weingütern dienen der Information über die Weine und bleiben Eigentum der jeweiligen Produzenten.</p>
<h3>Alkohol</h3><p>Unsere Anlässe richten sich an Erwachsene. Wein ist ein Genussmittel – wir trinken bewusst und in Massen und empfehlen, zu unseren Anlässen mit dem öffentlichen Verkehr anzureisen.</p>
<p class="small">Stand: November 2026</p>""")
DATENSCHUTZ = simple('Datenschutz – crazytable', 'Datenschutzerklärung des Weinclubs crazytable.', '', 'Datenschutz',
    """<p>Der Weinclub crazytable nimmt den Schutz deiner persönlichen Daten ernst. Diese Erklärung beschreibt, welche Daten wir auf crazytable.ch bearbeiten und wozu – nach dem Schweizer Datenschutzgesetz (DSG).</p>
<h3>Verantwortlich</h3><p>Weinclub crazytable, Kirchberg BE · Präsident Stefan Moser · <a href="mailto:stefan.moser@crazytable.ch" style="text-decoration:underline">stefan.moser@crazytable.ch</a></p>
<h3>Welche Daten wir bearbeiten</h3>
<p><strong>Formulare.</strong> Wenn du dich über die Website anmeldest, eine Frage stellst oder eine Idee einreichst, speichern wir die Angaben, die du im Formular machst (bei der Anmeldung: Name, Adresse, Geburtsdatum, E-Mail, Telefon, empfehlendes Mitglied; bei Kontakt und Ideenbox: Name, E-Mail, Nachricht). Wir verwenden sie ausschliesslich für den Vereinszweck: Aufnahme als Mitglied, Beantwortung deiner Anfrage, Planung der Anlässe. Die Formulare werden technisch durch Netlify (Netlify Inc., USA) verarbeitet und an den Vorstand per E-Mail übermittelt; Netlify speichert die Einsendungen für uns. Mitgliederdaten führen wir in der Mitgliederliste des Vereins, die nur dem Vorstand zugänglich ist.</p>
<p><strong>Server-Logdaten.</strong> Beim Aufruf der Website erfasst unser Hosting-Anbieter Netlify technisch bedingt Daten wie IP-Adresse, Datum und Uhrzeit, aufgerufene Seite und Browsertyp. Diese Daten dienen der Sicherheit und dem Betrieb der Website und werden nicht mit anderen Daten verknüpft.</p>
<p><strong>Schriften.</strong> Die Website lädt Schriften von Google Fonts (Google LLC). Dabei wird deine IP-Adresse an Google übermittelt.</p>
<p><strong>Fotos.</strong> An unseren Anlässen fotografieren wir. Ausgewählte Bilder zeigen wir auf dieser Website und in unseren Fotoalben bei Flickr (SmugMug Inc., USA). Wenn du auf einem Bild nicht erscheinen möchtest, sag es uns am Anlass oder schreib uns – wir entfernen das Bild.</p>
<p><strong>Cookies und Tracking.</strong> Diese Website setzt keine Cookies zu Analyse- oder Werbezwecken und nutzt keine Tracking-Dienste.</p>
<h3>Weitergabe</h3><p>Wir geben deine Daten nicht an Dritte weiter, ausser an die genannten technischen Dienstleister, soweit das für den Betrieb der Website nötig ist, oder wenn wir gesetzlich dazu verpflichtet sind.</p>
<h3>Aufbewahrung</h3><p>Anfragen und Ideen löschen wir, sobald sie erledigt sind. Mitgliederdaten bewahren wir für die Dauer der Mitgliedschaft und danach so lange auf, wie das Vereins- und Rechnungswesen es verlangt.</p>
<h3>Deine Rechte</h3><p>Du kannst jederzeit Auskunft über deine bei uns gespeicherten Daten verlangen, sie berichtigen oder löschen lassen. Schreib dafür an <a href="mailto:stefan.moser@crazytable.ch" style="text-decoration:underline">stefan.moser@crazytable.ch</a>.</p>
<p class="small">Stand: November 2026. Wir passen diese Erklärung an, wenn sich die Website oder die gesetzlichen Vorgaben ändern.</p>""")

# ---------- Weinkarte ----------
# Datenquelle: data/regions.json = Export der Supabase-Tabelle «regions» (Mitgliederbereich).
# Aktualisieren: im Supabase-SQL-Editor
#   select json_agg(json_build_object('slug',slug,'name',name,'country',country,'lat',lat,'lng',lng,'teaser',teaser,
#     'description',description,'terms',terms,'status',status,'first_tasted',first_tasted,'note',note,'sort_order',sort_order)
#     order by sort_order) from regions where active;
# Resultat in data/regions.json speichern, dann python3 build.py.
import json as _json, html as _html, re as _re, unicodedata as _ud
REGIONS = _json.load(open(os.path.join(ROOT, 'data', 'regions.json'), encoding='utf-8'))
STATUS_LABEL = {'TASTED': 'Im Glas gehabt', 'PLANNED': 'Geplant 2027', 'CATALOG': 'Noch nicht im Glas'}
MONATE = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
COUNTRY_ORDER = ['Schweiz','Italien','Frankreich','Spanien','Portugal','Österreich','Deutschland','Argentinien','Mexiko','USA','Südafrika']

def de_date(iso):
    y, m, d = iso.split('-')
    return f"{int(d)}. {MONATE[int(m)-1]} {y}"

def termslug(t):
    t = _ud.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return _re.sub(r'[^a-z0-9]+', '-', t).strip('-')

def region_article(r):
    meta = STATUS_LABEL[r['status']]
    if r['status'] == 'TASTED' and r.get('first_tasted'):
        meta += ' — zum ersten Mal am ' + de_date(r['first_tasted'])
    chips = ''.join(f'<a class="chip chip-term" href="#begriff-{termslug(t)}">{_html.escape(t)}</a>' for t in r['terms'])
    note = f'<p class="wk-note"><span class="meta">Bei uns</span>{_html.escape(r["note"])}</p>' if r.get('note') else ''
    return (f'<article class="wk-region" id="{r["slug"]}" data-status="{r["status"].lower()}">'
            f'<div class="wk-region-head"><span class="meta">{_html.escape(r["country"])} · {meta}</span>'
            f'<h3>{_html.escape(r["name"])}</h3><p class="wk-teaser">{_html.escape(r["teaser"])}</p></div>'
            f'<div class="wk-region-body"><p>{_html.escape(r["description"] or "")}</p>{note}<div class="chips">{chips}</div></div>'
            f'</article>')

def regions_by_country():
    out = []
    for c in COUNTRY_ORDER:
        rs = [r for r in REGIONS if r['country'] == c]
        if rs:
            out.append(f'<div class="wk-country" id="land-{termslug(c)}"><h2 class="wk-country-h">{c}</h2>'
                       f'<div class="wk-regions">{"".join(region_article(r) for r in rs)}</div></div>')
    return ''.join(out)

def term_index():
    idx = {}
    for r in REGIONS:
        for t in r['terms']:
            idx.setdefault(t, []).append(r)
    items = []
    for t in sorted(idx, key=termslug):
        links = ', '.join(f'<a href="#{r["slug"]}">{_html.escape(r["name"].split(" (")[0])}</a>' for r in idx[t])
        items.append(f'<li id="begriff-{termslug(t)}"><b>{_html.escape(t)}</b><span>{links}</span></li>')
    return ''.join(items)

N_TASTED = sum(1 for r in REGIONS if r['status'] == 'TASTED')
N_PLANNED = sum(1 for r in REGIONS if r['status'] == 'PLANNED')
N_TERMS = len({t for r in REGIONS for t in r['terms']})
COUNTRY_NAV = ''.join(f'<a class="chip" href="#land-{termslug(c)}">{c}</a>' for c in COUNTRY_ORDER if any(r['country'] == c for r in REGIONS))
MAP_DATA = _json.dumps([dict(slug=r['slug'], name=r['name'], lat=r['lat'], lng=r['lng'], status=r['status']) for r in REGIONS], ensure_ascii=False)

WEINKARTE = head('Weinkarte – crazytable', 'Die Weinkarte des Weinclubs crazytable: alle Regionen, aus denen wir an unseren Anlässen getrunken haben, mit kurzen Porträts und den Begriffen, die man dazu kennen sollte.', 'weinkarte') + f"""
<section class="band-green cellar-hero wk-hero">
  <div class="wrap grid-12" style="padding:0;align-items:end">
    <div class="c1-8 stack stack-lg">
      <p class="overline">Weinkarte</p>
      <h1 style="font-size:clamp(56px,9vw,120px)">Wo wir <em>getrunken</em> haben.</h1>
      <p class="lead" style="max-width:560px">Jede Region leuchtet, sobald ein Wein von dort bei einem Clubanlass im Glas war. Seit 2023 wächst die Karte Anlass für Anlass – und mit ihr unser kleines Weinlexikon.</p>
    </div>
    <div class="c10-3 cellar-rule">
      <span class="k">{N_TASTED}</span><span class="v">Regionen im Glas gehabt</span>
      <span class="k">{N_PLANNED}</span><span class="v">Regionen geplant für 2027</span>
      <span class="k">{N_TERMS}</span><span class="v">Begriffe im Lexikon</span>
    </div>
  </div>
</section>

<section class="wk-mapband">
  <div class="wrap">
    <div class="wk-toolbar">
      <div class="wk-seg" role="group" aria-label="Kartenausschnitt"><button type="button" data-view="eu" aria-pressed="true">Europa</button><button type="button" data-view="world" aria-pressed="false">Welt</button></div>
      <div class="wk-legend"><span><i class="wk-dot is-tasted"></i>im Glas gehabt</span><span><i class="wk-dot is-planned"></i>geplant 2027</span><span><i class="wk-dot is-catalog"></i>noch nicht</span></div>
    </div>
    <div class="wk-map" id="wk-map" aria-label="Karte der Weinregionen"></div>
    <p class="small wk-hint">Auf einen Punkt tippen, um zur Region zu springen.</p>
  </div>
  <script id="wk-data" type="application/json">{MAP_DATA}</script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.17/d3.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/topojson/1.6.9/topojson.min.js" defer></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/datamaps/0.5.9/datamaps.world.min.js" defer></script>
  <script src="/js/weinkarte.js" defer></script>
</section>

<div class="wrap" style="padding:0">

<section class="section stack" style="gap:48px">
  <div class="between reveal">
    <h2>Die Regionen</h2>
    <nav class="chips wk-countrynav" aria-label="Länder">{COUNTRY_NAV}</nav>
  </div>
  {regions_by_country()}
</section>

<section class="section grid-12" style="row-gap:40px">
  <div class="c1-4 stack">
    <p class="overline">Weinlexikon</p>
    <h2>Begriffe, die man kennen sollte</h2>
    <p class="lead">Jede Region bringt ihre eigenen Wörter mit. Hier stehen sie beieinander – mit dem Verweis, wo sie auf der Karte zu Hause sind. Die Erklärungen wachsen nach jedem Anlass.</p>
  </div>
  <ol class="wk-terms c6-7">{term_index()}</ol>
</section>

<section class="section" style="border-bottom:0">
  <article class="card card-dashed" style="max-width:560px">
    <p class="overline">Deine Idee</p>
    <h3>Welche Region fehlt?</h3>
    <p>Eine Ecke, die auf der Karte noch dunkel ist, ein Winzer, den wir kennenlernen sollten – schick uns deinen Vorschlag.</p>
    <a class="arrow" href="/verein#ideenbox" style="color:var(--ink)">Zur Ideenbox →</a>
  </article>
</section>
</div>
""" + FOOTER


PAGES = {
    'index.html': INDEX, 'anlaesse.html': ANLAESSE, 'weinkeller.html': WEINKELLER, 'weinkarte.html': WEINKARTE, 'verein.html': VEREIN,
    'mitglied-werden.html': MITGLIED, 'danke.html': DANKE,
    'disclaimer.html': DISCLAIMER, 'datenschutz.html': DATENSCHUTZ,
}
for name, html in PAGES.items():
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', name)
