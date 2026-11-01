#!/usr/bin/env python3
"""Erzeugt die HTML-Seiten von crazytable.ch aus gemeinsamen Bausteinen.
Aufruf: python3 build.py  -> schreibt *.html ins gleiche Verzeichnis."""
import os
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
<link rel="stylesheet" href="/css/style.css">
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
    <div><span class="h">Club</span><a href="/verein">Verein &amp; Vorstand</a><a href="/anlaesse">Anlässe</a><a href="/weinkeller">Weinkeller</a></div>
    <div><span class="h">Mitmachen</span><a href="/mitglied-werden">Mitglied werden</a><a href="/verein#ideenbox">Ideenbox</a><a href="/mitglied-werden#kontakt">Kontakt</a></div>
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
    <span style="font-size:15px;color:var(--text)">Mai 2027 — Mittwoch</span>
    <span style="font-size:15px;color:var(--muted)">Kargo68, Zuchwil / Solothurn</span>
  </div>
  <div class="c4-6 stack">
    <h2 style="font-size:44px">Doce Copas – zwölf Gläser Spanien</h2>
    <p class="lead" style="font-size:17px">Zwölf spanische Weine, ausgesucht mit Vinos de España aus der Region Solothurn, dazu eine kulinarische Begleitung zu jedem Glas – ohne Musik, dafür mit viel Zeit am Tisch.</p>
    <span class="small">Für Mitglieder · Details und Anmeldung folgen im Frühjahr 2027</span>
  </div>
  <div class="c10-3 stack stack-sm" style="padding-top:6px">
    <a class="btn btn-dark" href="mailto:stefan.moser@crazytable.ch?subject=Anmeldung%20Degustationsabend">Anmelden</a>
    <a class="btn btn-ghost" href="/termine.ics">In Kalender</a>
    <a class="arrow" href="/anlaesse" style="text-align:center;padding-top:8px">Alle Anlässe →</a>
  </div>
</section>'''

INDEX = head('crazytable – Weinclub in Kirchberg BE', 'Weinclub in Kirchberg BE: zwei Degustationen pro Jahr, Winzer persönlich kennenlernen, gemeinsamer Weinkeller. Maximal 25 Mitglieder.', 'home') + f'''
<section class="hero grid-12" style="border-bottom:1px solid var(--line);max-width:1280px;margin:0 auto">
  <div class="c1-7 stack stack-lg">
    <p class="overline">Weinclub — Kirchberg BE — seit 2023</p>
    <h1>Ein Tisch.<br>Viele Gläser.<br><em class="accent">Gute Geschichten.</em></h1>
    <p class="lead" style="max-width:480px">Zweimal im Jahr kommen wir zusammen – zu einem Degustationsabend oder einer Reise, mit Weinen aus aller Welt und den Geschichten dahinter. Und Jahr für Jahr wächst unser gemeinsamer Keller voller Trouvaillen.</p>
    <div class="row">
      <a class="btn btn-primary" href="/mitglied-werden">Mitglied werden</a>
      <a class="btn btn-outline" href="/anlaesse">Anlässe</a>
    </div>
  </div>
  <div class="c8-5">{ph('', img='/img/hero.jpg', alt='Weinkeller mit Barriques und Flaschenregal')}</div>
</section>

<div class="stats">
  <div class="stat"><b>2</b><span>Degustationen pro Jahr, mit Winzerbesuch und Menü</span></div>
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
    <li><span class="n">02</span><h3>Die Degustationen</h3><p>Mindestens zwei Abende pro Jahr. Winzerinnen und Winzer stellen ihre Philosophie persönlich vor, mindestens sechs Weine kommen ins Glas – mit passender kulinarischer Begleitung.</p></li>
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
    <a class="btn btn-ghost" href="/termine.ics">In Kalender</a>
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
      <span class="k">20 %</span><span class="v">der Mitgliederbeiträge</span>
      <span class="k">CHF 1'000</span><span class="v">Deckel pro Jahr</span>
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
        <dl class="facts"><dt>Flaschen</dt><dd>18 × 75 cl</dd><dt>Einstand</dt><dd>[CHF]</dd><dt>Trinkfenster</dt><dd>ab ca. [2033]</dd></dl>
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
      </div>
    </article>
    <article class="bottle bottle-next">
      <div class="bottle-img"><div class="ph ratio-45" style="background:var(--black);align-items:center;justify-content:center"><span style="font-family:var(--serif);font-size:120px;color:var(--cyan);letter-spacing:0">?</span></div></div>
      <div class="bottle-body">
        <span class="meta">Investment IV — HV [2026]</span>
        <h3>Dein Vorschlag</h3>
        <p>Welche Trouvaille sollten wir als Nächstes einlagern? Region, Jahrgang, warum – der Vorstand nimmt die besten Vorschläge in die Auswahl.</p>
        <a class="btn btn-primary" href="/verein#ideenbox" style="align-self:flex-start">Wein vorschlagen</a>
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
      <span class="tl-label">Plansel Selecta 2019</span>
      <div class="tl-track"><span class="tl-dot" style="left:5.5%" title="Kauf 2024"></span><span class="tl-bar" style="left:5.5%;width:61.1%">Trinkfenster bis 2035</span></div>
    </div>
    <div class="tl-row">
      <span class="tl-label">Rosso del Bepi 2016</span>
      <div class="tl-track"><span class="tl-dot" style="left:11.1%" title="Kauf 2025"></span><span class="tl-bar" style="left:11.1%;width:61.1%">Trinkfenster bis ca. 2036</span></div>
    </div>
    <div class="tl-row tl-ghost">
      <span class="tl-label">Investment IV</span>
      <div class="tl-track"><span class="tl-dot" style="left:16.6%" title="Kauf 2026"></span><span class="tl-wait" style="left:16.6%;width:83.4%"></span></div>
    </div>
    <div class="tl-legend"><span><i class="lg-dot"></i>Kauf / Lieferung</span><span><i class="lg-wait"></i>Reifen im Keller</span><span><i class="lg-bar"></i>Trinkfenster</span></div>
  </div>
