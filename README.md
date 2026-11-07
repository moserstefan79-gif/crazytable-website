# crazytable.ch – Website

Statische Website, gebaut für Netlify. Keine Datenbank, kein Build-Tool nötig.

## Struktur
- `index.html`, `anlaesse.html`, `weinkeller.html`, `verein.html`, `mitglied-werden.html` – die fünf Seiten
- `weinkarte.html` – Weinkarte und Weinlexikon; Daten aus `data/regions.json` (Export der Supabase-Tabelle `regions`, SQL steht in `build.py`), Karte via `js/weinkarte.js` (Datamaps/d3 von cdnjs)
- `danke.html` (Formular-Bestätigung), `disclaimer.html`, `datenschutz.html`
- `css/style.css` – das ganze Design (Farben/Schriften oben in `:root`)
- `img/` – Bilder; `favicon.svg` ist drin, Fotos fehlen noch (siehe unten)
- `_redirects` – alte Clubdesk-Adressen → neue Seiten; später Login → Weinclub-Plattform
- `netlify.toml` – Sicherheits-Header und Caching
- `termine.ics` – Kalenderdatei für «In Kalender» / «Termine abonnieren»
- `build.py` – erzeugt die HTML-Seiten aus gemeinsamen Bausteinen (Header, Footer, Texte).
  Texte ändern → in `build.py` anpassen → `python3 build.py` ausführen. Die HTML-Dateien lassen sich auch direkt bearbeiten, dann aber `build.py` nicht mehr ausführen (würde überschreiben).

## Deploy auf Netlify (ohne Git)
1. app.netlify.com → «Add new site» → «Deploy manually».
2. Diesen Ordner als Ganzes ins Fenster ziehen.
3. Site → Domain management → crazytable.ch hinzufügen; DNS bei Hostpoint setzen:
   `A @ 75.2.60.5`, `CNAME www <site>.netlify.app.`
4. Site → Forms: die drei Formulare «anmeldung», «kontakt», «ideenbox» erscheinen nach dem ersten Deploy.
   Unter Forms → Settings → Notifications eine E-Mail-Benachrichtigung an stefan.moser@crazytable.ch einrichten.

Mit Git (empfohlen für Änderungen): Ordner in ein Repo, in Netlify «Import from Git», Publish directory `.`.

## Noch zu ergänzen
- Fotos: `img/hero.jpg` (4:5), Porträts `stefan.jpg`, `christian.jpg`, `antoinette.jpg` (1:1), `pontet-canet.jpg` (3:2).
  Danach in `build.py` den jeweiligen `ph('…')`-Platzhalter durch `ph('', img='/img/hero.jpg', alt='…')` ersetzen.
  Die Rückblick-Karten nutzen bereits die Flickr-Vorschaubilder der Club-Alben.
- Flickr-Album-Links: in `build.py` bei `card(...)` die Platzhalter-URL `https://www.flickr.com/` durch die Album-URLs ersetzen.
- Nächster Anlass: Datum, Ort, Anmeldeschluss in `NEXT_EVENT` und in `termine.ics`.
- Weinkeller: Investment II und Flaschenzahlen.
- Disclaimer und Datenschutz: Texte von Clubdesk übernehmen.
- Filter-Chips auf /anlaesse sind rein optisch (kein JavaScript); bei Bedarf später aktivieren.
