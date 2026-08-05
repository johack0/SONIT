# -*- coding: utf-8 -*-
"""Genera docs/piano-wireframe.html (Doc 05) dai blocchi di contenuto del Doc 04."""
import os, sys, html as H, importlib.util

REPO = "/Users/johack/MEGA/Humans.tech/workspace Claudio/SONIT/"
spec = importlib.util.spec_from_file_location("st", REPO + "docs/contenuti/_sorgente_testi.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
PAGES = st.PAGES

# layout previsto per ciascun blocco: (slug, indice) -> (tipo layout, nota)
LAY = {
 ("home",1):("Hero a piena larghezza, testo a sinistra, spazio visivo a destra","due CTA affiancate, una per pubblico"),
 ("home",2):("Fascia numeri, 4 colonne su desktop, 2 su tablet, 1 su mobile","primo blocco di prova"),
 ("home",3):("Introduzione + 3 card affiancate","le card sono cliccabili per intero"),
 ("home",4):("Cinque passi in orizzontale su desktop, verticali su mobile","numerazione visibile"),
 ("home",5):("Fascia su fondo pieno, loghi o sigle + CTA","richiamo alla pagina"),
 ("home",6):("Striscia loghi su una riga, scroll orizzontale su mobile","nessun logo inventato nel wireframe"),
 ("home",7):("Card progetto larga, 2 colonne testo + spazio schema","una sola scheda"),
 ("home",8):("Blocco distinto, fondo diverso dal resto della pagina","è il varco verso il B2C"),
 ("home",9):("Due colonne: dati sedi a sinistra, CTA e mappa a destra","niente form completo"),

 ("chi-siamo",1):("Intro su una colonna stretta, max 65 caratteri per riga",""),
 ("chi-siamo",2):("Testo + elenco ruoli in 2 colonne","i numeri ripresi in evidenza"),
 ("chi-siamo",3):("Blocco valori su fondo tenue, una colonna",""),
 ("chi-siamo",4):("Due schede sedi affiancate + nota copertura nazionale",""),
 ("chi-siamo",5):("Fascia download con due pulsanti file","peso e formato indicati"),
 ("chi-siamo",6):("CTA di chiusura, larghezza piena",""),

 ("soluzioni",1):("Apertura su colonna stretta, senza elementi laterali","è il messaggio principale della pagina"),
 ("soluzioni",2):("Elenco competenze su 2 colonne",""),
 ("soluzioni",3):("3 card business unit affiancate, pari altezza","ingresso al livello 2"),
 ("soluzioni",4):("Cinque passi verticali con numerazione",""),
 ("soluzioni",5):("Blocco con ancora #consulenza, 2 colonne","target del redirect da /consulenza.php"),
 ("soluzioni",6):("Blocco breve su fondo tenue",""),
 ("soluzioni",7):("CTA di chiusura",""),

 ("telecomunicazioni",1):("Apertura 2 colonne: testo + spazio visivo",""),
 ("telecomunicazioni",2):("Sei fasi in sequenza verticale, con la riga di beneficio rientrata","è il cuore della pagina, va il doppio dello spazio"),
 ("telecomunicazioni",3):("Blocco richiamo consulenza, una colonna",""),
 ("telecomunicazioni",4):("Fascia certificazioni pertinenti + CTA",""),
 ("telecomunicazioni",5):("Una o due card progetto",""),
 ("telecomunicazioni",6):("CTA di chiusura contestuale",""),

 ("impianti",1):("Apertura 2 colonne",""),
 ("impianti",2):("Elenco ambiti su 2 colonne",""),
 ("impianti",3):("Due blocchi affiancati: civile / industriale","confronto visivo esplicito"),
 ("impianti",4):("Blocco richiamo consulenza",""),
 ("impianti",5):("Fascia certificazioni + CTA",""),
 ("impianti",6):("Card progetto",""),
 ("impianti",7):("CTA di chiusura",""),

 ("fotovoltaico",1):("Apertura 2 colonne",""),
 ("fotovoltaico",2):("Elenco ambiti su 2 colonne",""),
 ("fotovoltaico",3):("Blocco taglie e contesti, 3 esempi affiancati","segnala visivamente la scala industriale"),
 ("fotovoltaico",4):("Blocco incentivi su fondo tenue",""),
 ("fotovoltaico",5):("Blocco filiera energia, una colonna",""),
 ("fotovoltaico",6):("Blocco varco B2C, fondo diverso, in coda alla pagina","stesso trattamento del blocco privati in home"),
 ("fotovoltaico",7):("CTA di chiusura B2B",""),

 ("fotovoltaico-casa",1):("Hero con form visibile a destra già alla prima schermata","su mobile il form scende sotto il testo, con CTA di ancoraggio"),
 ("fotovoltaico-casa",2):("Quattro passi in orizzontale su desktop",""),
 ("fotovoltaico-casa",3):("Blocco dimensionamento, testo + spazio per schema",""),
 ("fotovoltaico-casa",4):("Blocco detrazioni su fondo tenue",""),
 ("fotovoltaico-casa",5):("Blocco chi installa, 2 colonne",""),
 ("fotovoltaico-casa",6):("FAQ a fisarmonica","le risposte chiuse per default"),
 ("fotovoltaico-casa",7):("Form completo a piena larghezza in chiusura","secondo punto di conversione della pagina"),

 ("certificazioni",1):("Apertura una colonna",""),
 ("certificazioni",2):("Griglia certificazioni: scheda per certificazione","struttura pronta, contenuto da materiali"),
 ("certificazioni",3):("Elenco a due colonne: certificazione + effetto pratico",""),
 ("certificazioni",4):("Blocco sicurezza, una colonna",""),
 ("certificazioni",5):("CTA di chiusura",""),

 ("partner",1):("Apertura una colonna",""),
 ("partner",2):("Griglia loghi per categoria di fornitura","placeholder neutri nel wireframe"),
 ("partner",3):("Elenco categorie di committenti",""),
 ("partner",4):("Blocco proposta di collaborazione + CTA",""),

 ("progetti",1):("Apertura una colonna stretta",""),
 ("progetti",2):("Spiegazione del formato in quattro passi",""),
 ("progetti",3):("Elenco schede progetto, una per riga su desktop","filtro per business unit se le schede superano 4"),
 ("progetti",4):("CTA di chiusura",""),

 ("contatti",1):("Apertura una colonna",""),
 ("contatti",2):("Form su 2 colonne di campi, larghezza contenuta","campi di qualificazione raggruppati"),
 ("contatti",3):("Due schede sedi + riferimenti",""),
 ("contatti",4):("Blocco varco privati",""),
 ("contatti",5):("Pagina /grazie separata, layout minimo centrato","wireframe a sé, non una sezione"),
}

ORDER = [
 ("1", "Impalcatura", ["Header, menu e footer", "Griglia e breakpoint", "Blocchi ricorrenti: CTA di chiusura, fascia numeri, card BU, striscia loghi"],
  "Va per primo: definisce l'ossatura di tutte le altre pagine."),
 ("2", "Home", ["home"], "È la pagina che decide la gerarchia dei messaggi. Va validata prima delle altre."),
 ("3", "Hub soluzioni", ["soluzioni"], "Contenuti completi, nessun blocco in attesa: si può disegnare per intero."),
 ("4", "Tre business unit", ["telecomunicazioni","impianti","fotovoltaico"], "Condividono un solo template: si disegna una volta e si declina."),
 ("5", "Percorso B2C", ["fotovoltaico-casa"], "Layout diverso dal resto: il form è protagonista, non un blocco in coda."),
 ("6", "Chi siamo", ["chi-siamo"], "Struttura pronta, il blocco numeri resta con dati segnaposto."),
 ("7", "Pagine di prova", ["certificazioni","partner","progetti"], "Struttura disegnabile subito, contenuti segnaposto fino ai materiali."),
 ("8", "Conversione", ["contatti"], "Include il wireframe della pagina di conferma /grazie."),
]

BY = {p["slug"]: p for p in PAGES}

def state(p):
    cli = sum(1 for _,s,_ in p["blocks"] if s=="cliente")
    if cli == 0: return ('<span class="tag t-ok">Completa</span>', 0)
    return (f'<span class="tag t-warn">{cli} blocchi segnaposto</span>', cli)

rows = []
for p in PAGES:
    st_html, cli = state(p)
    secs = []
    for i,(name,src,_) in enumerate(p["blocks"],1):
        lay, note = LAY.get((p["slug"], i), ("—",""))
        badge = {"riuso":'<span class="d d-r">riuso</span>',"nuovo":'<span class="d d-n">nuovo</span>',
                 "cliente":'<span class="d d-c">segnaposto</span>'}[src]
        secs.append(f'<tr><td class="num">{i:02d}</td><td><b>{H.escape(name)}</b> {badge}</td>'
                    f'<td>{H.escape(lay)}</td><td class="nt">{H.escape(note)}</td></tr>')
    rows.append(f"""<div class="pg" id="wf-{p['slug']}">
  <div class="ph"><b>{H.escape(p['label'])}</b><code>{p['url']}</code>{st_html}
    <a class="lnk" href="/docs/contenuti/{p['slug']}">Contenuti →</a></div>
  <div class="tbl-wrap"><table>
    <thead><tr><th class="num">#</th><th>Sezione</th><th>Layout previsto</th><th>Nota</th></tr></thead>
    <tbody>{''.join(secs)}</tbody>
  </table></div>
</div>""")

ord_rows = []
for n, title, items, why in ORDER:
    if items and items[0] in BY:
        lst = " · ".join(f'<a href="#wf-{s}">{H.escape(BY[s]["label"])}</a>' for s in items)
    else:
        lst = " · ".join(H.escape(i) for i in items)
    ord_rows.append(f'<tr><td class="num">{n}</td><td><b>{H.escape(title)}</b><br><span class="nt">{lst}</span></td><td>{H.escape(why)}</td></tr>')

tot_secs = sum(len(p["blocks"]) for p in PAGES)
tot_cli = sum(1 for p in PAGES for _,s,_ in p["blocks"] if s=="cliente")

CSS = open(REPO+"docs/architettura-informazioni.html", encoding="utf-8").read()
CSS = CSS[CSS.index("<style>")+7:CSS.index("</style>")]
EXTRA = """
  .pg{border:1px solid var(--line);border-radius:10px;margin:0 0 16px;overflow:hidden}
  .pg .ph{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:var(--blu-tenue);padding:10px 16px;border-bottom:1px solid var(--line)}
  .pg .ph b{font-size:14.5px}
  .pg .ph code{background:#fff}
  .pg .ph .tag{margin-left:auto}
  .pg .ph .lnk{font-size:12px;font-weight:700;text-decoration:none;color:#fff;background:var(--blu);border-radius:16px;padding:4px 11px}
  .pg .ph .lnk:hover{background:var(--blu-scuro)}
  .pg table{min-width:640px}
  td.num,th.num{text-align:right;font-family:var(--mono);font-size:12px;white-space:nowrap;width:38px}
  td.nt{color:var(--ink-soft);font-size:12.6px}
  .d{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;padding:1px 6px;border-radius:20px;vertical-align:1px}
  .d-r{background:#e7f4ec;color:var(--ok)}
  .d-n{background:#e8f0fe;color:var(--info)}
  .d-c{background:#fff4e0;color:var(--warn)}
  pre.wf{font-family:var(--mono);font-size:12px;line-height:1.55;background:#0e1a2b;color:#d7e3f4;padding:20px;border-radius:8px;overflow-x:auto;margin:0 0 18px}
  pre.wf b{color:#7fb2ff;font-weight:600}
  pre.wf i{color:#8e9db4;font-style:normal}
  pre.wf u{color:#ffcf8f;text-decoration:none}
  ul.ck{list-style:none;padding:0}
  ul.ck li{padding:7px 0 7px 26px;border-bottom:1px solid var(--line);position:relative;font-size:14px}
  ul.ck li::before{content:"☐";position:absolute;left:2px;color:var(--blu);font-size:15px}
"""

DOC = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SONIT — Piano dei wireframe e punto di ripresa</title>
<meta name="robots" content="noindex, nofollow">
<style>{CSS}{EXTRA}</style>
</head>
<body>
<div class="wrap">

<aside>
  <p class="brand">SONIT<span>&nbsp;/ DXP</span></p>
  <p class="sub">Piano wireframe · Doc 05</p>
  <nav>
    <div class="grp">Ripresa</div>
    <a href="#stato">Dove siamo</a>
    <a href="#approvare">Cosa approvare prima</a>
    <a href="#ripresa">Primi passi al rientro</a>
    <div class="grp">Piano</div>
    <a href="#criteri">Criteri e impostazione</a>
    <a href="#componenti">Componenti ricorrenti</a>
    <a href="#ordine">Ordine di produzione</a>
    <a href="#sezioni">Sezioni pagina per pagina</a>
    <div class="grp">Schemi</div>
    <a href="#schema-home">Schema home</a>
    <a href="#schema-bu">Schema business unit</a>
    <a href="#schema-b2c">Schema landing B2C</a>
    <div class="grp">Chiusura</div>
    <a href="#validazione">Checklist di validazione</a>
    <a href="#dopo">Cosa viene dopo</a>
  </nav>
  <a class="back" href="/">← Indice dei documenti</a>
  <a class="back" href="/docs/contenuti/">← Doc 04 · Contenuti</a>
  <p class="meta">Versione 1.0<br>05/08/2026</p>
</aside>

<main>

<div class="upbar">
  <a href="/">← Indice dei documenti</a>
  <span>·</span>
  <a href="/docs/architettura-informazioni">Doc 03 · Architettura</a>
  <a href="/docs/contenuti/">Doc 04 · Contenuti</a>
  <span>Stai leggendo: Doc 05 · Piano wireframe</span>
</div>

<header class="top">
  <p class="kicker">Progetto DXP · Documento 05 · Fase F3 → F4</p>
  <h1>Piano dei wireframe e punto di ripresa</h1>
  <p class="lead">Tutto quello che serve per riprendere il lavoro dopo l'approvazione dei contenuti: stato del progetto, cosa va approvato, in che ordine si disegnano i wireframe e quali sezioni contiene ogni pagina.</p>
</header>

<!-- STATO -->
<h2 id="stato">Dove siamo</h2>
<div class="grid">
  <div class="card"><div class="n">F0 → F3</div><div class="l">fasi completate: kick-off, analisi, architettura, contenuti</div></div>
  <div class="card"><div class="n">11</div><div class="l">pagine con contenuti scritti</div></div>
  <div class="card"><div class="n">{tot_secs}</div><div class="l">sezioni da portare in wireframe</div></div>
  <div class="card"><div class="n">{tot_cli}</div><div class="l">sezioni con contenuto segnaposto</div></div>
  <div class="card"><div class="n">7 / 7</div><div class="l">decisioni di struttura validate</div></div>
  <div class="card"><div class="n">13</div><div class="l">materiali ancora attesi dal cliente</div></div>
</div>

<div class="tbl-wrap">
<table>
  <thead><tr><th>Fase</th><th>Deliverable</th><th>Stato</th></tr></thead>
  <tbody>
    <tr><td>F0 · Kick-off</td><td>Obiettivi, vincoli, governance</td><td><span class="tag t-ok">Completata 28/07/2026</span></td></tr>
    <tr><td>F1 · Stato dell'arte</td><td><a href="/docs/stato-arte-sonit">Doc 01</a>, <a href="/docs/alberatura-attuale">Doc 02</a>, testi estratti</td><td><span class="tag t-ok">Completata</span></td></tr>
    <tr><td>F2 · Architettura</td><td><a href="/docs/architettura-informazioni">Doc 03</a> + 7 decisioni validate</td><td><span class="tag t-ok">Completata</span></td></tr>
    <tr><td>F3 · Contenuti</td><td><a href="/docs/contenuti/">Doc 04</a>: 11 pagine, {tot_secs} blocchi</td><td><span class="tag t-info">Scritti, in attesa di approvazione</span></td></tr>
    <tr><td>F3 · Wireframe</td><td>Wireframe low fidelity di tutte le pagine</td><td><span class="tag t-neutro">Pianificata, questo documento</span></td></tr>
    <tr><td>F4 · Direzione visiva</td><td>Due proposte di design</td><td><span class="tag t-neutro">Da avviare</span></td></tr>
    <tr><td>F5 → F7</td><td>Design completo, sviluppo, go-live</td><td><span class="tag t-neutro">Da avviare</span></td></tr>
  </tbody>
</table>
</div>

<div class="box">
  <p><strong>Il punto esatto in cui il lavoro si è fermato.</strong> Struttura e contenuti sono decisi e scritti. Il passo successivo non richiede altre decisioni di architettura: richiede due cose, l'approvazione dei contenuti da parte di Giorgio e i materiali che il cliente deve caricare. I wireframe si possono iniziare appena arriva la prima delle due, perché la struttura delle sezioni non cambia con i materiali: cambia solo cosa ci sta dentro.</p>
</div>

<!-- APPROVARE -->
<h2 id="approvare">Cosa approvare prima dei wireframe</h2>
<p>Non serve approvare tutto. Servono tre cose, in ordine di impatto.</p>
<div class="tbl-wrap">
<table>
  <thead><tr><th>#</th><th>Da approvare</th><th>Chi</th><th>Se non arriva</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><b>Ordine e presenza delle sezioni</b> di ogni pagina, come elencate nel <a href="/docs/contenuti/">Doc 04</a>. È la parte che definisce il wireframe.</td><td>Giorgio</td><td>I wireframe si rifanno: è il costo più alto di tutta la fase</td></tr>
    <tr><td>2</td><td><b>Messaggio principale della home</b>: "Una sola regia su reti, impianti ed energia" e la riga di offerta sotto.</td><td>Giorgio e Beatrice</td><td>Cambia l'hero e la doppia CTA, quindi la prima schermata</td></tr>
    <tr><td>3</td><td><b>I numeri aziendali</b> da pubblicare: quali dati e con quali valori aggiornati.</td><td>Giorgio</td><td>Il blocco resta nel wireframe con dati segnaposto, si chiude dopo</td></tr>
  </tbody>
</table>
</div>
<p>Il copy nel dettaglio della singola frase <strong>non</strong> blocca i wireframe: a bassa fedeltà conta la gerarchia, non la parola esatta. Le rifiniture di testo si fanno in fase di design, quando si vede quanto spazio ha ogni blocco.</p>

<!-- RIPRESA -->
<h2 id="ripresa">Primi passi al rientro</h2>
<ol>
  <li><strong>Leggere <code>WORKLOG.md</code></strong>: contiene fasi, attività con stato, decisioni chiuse, materiali attesi e diario. È il punto di verità sullo stato del progetto.</li>
  <li><strong>Verificare cosa è arrivato dal cliente</strong> sul Drive condiviso e aggiornare le voci A-01 → A-13 del worklog. Ogni materiale che arriva chiude uno o più blocchi segnaposto del Doc 04.</li>
  <li><strong>Registrare l'approvazione</strong> dei contenuti nel diario, indicando cosa è stato approvato e cosa è stato chiesto di cambiare.</li>
  <li><strong>Aggiornare i testi</strong> se ci sono modifiche: si modifica <code>docs/contenuti/_sorgente_testi.py</code> e si rigenera con <code>python3 docs/contenuti/_genera.py</code>. Non si editano i singoli HTML.</li>
  <li><strong>Partire dai wireframe nell'ordine indicato qui sotto</strong>, cominciando dall'impalcatura e dalla home.</li>
</ol>

<div class="box warn">
  <p><strong>Da non perdere per strada.</strong> Ci sono quattro cose che vanno portate in F6 e che è facile dimenticare a distanza di settimane: il <code>canonical</code> rotto su 7 pagine su 10 va corretto nel nuovo sito; <code>/partner.php</code> in sitemap e in 404 si chiude con la nuova pagina partner; GA4 e Search Console vanno attivati <em>prima</em> del go-live per avere una baseline; i testi legali vanno portati su dominio proprio. Sono le voci W-022, W-026 e W-025 del worklog.</p>
</div>

<!-- CRITERI -->
<h2 id="criteri">Criteri e impostazione dei wireframe</h2>
<ul>
  <li><strong>Bassa fedeltà, davvero.</strong> Nessun colore di brand, nessuna immagine definitiva, tipografia di sistema. Si valuta struttura, ordine e peso dei blocchi: se si guarda il colore, si sta valutando la cosa sbagliata.</li>
  <li><strong>Tre larghezze</strong> per ogni pagina: mobile 375, tablet 768, desktop 1280. Il mobile non è una riduzione del desktop: per le pagine con form, il form cambia posizione.</li>
  <li><strong>Griglia a 12 colonne</strong> su desktop, 8 su tablet, 4 su mobile, con larghezza massima del contenuto testuale di circa 65 caratteri per riga.</li>
  <li><strong>Testo reale, non lorem ipsum.</strong> Si usano i contenuti del Doc 04: è l'unico modo per vedere se un blocco è troppo lungo o troppo corto prima del design.</li>
  <li><strong>Ogni sezione porta il suo numero</strong> del Doc 04, così il confronto tra wireframe e contenuti è immediato in revisione.</li>
  <li><strong>Le sezioni segnaposto si disegnano comunque</strong>, con un contrassegno visibile: la struttura non deve aspettare i materiali.</li>
  <li><strong>Ogni pagina finisce con una CTA</strong> pertinente al proprio pubblico. Nessuna pagina senza uscita, nessun form generico replicato.</li>
</ul>

<!-- COMPONENTI -->
<h2 id="componenti">Componenti ricorrenti da disegnare una volta sola</h2>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Componente</th><th>Contenuto</th><th>Dove compare</th></tr></thead>
  <tbody>
    <tr><td>Header</td><td>Logo · telefono · link "Area riservata" · menu a 6 voci con sottomenu su Soluzioni</td><td>Tutte le pagine</td></tr>
    <tr><td>Menu mobile</td><td>Le stesse 6 voci, sottomenu espandibile, telefono come pulsante di chiamata</td><td>Tutte le pagine, sotto 768px</td></tr>
    <tr><td>Footer</td><td>Dati societari e P.IVA · colonna soluzioni · colonna azienda · legali · social · area riservata</td><td>Tutte le pagine</td></tr>
    <tr><td>CTA di chiusura</td><td>Titolo breve + una riga + pulsante, contestuale alla pagina</td><td>Tutte tranne la landing B2C</td></tr>
    <tr><td>Fascia numeri</td><td>4 dati con etichetta</td><td>Home, Chi siamo</td></tr>
    <tr><td>Card business unit</td><td>Titolo, 2 righe, link</td><td>Home, Soluzioni</td></tr>
    <tr><td>Striscia loghi</td><td>Placeholder neutri, scroll orizzontale su mobile</td><td>Home, Partner</td></tr>
    <tr><td>Scheda progetto</td><td>Contesto · problema · soluzione · esito</td><td>Home, Progetti, pagine business unit</td></tr>
    <tr><td>Blocco varco B2C</td><td>Fondo distinto, una riga, un pulsante</td><td>Home, Fotovoltaico B2B, Contatti</td></tr>
    <tr><td>Form B2B</td><td>9 campi con qualificazione, 2 colonne</td><td>Contatti</td></tr>
    <tr><td>Form B2C</td><td>7 campi, colonna singola, sempre visibile in alto</td><td>Fotovoltaico per la casa</td></tr>
    <tr><td>Cookie bar</td><td>Testo breve, un pulsante, link alla cookie policy sul dominio Sonit</td><td>Tutte le pagine</td></tr>
  </tbody>
</table>
</div>

<!-- ORDINE -->
<h2 id="ordine">Ordine di produzione</h2>
<div class="tbl-wrap">
<table>
  <thead><tr><th class="num">#</th><th>Blocco di lavoro</th><th>Perché in questa posizione</th></tr></thead>
  <tbody>{''.join(ord_rows)}</tbody>
</table>
</div>

<!-- SEZIONI -->
<h2 id="sezioni">Sezioni pagina per pagina</h2>
<p>Ogni sezione corrisponde a un blocco di contenuto del <a href="/docs/contenuti/">Doc 04</a>, nello stesso ordine e con la stessa numerazione. La colonna layout è la proposta di impaginazione da verificare in wireframe.</p>
{''.join(rows)}

<!-- SCHEMI -->
<h2 id="schema-home">Schema della home</h2>
<pre class="wf">
<i>desktop 1280 · le sezioni numerate come nel Doc 04</i>

╭─ <b>HEADER</b>
│  logo · telefono · area riservata
│  Chi siamo   Soluzioni ▾   Certificazioni   Partner   Progetti   Contatti
├──────────────────────────────────────────────────────────────
│  <b>01 · HERO</b>
│  ┌ testo, 7 colonne ──────────────┐  ┌ spazio visivo, 5 col ┐
│  │ Una sola regia su reti,        │  │                      │
│  │ impianti ed energia.           │  │                      │
│  │ riga di offerta, 2 righe       │  │                      │
│  │ [ Sono un'impresa ] [ privato ]│  │                      │
│  └────────────────────────────────┘  └──────────────────────┘
├──────────────────────────────────────────────────────────────
│  <b>02 · NUMERI</b>        45  ·  5 anni  ·  2 sedi  ·  Italia
├──────────────────────────────────────────────────────────────
│  <b>03 · TRE BUSINESS UNIT</b>
│  intro su 2 righe
│  ┌ TLC ─────────┐  ┌ Impianti ────┐  ┌ Fotovoltaico ┐
│  └──────────────┘  └──────────────┘  └──────────────┘
├──────────────────────────────────────────────────────────────
│  <b>04 · METODO IN 5 PASSI</b>       1 → 2 → 3 → 4 → 5
├──────────────────────────────────────────────────────────────
│  <b>05 · CERTIFICAZIONI</b>          <u>segnaposto</u> · sigle + CTA
├──────────────────────────────────────────────────────────────
│  <b>06 · PARTNER</b>                 <u>segnaposto</u> · striscia loghi
├──────────────────────────────────────────────────────────────
│  <b>07 · PROGETTO IN EVIDENZA</b>    <u>segnaposto</u> · una scheda
├──────────────────────────────────────────────────────────────
│  <b>08 · FOTOVOLTAICO PRIVATI</b>    fondo distinto → landing B2C
├──────────────────────────────────────────────────────────────
│  <b>09 · CONTATTI RAPIDI</b>         sedi  ·  CTA + mappa
├──────────────────────────────────────────────────────────────
│  <b>FOOTER</b>
│  dati societari · soluzioni · azienda · legali · social
╰──────────────────────────────────────────────────────────────

<i>mobile 375: stesso ordine, colonna singola. Le due CTA dell'hero restano
affiancate se ci stanno, altrimenti impilate con quella B2B per prima.</i>
</pre>

<h2 id="schema-bu">Schema delle pagine business unit</h2>
<pre class="wf">
<i>un solo template per Telecomunicazioni, Impianti e Fotovoltaico B2B</i>

╭─ HEADER
├──────────────────────────────────────────────────────────────
│  <b>01 · APERTURA</b>
│  ┌ cosa facciamo e per chi, 2 paragrafi ┐  ┌ spazio visivo ┐
│  └──────────────────────────────────────┘  └───────────────┘
├──────────────────────────────────────────────────────────────
│  <b>02 · AMBITI DI INTERVENTO</b>     elenco su 2 colonne
├──────────────────────────────────────────────────────────────
│  <b>03 · COME LAVORIAMO</b>
│    fase 1 ─ descrizione della lavorazione
│             <i>› per il committente: il beneficio</i>
│    fase 2 ─ …
│    <i>su Telecomunicazioni sono 6 fasi: va il doppio dello spazio</i>
├──────────────────────────────────────────────────────────────
│  <b>04 · CONSULENZA E PRATICHE</b>    richiamo del blocco trasversale
├──────────────────────────────────────────────────────────────
│  <b>05 · CERTIFICAZIONI PERTINENTI</b>  <u>segnaposto</u> + CTA
├──────────────────────────────────────────────────────────────
│  <b>06 · PROGETTI COLLEGATI</b>       <u>segnaposto</u> · 1–2 schede
├──────────────────────────────────────────────────────────────
│  <b>07 · CTA DI CHIUSURA</b>          contestuale alla business unit
│  <i>solo su Fotovoltaico: prima della CTA, il varco verso il B2C</i>
├──────────────────────────────────────────────────────────────
│  FOOTER
╰──────────────────────────────────────────────────────────────
</pre>

<h2 id="schema-b2c">Schema della landing B2C</h2>
<pre class="wf">
<i>/fotovoltaico-casa · unica pagina con il form in prima schermata</i>

╭─ HEADER ridotto      <i>logo · telefono · torna al sito</i>
├──────────────────────────────────────────────────────────────
│  <b>01 · HERO + FORM</b>
│  ┌ promessa, 7 colonne ───────────┐  ┌ form, 5 colonne ─────┐
│  │ Il fotovoltaico per la tua     │  │ nome e cognome       │
│  │ casa, dal sopralluogo          │  │ comune               │
│  │ all'accensione.                │  │ telefono             │
│  │ 3 righe di promessa            │  │ email                │
│  │ [ Chiama ]                     │  │ [ Richiedi ]         │
│  └────────────────────────────────┘  └──────────────────────┘
├──────────────────────────────────────────────────────────────
│  <b>02 · COME FUNZIONA</b>
│  1 sopralluogo → 2 progetto → 3 installazione → 4 attivazione
├──────────────────────────────────────────────────────────────
│  <b>03 · CHE IMPIANTO TI SERVE</b>    <u>segnaposto taglie</u>
├──────────────────────────────────────────────────────────────
│  <b>04 · DETRAZIONI E PRATICHE</b>    fondo tenue
├──────────────────────────────────────────────────────────────
│  <b>05 · CHI VIENE A INSTALLARE</b>   2 colonne
├──────────────────────────────────────────────────────────────
│  <b>06 · DOMANDE FREQUENTI</b>        fisarmonica, risposte chiuse
├──────────────────────────────────────────────────────────────
│  <b>07 · FORM COMPLETO</b>            secondo punto di conversione
├──────────────────────────────────────────────────────────────
│  FOOTER ridotto
╰──────────────────────────────────────────────────────────────

<i>mobile 375: il form dell'hero scende sotto la promessa, con un pulsante di
ancoraggio in prima schermata. Nessun contenuto industriale, nessuna taglia
in MW: la separazione dei pubblici è anche visiva.</i>
</pre>

<!-- VALIDAZIONE -->
<h2 id="validazione">Checklist di validazione dei wireframe</h2>
<p>Da verificare prima di portare i wireframe al cliente.</p>
<ul class="ck">
  <li>Ogni pagina ha tutte le sezioni previste dal Doc 04, nello stesso ordine, con la stessa numerazione</li>
  <li>Ogni sezione segnaposto è contrassegnata come tale e non sembra contenuto definitivo</li>
  <li>Ogni pagina ha una CTA di chiusura pertinente al proprio pubblico</li>
  <li>Nessuna pagina contiene il form B2B generico fuori da <code>/contatti</code></li>
  <li>Il varco verso il B2C compare in home, sulla pagina fotovoltaico B2B e nei contatti, e in nessun altro punto</li>
  <li>La landing B2C non contiene riferimenti a impianti industriali o taglie in MW</li>
  <li>Le tre larghezze sono disegnate per ogni pagina, non solo il desktop</li>
  <li>I form mostrano tutti i campi previsti, compresi consenso privacy e antispam</li>
  <li>La pagina di conferma <code>/grazie</code> è disegnata come pagina a sé</li>
  <li>Header e footer sono identici su tutte le pagine, con lo stato attivo del menu corretto</li>
  <li>Il link all'area riservata è in header e non ci sono form di login nelle pagine pubbliche</li>
  <li>I testi usati sono quelli del Doc 04, non testo finto</li>
  <li>Nessun blocco supera in altezza ciò che il suo contenuto reale richiede</li>
</ul>

<!-- DOPO -->
<h2 id="dopo">Cosa viene dopo i wireframe</h2>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Fase</th><th>Cosa si produce</th><th>Cosa serve avere chiuso prima</th></tr></thead>
  <tbody>
    <tr><td>F4 · Direzione visiva</td><td>Due proposte di design con direzioni diverse, sulla home e su una pagina interna</td><td>Wireframe approvati; palette derivata dal blu di brand <code>#003A83</code>; libreria immagini standard selezionata, senza foto reali di cantiere</td></tr>
    <tr><td>F5 · Design completo</td><td>Design system e tutte le pagine, desktop e mobile, con i contenuti definitivi</td><td>Direzione visiva scelta; materiali del cliente arrivati, altrimenti restano segnaposto anche nel design</td></tr>
    <tr><td>F6 · Sviluppo</td><td>Sito in staging con form, SEO tecnico, accessibilità, performance</td><td>Design approvato; caselle email di destinazione; testi legali; PDF di brochure e company profile</td></tr>
    <tr><td>F7 · Go-live</td><td>Pubblicazione, redirect 301, analytics, collaudo</td><td>Accessi a dominio, DNS e hosting; GA4 e Search Console attivati prima del lancio per la baseline</td></tr>
  </tbody>
</table>
</div>

<div class="box ok">
  <p><strong>Riassunto in una riga.</strong> Struttura decisa, contenuti scritti, piano dei wireframe pronto: al rientro si aggiorna il worklog con ciò che è arrivato, si registra l'approvazione e si disegna partendo dall'impalcatura e dalla home, seguendo l'ordine di produzione di questo documento.</p>
</div>

<footer class="doc">
  <p><strong>SONIT · Progetto DXP — Documento 05: piano dei wireframe e punto di ripresa.</strong> Versione 1.0 del 05/08/2026. Costruito sui contenuti del <a href="/docs/contenuti/">Documento 04</a> e sull'architettura validata del <a href="/docs/architettura-informazioni">Documento 03</a>. Le sezioni elencate sono generate dalla stessa sorgente dei contenuti: restano allineate a ogni rigenerazione.</p>
  <p><a href="/">Indice dei documenti</a> · <a href="/docs/contenuti/">Contenuti</a> · <a href="/docs/architettura-informazioni">Architettura</a> · <a href="/docs/alberatura-attuale">Alberatura attuale</a> · <a href="/docs/stato-arte-sonit">Stato dell'arte</a></p>
</footer>

</main>
</div>
</body>
</html>
"""
open(REPO+"docs/piano-wireframe.html","w",encoding="utf-8").write(DOC)
print("piano-wireframe.html scritto ·", tot_secs, "sezioni ·", tot_cli, "segnaposto")