</section>

<section class="section stack" style="gap:40px">
  <div class="stack" style="gap:12px"><p class="overline">Die Abstimmungen</p><h2>So haben wir entschieden</h2></div>
  <div class="votes">
    <article class="vote">
      <div class="vote-head"><span class="meta">Hauptversammlung — 6. Mai 2023</span><h3>Vier Kandidaten, ein Bordeaux</h3></div>
      <ol class="candidates">
        <li class="winner"><span class="n">1</span><span class="name">Château Pontet-Canet 2023</span><span class="tag">Gewählt · 18 Flaschen</span></li>
        <li><span class="n">2</span><span class="name">Château Giscours 2020</span><span class="tag">Grand Cru Classé</span></li>
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
      <div class="vote-head"><span class="meta">Hauptversammlung — 23. Mai 2025</span><h3>Ein Klassiker aus dem Veneto</h3></div>
      <ol class="candidates">
        <li class="winner"><span class="n">1</span><span class="name">Rosso del Bepi 2016, Giuseppe Quintarelli</span><span class="tag">Gewählt · 12 Flaschen</span></li>
        <li><span class="n">2</span><span class="name">[Kandidat]</span><span class="tag">[Region]</span></li>
        <li><span class="n">3</span><span class="name">[Kandidat]</span><span class="tag">[Region]</span></li>
      </ol>
      <p class="small">Mitbewerber eintragen oder Zeilen löschen.</p>
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
  <div class="people" style="grid-template-columns:minmax(0,1fr) minmax(0,2fr);align-items:end">
    {person('Stefan Moser','Präsident','stefan.moser@crazytable.ch','/img/stefan.jpg')}
    <p class="lead" style="max-width:none">Der Vorstand führt den Club mit leichter Hand: Jahresprogramm, Weinkeller, Hauptversammlung. Wer mitgestalten will – die Ideenbox ist offen.</p>
  </div>
  <div class="grid-12" style="padding-top:24px;border-top:1px solid var(--line)">
    <h3 class="c1-3" style="font-size:24px">Revisoren</h3>
    <div class="c4-6" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px">
      <div class="stack" style="gap:2px"><strong style="font-weight:500">Patrick Felder</strong><span class="small">Revisor</span><a href="mailto:patrick.felder@crazytable.ch" style="font-size:14px">patrick.felder@crazytable.ch</a></div>
      <div class="stack" style="gap:2px"><strong style="font-weight:500">Yves Schüpbach</strong><span class="small">Revisor</span><a href="mailto:yves.schuepbach@crazytable.ch" style="font-size:14px">yves.schuepbach@crazytable.ch</a></div>
    </div>
  </div>
</section>

<section class="section grid-12" id="hauptversammlung">
  <div class="c1-5 stack">
    <p class="overline">Hauptversammlung</p>
    <h2 style="font-size:40px">Einmal im Jahr: Rechnung, Programm – und der Kellerentscheid</h2>
    <p style="color:var(--text)">Die Hauptversammlung findet jeweils vor einem Degustationsabend statt. Wer nicht dabei sein kann, stimmt vorab schriftlich ab – und kann die Weine des Abends in den zehn Tagen danach mit 20 % Rabatt bestellen.</p>
    <div class="row"><a class="btn btn-ghost" href="/statuten.pdf">Statuten (PDF)</a><a class="btn btn-ghost" href="mailto:stefan.moser@crazytable.ch?subject=Schriftliche%20Abstimmung%20HV">Schriftlich abstimmen</a></div>
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
DISCLAIMER = simple('Disclaimer – crazytable', 'Rechtliche Hinweise.', '', 'Disclaimer',
    '<p>[Disclaimer-Text von der bisherigen Website hier einsetzen.]</p>')
DATENSCHUTZ = simple('Datenschutz – crazytable', 'Datenschutzerklärung des Weinclubs crazytable.', '', 'Datenschutz',
    '<p>[Datenschutzerklärung von der bisherigen Website hier einsetzen. Ergänzen: Formulardaten werden über Netlify Forms verarbeitet und per E-Mail an den Vorstand übermittelt.]</p>')

PAGES = {
    'index.html': INDEX, 'anlaesse.html': ANLAESSE, 'weinkeller.html': WEINKELLER, 'verein.html': VEREIN,
    'mitglied-werden.html': MITGLIED, 'danke.html': DANKE,
    'disclaimer.html': DISCLAIMER, 'datenschutz.html': DATENSCHUTZ,
}
for name, html in PAGES.items():
    with open(os.path.join(ROOT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    print('wrote', name)
