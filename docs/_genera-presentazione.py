# -*- coding: utf-8 -*-
"""Genera presentazione/index.html: versione cliente, alberatura semplificata
+ wireframe disegnati con i contenuti dentro.

Sorgenti: docs/contenuti/_sorgente_testi.py (copy) e docs/_layout.py (LAY, SHAPE).
Rigenerare con: python3 docs/_genera-presentazione.py
"""
import os, re, sys, html as H, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)

spec = importlib.util.spec_from_file_location("st", os.path.join(HERE, "contenuti", "_sorgente_testi.py"))
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
PAGES = st.PAGES

from _layout import LAY, SHAPE  # noqa: E402

DATA = "17/08/2026"
OUT = os.path.join(REPO, "presentazione")

# pagine fuori dal menu principale
OFF_MENU = {"fotovoltaico-casa"}

MENU = ["Chi siamo", "Soluzioni", "Certificazioni", "Partner", "Progetti", "Contatti"]

# una riga per pagina, in lingua da riunione
PITCH = {
 "home": "La prima schermata deve dire chi siete e che dimensione avete, prima di elencare i servizi.",
 "chi-siamo": "La pagina che regge il posizionamento: struttura, crescita, sedi, documenti scaricabili.",
 "soluzioni": "Spiega l'ecosistema e distribuisce verso le tre aree. Da qui non si esce a mani vuote.",
 "telecomunicazioni": "Il core business raccontato per intero, fase per fase, con il beneficio per il committente.",
 "impianti": "Distingue il contesto civile da quello industriale, che oggi sono mescolati.",
 "fotovoltaico": "La business unit in crescita, con taglia industriale evidente e il varco verso i privati in coda.",
 "fotovoltaico-casa": "Percorso separato per i privati: il form è protagonista, nessun contenuto industriale.",
 "certificazioni": "Risponde in anticipo alla domanda di qualifica che ogni committente strutturato pone.",
 "partner": "Con chi lavorate: la catena di fornitura come indicatore di affidabilità.",
 "progetti": "I lavori raccontati come casi, con l'imprevisto affrontato. Non un album di foto.",
 "contatti": "Converte qualificando la richiesta, così arriva già smistata alla persona giusta.",
}

# ─────────────────────────────────────────────── trasformazione del copy

RE_NOTE = re.compile(r'(?s)<p class="c-note">.*?</p>')
RE_CLI  = re.compile(r'(?s)<span class="cli">DA MATERIALI CLIENTE · (.*?)</span>')
RE_TODO = re.compile(r'(?s)<span class="todo">DA CONFERMARE · (.*?)</span>')
RE_BTN  = re.compile(r'(?s)<p class="c-btn">(.*?)</p>')
RE_LINK = re.compile(r'(?s)<p class="c-link">(.*?)</p>')


def _plain(t):
    """testo pulito da una nota interna: via i tag e i riferimenti interni di progetto"""
    t = re.sub(r"<[^>]+>", " ", t)
    # via i codici del worklog: non hanno senso per il cliente
    t = re.sub(r"(?i)[.,;:·]?\s*(?:è\s+la\s+|la\s+)?voce\s+A-\d+(?:\s+del\s+worklog)?", "", t)
    t = re.sub(r"(?i)\s*del worklog", "", t)
    t = re.sub(r"\s+([,.;:])", r"\1", t)
    t = re.sub(r"\s+", " ", t).strip(" .,;:·")
    return t


def requests_of(copy):
    """estrae le richieste al cliente: [(tipo, testo)] con tipo materiale|conferma"""
    out = []
    for m in RE_CLI.finditer(copy):
        out.append(("materiale", _plain(m.group(1))))
    for m in RE_TODO.finditer(copy):
        out.append(("conferma", _plain(m.group(1))))
    return out


def buttons(inner):
    """[Etichetta → /url] &nbsp; [Altra] -> pulsanti disegnati"""
    labels = re.findall(r"\[([^\]]+)\]", inner)
    if not labels:
        return f'<p class="wbtns">{inner}</p>'
    out = []
    for lab in labels:
        lab = re.split(r"\s*(?:→|->)\s*", lab)[0].strip()
        out.append(f'<span class="wb">{H.escape(lab)}</span>')
    return '<p class="wbtns">' + "".join(out) + "</p>"


RE_LBL = re.compile(r'(?s)<p class="c-lbl">(.*?)</p>')


def clean(copy, name=""):
    """copy pronto per il wireframe: senza note interne, con pulsanti disegnati"""
    t = RE_NOTE.sub("", copy)
    # la prima etichetta di sezione, se ripete il nome del blocco, è rumore
    m = RE_LBL.search(t)
    if m and name and _plain(m.group(1)).lower() == name.strip().lower():
        t = t[:m.start()] + t[m.end():]
    # etichette residue nel corpo del testo: restano, ma in lingua cliente
    t = RE_CLI.sub(lambda m: f'<span class="ask">da voi: {m.group(1)}</span>', t)
    t = RE_TODO.sub(lambda m: f'<span class="ask">da confermare: {m.group(1)}</span>', t)
    t = RE_BTN.sub(lambda m: buttons(m.group(1)), t)
    t = RE_LINK.sub(lambda m: f'<p class="wlink">{m.group(1)}</p>', t)
    return t.strip()


# ─────────────────────────────────────────────── mattoni del wireframe

def ph(caption, cls=""):
    return f'<div class="ph {cls}"><span>{H.escape(caption)}</span></div>'


def fields(n, cols=2, submit="Invia"):
    fs = "".join('<i></i>' for _ in range(n))
    return (f'<div class="fbox"><div class="fgrid c{cols}">{fs}</div>'
            f'<div class="fcheck"><b></b><span>consenso privacy</span></div>'
            f'<span class="wb">{H.escape(submit)}</span></div>')


def repeat(n, caption, cls="ph-sm"):
    return "".join(ph(caption, cls) for _ in range(n))


def shape_html(shape, inner):
    """restituisce (classe della fascia, html interno)"""
    if shape == "hero":
        return "band-hero", f'<div class="g2"><div>{inner}</div>{ph("spazio visivo", "ph-lg")}</div>'
    if shape == "hero-form":
        return "band-hero", f'<div class="g2"><div>{inner}</div>{fields(6, 1, "Richiedi il sopralluogo")}</div>'
    if shape == "split":
        return "", f'<div class="g2"><div>{inner}</div>{ph("spazio visivo", "ph-md")}</div>'
    if shape == "narrow":
        return "", f'<div class="nar">{inner}</div>'
    if shape == "duo":
        return "", f'<div class="cols2">{inner}</div>'
    if shape == "trio":
        return "", inner + f'<div class="g3">{repeat(3, "esempio di impianto")}</div>'
    if shape == "tinted":
        return "tint", inner
    if shape == "numbers":
        return "tint", inner
    if shape == "logos":
        return "", inner + f'<div class="logos">{repeat(6, "logo", "ph-logo")}</div>'
    if shape == "logogrid":
        cats = ["Telecomunicazioni", "Materiale elettrico", "Fotovoltaico", "Sicurezza"]
        gs = "".join(f'<div class="lg"><span class="cap">{c}</span>'
                     f'<div class="logos">{repeat(3, "logo", "ph-logo")}</div></div>' for c in cats)
        return "", inner + f'<div class="lgrid">{gs}</div>'
    if shape == "certgrid":
        card = ('<div class="cert"><span class="cap">sigla e norma</span>'
                '<i></i><i class="s"></i><i class="s"></i>'
                '<span class="wlink">PDF →</span></div>')
        return "", inner + f'<div class="g3">{card * 6}</div>'
    if shape == "project":
        return "", inner + ('<div class="proj">' + ph("immagine di contesto", "ph-md") +
                            '<div class="lines"><span class="cap">titolo del progetto</span>'
                            '<i></i><i></i><i class="s"></i>'
                            '<span class="wb">Leggi il progetto</span></div></div>')
    if shape == "projectlist":
        row = ('<div class="proj">' + ph("immagine", "ph-sm") +
               '<div class="lines"><span class="cap">titolo del progetto</span>'
               '<i></i><i class="s"></i><span class="wlink">Apri la scheda →</span></div></div>')
        return "", inner + row * 3
    if shape == "highlight":
        return "hl", f'<div class="g2"><div>{inner}</div>{ph("immagine residenziale", "ph-md")}</div>'
    if shape == "contact":
        return "", f'<div class="g2"><div>{inner}</div>{ph("mappa delle due sedi", "ph-md")}</div>'
    if shape == "download":
        return "tint", inner
    if shape == "form":
        return "", f'<div class="nar">{inner}</div>{fields(8, 2, "Invia la richiesta")}'
    if shape == "accordion":
        return "", f'<div class="acc">{inner}</div>'
    if shape == "cta":
        return "ctab", f'<div class="nar">{inner}</div>'
    if shape == "thanks":
        return "thx", f'<div class="nar">{inner}</div>'
    return "", inner


# ─────────────────────────────────────────────── pagine

def screen(p):
    """il wireframe completo di una pagina, dentro una finestra di browser"""
    secs = []
    for i, (name, src, copy) in enumerate(p["blocks"], 1):
        shape = SHAPE.get((p["slug"], i), "full")
        lay = LAY.get((p["slug"], i), ("", ""))[0]
        body = clean(copy, name)
        cls, inner = shape_html(shape, body)
        # le richieste già visibili nel corpo del testo non si ripetono nel riquadro
        needs = [(k, t) for k, t in requests_of(copy) if t not in body]
        need_html = ""
        if src == "cliente" or needs:
            items = "".join(
                f'<li><b>{"Serve da voi" if k == "materiale" else "Da confermare"}</b> · {H.escape(t)}</li>'
                for k, t in needs) or "<li><b>Serve da voi</b> · materiale non ancora disponibile</li>"
            need_html = f'<div class="need"><ul>{items}</ul></div>'
        flag = ' data-wait="1"' if src == "cliente" else ""
        secs.append(
            f'<section class="band {cls}"{flag}>'
            f'<div class="blabel"><span class="bn">{i:02d}</span>'
            f'<span class="bt">{H.escape(name)}</span>'
            + (f'<span class="bw">in attesa di materiali</span>' if src == "cliente" else "")
            + f'</div>'
            f'<div class="binner">{inner}{need_html}</div>'
            + (f'<p class="bcap">{H.escape(lay)}</p>' if lay and lay != "—" else "")
            + '</section>')

    nav = "".join(f'<span>{m}</span>' for m in MENU)
    return f"""<div class="screen">
  <div class="chrome"><i></i><i></i><i></i><code>sonit.it{H.escape(p['url'])}</code></div>
  <div class="site">
    <div class="topnav"><b>SONIT</b><div class="mn">{nav}</div><span class="res">+39 0776 868072 · Area riservata</span></div>
    {''.join(secs)}
    <div class="sitefoot"><span>Sedi · contatti · certificazioni · privacy e cookie</span></div>
  </div>
</div>"""


def page_block(p):
    waiting = sum(1 for _, s, _ in p["blocks"] if s == "cliente")
    state = (f'<span class="tag t-warn">{waiting} '
             f'{"sezione" if waiting == 1 else "sezioni"} in attesa di materiali</span>'
             if waiting else '<span class="tag t-ok">contenuti completi</span>')
    off = '<span class="tag t-off">fuori dal menu</span>' if p["slug"] in OFF_MENU else ""
    return f"""<div class="pageblock" id="p-{p['slug']}">
  <div class="phead">
    <div>
      <p class="pk">Pagina</p>
      <h3>{H.escape(p['label'])}</h3>
      <code>{H.escape(p['url'])}</code>
    </div>
    <div class="pmeta">{state}{off}</div>
  </div>
  <p class="ppitch">{H.escape(PITCH.get(p['slug'], p['goal']))}</p>
  <dl class="pdl">
    <dt>A cosa serve</dt><dd>{H.escape(p['goal'])}</dd>
    <dt>Cosa può fare chi la visita</dt><dd>{H.escape(p['cta'])}</dd>
    <dt>Sezioni</dt><dd>{len(p['blocks'])}, nell'ordine in cui si incontrano scorrendo</dd>
  </dl>
  {screen(p)}
</div>"""


# ─────────────────────────────────────────────── alberatura semplificata

def tree():
    def node(label, url, slug=None, note="", cls=""):
        link = f'<a href="#p-{slug}">' if slug else "<span>"
        end = "</a>" if slug else "</span>"
        n = f'<em>{H.escape(note)}</em>' if note else ""
        return (f'<li class="{cls}">{link}<b>{H.escape(label)}</b>'
                f'<code>{H.escape(url)}</code>{end}{n}</li>')

    figli = "".join([
        node("Chi siamo", "/chi-siamo", "chi-siamo"),
        node("Soluzioni", "/soluzioni", "soluzioni", "hub delle tre aree"),
        f'<li class="sub"><ul>'
        + node("Telecomunicazioni", "/soluzioni/telecomunicazioni", "telecomunicazioni")
        + node("Impianti civili e industriali", "/soluzioni/impianti", "impianti")
        + node("Fotovoltaico ed efficientamento", "/soluzioni/fotovoltaico", "fotovoltaico")
        + "</ul></li>",
        node("Certificazioni", "/certificazioni", "certificazioni"),
        node("Partner e fornitori", "/partner", "partner"),
        node("Progetti", "/progetti", "progetti"),
        node("Contatti", "/contatti", "contatti", "con pagina di conferma /grazie"),
    ])
    return f"""<div class="tree">
  <ul class="lv0">{node("Home", "/", "home")}</ul>
  <ul class="lv1">{figli}</ul>
</div>

<div class="treeside">
  <div class="ts">
    <p class="cap">Percorso privati, separato</p>
    <div class="tree"><ul class="lv0">{node("Fotovoltaico per la casa", "/fotovoltaico-casa", "fotovoltaico-casa",
          "raggiungibile dalla home, dalla pagina fotovoltaico e dai contatti, non dal menu")}</ul></div>
    <p>Chi cerca il fotovoltaico per la propria abitazione non attraversa i contenuti industriali, e chi valuta Sonit come fornitore non incontra il linguaggio da privato.</p>
  </div>
  <div class="ts">
    <p class="cap">Pagine di servizio</p>
    <p>Privacy policy e cookie policy su dominio Sonit, non più su un sito terzo. Area riservata come link in testata, verso <code>app.sonit.it</code>.</p>
  </div>
  <div class="ts">
    <p class="cap">Predisposte, non pubblicate al lancio</p>
    <p>Lavora con noi e IT / cybersecurity: struttura pronta, si accendono quando decidete voi.</p>
  </div>
</div>"""


# ─────────────────────────────────────────────── cosa serve dal cliente

def needs_section():
    rows = []
    tot_m = tot_c = 0
    for p in PAGES:
        items = []
        for i, (name, src, copy) in enumerate(p["blocks"], 1):
            for k, t in requests_of(copy):
                items.append(f'<li><span class="k {"km" if k == "materiale" else "kc"}">'
                             f'{"materiale" if k == "materiale" else "conferma"}</span>'
                             f'<b>{H.escape(name)}</b> — {H.escape(t)}</li>')
                if k == "materiale":
                    tot_m += 1
                else:
                    tot_c += 1
        if items:
            rows.append(f'<div class="nb"><p class="cap"><a href="#p-{p["slug"]}">{H.escape(p["label"])}</a>'
                        f'<code>{H.escape(p["url"])}</code></p><ul>{"".join(items)}</ul></div>')
    return tot_m, tot_c, "".join(rows)


# ─────────────────────────────────────────────── documento

tot_blocks = sum(len(p["blocks"]) for p in PAGES)
tot_wait = sum(1 for p in PAGES for _, s, _ in p["blocks"] if s == "cliente")
tot_m, tot_c, needs_html = needs_section()
pages_html = "".join(page_block(p) for p in PAGES)
jump = "".join(f'<a href="#p-{p["slug"]}">{H.escape(p["label"])}</a>' for p in PAGES)

CSS = """
:root{--blu:#003A83;--blu-scuro:#00265a;--blu-chiaro:#CFDDEC;--blu-tenue:#f2f6fb;
  --ink:#16202e;--ink-soft:#4a5768;--line:#dde4ee;--warn:#b26a00;--ok:#1b6b3a;
  --wf:#e9edf3;--wf-line:#c3ccda;--wf-ink:#8d99ab;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:var(--ink);background:#fff;line-height:1.6;font-size:15px}
.shell{max-width:1100px;margin:0 auto;padding:0 26px 90px}
a{color:var(--blu)}
code{font-family:var(--mono);font-size:12px;color:var(--ink-soft)}

/* barra di navigazione del documento */
.upbar{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.95);
  backdrop-filter:saturate(180%) blur(8px);border-bottom:1px solid var(--line);
  margin:0 -26px 0;padding:9px 26px;display:flex;flex-wrap:wrap;gap:7px;align-items:center;font-size:12.3px}
.upbar a{text-decoration:none;color:var(--blu);font-weight:600;padding:3px 10px;
  border:1px solid var(--blu-chiaro);border-radius:20px;background:var(--blu-tenue)}
.upbar a:hover{background:var(--blu);color:#fff;border-color:var(--blu)}
.upbar a.on{background:var(--blu);color:#fff;border-color:var(--blu)}
.upbar .sp{margin-left:auto;color:var(--ink-soft);font-weight:400}

/* scelta fra i due documenti */
.pick{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(290px,1fr))}
.pick a{display:block;border:1px solid var(--line);border-radius:11px;padding:22px;text-decoration:none;
  color:inherit;background:#fff;transition:.16s}
.pick a:hover{border-color:var(--blu);background:var(--blu-tenue);transform:translateY(-2px)}
.pick .n{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--blu);margin:0;text-transform:uppercase}
.pick h3{margin:5px 0 8px;font-size:21px;letter-spacing:-.02em}
.pick p{margin:0 0 12px;font-size:13.8px;color:var(--ink-soft)}
.pick .go{font-size:12.8px;font-weight:700;color:var(--blu);margin:0}

/* copertina */
header.cover{background:linear-gradient(160deg,var(--blu) 0%,var(--blu-scuro) 100%);color:#fff;
  margin:0 -26px 34px;padding:52px 26px 44px;position:relative;overflow:hidden}
header.cover::after{content:"";position:absolute;right:-90px;top:-90px;width:340px;height:340px;
  border:1px solid rgba(255,255,255,.14);border-radius:50%}
header.cover .kick{font-size:11px;text-transform:uppercase;letter-spacing:.18em;font-weight:700;opacity:.75;margin:0}
header.cover h1{font-size:38px;line-height:1.1;letter-spacing:-.03em;margin:10px 0 12px;max-width:24ch}
header.cover p.lead{margin:0;max-width:66ch;font-size:17px;color:#dbe6f5}
.cmeta{display:flex;flex-wrap:wrap;gap:26px;margin-top:28px;position:relative;z-index:1;font-size:12.6px}
.cmeta span{display:block;opacity:.62;text-transform:uppercase;letter-spacing:.1em;font-size:10.5px;margin-bottom:2px}

h2.sec{font-size:12.5px;text-transform:uppercase;letter-spacing:.14em;color:var(--blu);
  margin:52px 0 16px;padding-bottom:8px;border-bottom:1px solid var(--line)}
h2.sec:first-of-type{margin-top:8px}
p.intro{max-width:74ch;color:var(--ink-soft)}

.kpis{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin:0 0 22px}
.kpi{border:1px solid var(--line);border-radius:9px;padding:14px 16px}
.kpi b{display:block;font-size:26px;color:var(--blu);letter-spacing:-.02em;line-height:1.05}
.kpi span{display:block;font-size:12px;color:var(--ink-soft);margin-top:3px}

.tag{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;
  padding:2.5px 9px;border-radius:20px;white-space:nowrap}
.t-ok{background:#e7f4ec;color:var(--ok)}
.t-warn{background:#fff4e0;color:var(--warn)}
.t-off{background:#eef1f5;color:var(--ink-soft)}

.legend{display:flex;flex-wrap:wrap;gap:18px;margin:18px 0 0;font-size:12.6px;color:var(--ink-soft)}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.note{border:1px solid var(--line);border-left:4px solid var(--blu);background:var(--blu-tenue);
  padding:15px 18px;border-radius:0 9px 9px 0;margin:20px 0 0;max-width:80ch}
.note p{margin:0 0 8px}.note p:last-child{margin:0}
.note.warn{border-left-color:var(--warn);background:#fffaf0}

/* alberatura */
.tree{border:1px solid var(--line);border-radius:11px;padding:22px 24px;background:#fff}
.tree ul{list-style:none;margin:0;padding:0}
.tree .lv0{margin-bottom:6px}
.tree .lv1{margin-left:16px;border-left:1px solid var(--blu-chiaro);padding-left:0}
.tree li{position:relative;padding:5px 0 5px 20px}
.tree .lv1 > li::before{content:"";position:absolute;left:0;top:19px;width:14px;height:1px;background:var(--blu-chiaro)}
.tree li.sub{padding:0 0 4px 20px}
.tree li.sub > ul{margin-left:14px;border-left:1px dashed var(--blu-chiaro)}
.tree a,.tree span{display:inline-flex;flex-wrap:wrap;align-items:baseline;gap:9px;text-decoration:none;color:inherit;
  border:1px solid var(--line);border-radius:8px;padding:6px 12px;background:var(--blu-tenue)}
.tree a:hover{border-color:var(--blu);background:#fff}
.tree b{font-size:14px}
.tree .lv0 a{background:var(--blu);color:#fff;border-color:var(--blu)}
.tree .lv0 code{color:#cfe0f6}
.tree em{display:block;font-style:normal;font-size:12.2px;color:var(--ink-soft);margin:4px 0 0 2px;max-width:70ch}

.treeside{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));margin-top:14px}
.ts{border:1px solid var(--line);border-radius:10px;padding:15px 17px;font-size:13.4px;color:var(--ink-soft)}
.ts p{margin:0 0 8px}.ts p:last-child{margin:0}
.cap{font-size:11px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;color:var(--blu)}
.ts .tree{border:0;padding:0}

/* menu di riferimento */
.menustrip{display:flex;flex-wrap:wrap;align-items:center;gap:10px;border:1px solid var(--line);
  border-radius:10px;padding:12px 16px;margin:0 0 16px;background:var(--blu-tenue);font-size:13px}
.menustrip b{color:var(--blu);letter-spacing:.06em}
.menustrip span{background:#fff;border:1px solid var(--line);border-radius:16px;padding:3px 11px}
.menustrip .last{margin-left:auto;color:var(--ink-soft);font-size:12px;background:none;border:0;padding:0}

/* indice delle pagine */
.jump{display:flex;flex-wrap:wrap;gap:7px;margin:0 0 8px}
.jump a{font-size:12.4px;text-decoration:none;color:var(--blu);border:1px solid var(--line);
  border-radius:16px;padding:4px 11px}
.jump a:hover{background:var(--blu-tenue);border-color:var(--blu)}

/* blocco pagina */
.pageblock{margin:34px 0 0;padding-top:26px;border-top:2px solid var(--blu-chiaro);scroll-margin-top:56px}
.phead{display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;justify-content:space-between}
.phead .pk{font-size:10.5px;text-transform:uppercase;letter-spacing:.14em;color:var(--blu);font-weight:700;margin:0}
.phead h3{margin:3px 0 2px;font-size:25px;letter-spacing:-.02em}
.pmeta{display:flex;gap:7px;flex-wrap:wrap}
.ppitch{margin:10px 0 14px;font-size:16px;max-width:74ch}
.pdl{display:grid;grid-template-columns:210px minmax(0,1fr);gap:5px 18px;margin:0 0 20px;font-size:13.4px}
.pdl dt{color:var(--ink-soft);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em}
.pdl dd{margin:0}

/* finestra e sito disegnato */
.screen{border:1px solid var(--wf-line);border-radius:12px;overflow:hidden;background:#fff;
  box-shadow:0 18px 40px -30px rgba(0,40,90,.5)}
.chrome{display:flex;align-items:center;gap:7px;background:#eef1f6;border-bottom:1px solid var(--wf-line);padding:9px 14px}
.chrome i{width:9px;height:9px;border-radius:50%;background:var(--wf-line);display:block}
.chrome code{margin-left:12px;background:#fff;border:1px solid var(--wf-line);border-radius:20px;
  padding:2px 12px;font-size:11.5px;color:var(--wf-ink)}
.site{background:#fff}
.topnav{display:flex;flex-wrap:wrap;align-items:center;gap:12px;padding:14px 22px;border-bottom:1px solid var(--wf-line)}
.topnav b{font-size:15px;letter-spacing:.06em;color:var(--blu)}
.topnav .mn{display:flex;flex-wrap:wrap;gap:9px}
.topnav .mn span{font-size:12.2px;color:var(--wf-ink);background:var(--wf);border-radius:14px;padding:3px 10px}
.topnav .res{margin-left:auto;font-size:11.5px;color:var(--wf-ink)}
.sitefoot{background:#0e1a2b;color:#8ea3bf;padding:18px 22px;font-size:11.8px}

.band{position:relative;padding:24px 22px 22px 22px;border-bottom:1px dashed var(--wf-line)}
.band:last-of-type{border-bottom:0}
.band.tint{background:var(--blu-tenue)}
.band.band-hero{background:linear-gradient(150deg,#f6f9fd,#eaf1f9)}
.band.hl{background:#fff8ec;box-shadow:inset 3px 0 0 var(--warn)}
.band.ctab{background:var(--blu);color:#fff}
.band.ctab .wb{background:#fff;color:var(--blu);border-color:#fff}
.band.ctab .bcap,.band.ctab .blabel .bt{color:#cfe0f6}
.band.ctab .c-lbl,.band.ctab .c-h1{color:#fff}
.band.thx{background:#f4f7fb;border-top:2px solid var(--blu-chiaro);text-align:center}
.band.thx .nar{margin:0 auto}
.band[data-wait="1"]{box-shadow:inset 3px 0 0 var(--warn)}
.band.ctab[data-wait="1"]{box-shadow:inset 3px 0 0 #ffd79a}

.blabel{display:flex;align-items:baseline;gap:9px;margin:0 0 12px}
.blabel .bn{font-family:var(--mono);font-size:10.5px;font-weight:700;color:var(--blu);
  background:#fff;border:1px solid var(--blu-chiaro);border-radius:5px;padding:1px 6px}
.blabel .bt{font-size:11px;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--ink-soft)}
.blabel .bw{font-size:10px;text-transform:uppercase;letter-spacing:.06em;font-weight:700;
  color:var(--warn);background:#fff4e0;border-radius:20px;padding:1.5px 8px}
.bcap{margin:14px 0 0;font-size:11.8px;color:var(--wf-ink);font-style:italic}

/* copy dentro il wireframe */
.binner p{margin:0 0 10px}
.binner ul,.binner ol{margin:0 0 12px;padding-left:20px}
.binner li{margin-bottom:5px}
.nar{max-width:64ch}
.g2{display:grid;gap:22px;grid-template-columns:1.1fr .9fr;align-items:start}
.g3{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));margin:12px 0 0}
.cols2{columns:2;column-gap:34px}
.cols2 p{break-inside:avoid}
.c-h1{font-size:25px;font-weight:700;letter-spacing:-.025em;line-height:1.22;margin:0 0 10px!important;color:var(--blu-scuro)}
.c-sub{font-size:16px;color:var(--ink-soft);max-width:60ch}
.c-lbl{font-size:11px;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--blu);margin:0 0 8px!important}
.c-nums{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));margin:0 0 14px}
.c-nums div{border:1px solid var(--wf-line);border-radius:8px;padding:12px 14px;background:#fff}
.c-nums b{display:block;font-size:26px;color:var(--blu);letter-spacing:-.02em;line-height:1.1}
.c-nums span{display:block;font-size:11.8px;color:var(--ink-soft);margin-top:3px}
.c-cards{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:0 0 14px}
.c-cards > div{border:1px solid var(--wf-line);border-radius:9px;padding:15px 16px;background:#fff}
.c-cards b{display:block;margin-bottom:6px;color:var(--blu-scuro)}
.c-cards p{font-size:13.4px}
ol.c-steps{counter-reset:s;list-style:none;padding:0}
ol.c-steps li{counter-increment:s;position:relative;padding:0 0 12px 40px;margin:0}
ol.c-steps li::before{content:counter(s,decimal-leading-zero);position:absolute;left:0;top:1px;
  font-family:var(--mono);font-size:11.5px;font-weight:700;color:var(--blu);
  background:#fff;border:1px solid var(--blu-chiaro);border-radius:6px;padding:2px 6px}
ol.c-steps i{color:var(--ink-soft);font-style:italic}
ul.c-two{columns:2;column-gap:34px}
ul.c-faq{list-style:none;padding:0}
.acc ul.c-faq li{border:1px solid var(--wf-line);border-radius:8px;background:#fff;padding:11px 38px 11px 14px;
  margin-bottom:7px;position:relative}
.acc ul.c-faq li::after{content:"⌄";position:absolute;right:14px;top:9px;color:var(--wf-ink);font-size:15px}
.wbtns{margin:14px 0 0!important;display:flex;flex-wrap:wrap;gap:9px}
.wb{display:inline-block;background:var(--blu);color:#fff;border:1px solid var(--blu);border-radius:7px;
  padding:8px 15px;font-size:12.8px;font-weight:600}
.wbtns .wb:nth-child(n+2){background:#fff;color:var(--blu)}
.wlink{font-size:12.8px;font-weight:700;color:var(--blu);margin:6px 0 0!important}
.ask{display:inline-block;font-size:11.5px;font-weight:600;color:var(--warn);background:#fff4e0;
  border-radius:5px;padding:1px 7px}

/* segnaposto */
.ph{border:1px dashed var(--wf-line);border-radius:9px;background:repeating-linear-gradient(135deg,
  #f4f6fa 0 9px,#eef1f6 9px 18px);display:flex;align-items:center;justify-content:center;
  color:var(--wf-ink);font-size:11.5px;text-align:center;padding:10px}
.ph-lg{min-height:210px}.ph-md{min-height:150px}.ph-sm{min-height:78px}
.ph-logo{min-height:46px}
.logos{display:grid;gap:10px;grid-template-columns:repeat(auto-fit,minmax(90px,1fr));margin:12px 0 0}
.lgrid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));margin:12px 0 0}
.lg .cap{display:block;margin-bottom:4px}
.cert{border:1px dashed var(--wf-line);border-radius:9px;padding:13px 14px;background:#fff}
.cert i{display:block;height:9px;border-radius:4px;background:var(--wf);margin:8px 0}
.cert i.s{width:55%}
.proj{display:grid;gap:16px;grid-template-columns:.8fr 1.2fr;align-items:center;
  border:1px solid var(--wf-line);border-radius:10px;padding:14px;margin:12px 0 0;background:#fff}
.proj .lines i{display:block;height:9px;border-radius:4px;background:var(--wf);margin:8px 0}
.proj .lines i.s{width:60%}
.fbox{border:1px solid var(--wf-line);border-radius:10px;padding:16px;background:#fff}
.fgrid{display:grid;gap:10px}
.fgrid.c1{grid-template-columns:1fr}
.fgrid.c2{grid-template-columns:1fr 1fr}
.fgrid i{display:block;height:34px;border-radius:7px;background:var(--wf);border:1px solid var(--wf-line)}
.fcheck{display:flex;align-items:center;gap:8px;margin:12px 0;font-size:11.8px;color:var(--wf-ink)}
.fcheck b{width:14px;height:14px;border:1px solid var(--wf-line);border-radius:4px;display:block}

/* richieste al cliente */
.need{border:1px solid #f0d9ae;border-left:4px solid var(--warn);background:#fffaf0;
  border-radius:0 9px 9px 0;padding:12px 15px;margin:16px 0 0}
.need ul{list-style:none;margin:0;padding:0}
.need li{font-size:12.8px;color:#6b4a12;padding:3px 0}
.need b{color:var(--warn);text-transform:uppercase;font-size:10.5px;letter-spacing:.06em}

/* riepilogo richieste */
.nb{border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:0 0 12px}
.nb .cap{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline;margin:0 0 8px}
.nb .cap a{text-decoration:none}
.nb ul{list-style:none;margin:0;padding:0}
.nb li{font-size:13.2px;padding:5px 0;border-top:1px solid var(--line)}
.nb b{font-weight:600}
.k{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;
  border-radius:20px;padding:1.5px 8px;margin-right:8px;vertical-align:1px}
.km{background:#fff4e0;color:var(--warn)}
.kc{background:#eef1f5;color:var(--ink-soft)}

ul.ck{list-style:none;padding:0;max-width:80ch}
ul.ck li{padding:8px 0 8px 28px;border-bottom:1px solid var(--line);position:relative;font-size:14px}
ul.ck li::before{content:"☐";position:absolute;left:2px;color:var(--blu);font-size:16px}

footer.ft{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);font-size:12.2px;color:var(--ink-soft)}
footer.ft p{margin:0 0 6px}

@media (max-width:820px){
  .g2,.proj{grid-template-columns:1fr}
  .cols2,ul.c-two{columns:1}
  .pdl{grid-template-columns:1fr}
}
@media (max-width:640px){
  .shell{padding:0 15px 60px}
  .upbar{margin:0 -15px;padding:9px 15px}
  header.cover{margin:0 -15px 26px;padding:38px 15px 32px}
  header.cover h1{font-size:27px}
  .band{padding:18px 14px}
  .topnav{padding:12px 14px}
}
@media print{.upbar,.jump{display:none}.screen{box-shadow:none}}
"""

# ─────────────────────────────────────────────── guscio comune dei tre documenti

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%23003A83'/%3E%3Ctext x='16' y='22' "
           "font-family='Helvetica,Arial' font-size='16' font-weight='bold' fill='%23fff' "
           "text-anchor='middle'%3ES%3C/text%3E%3C/svg%3E")

NAVLINKS = [("/presentazione", "Copertina"),
            ("/presentazione/struttura", "1 · Struttura del sito"),
            ("/presentazione/pagine", "2 · Le pagine e i contenuti")]


def upbar(current, extra=""):
    out = []
    for href, label in NAVLINKS:
        on = ' class="on"' if href == current else ""
        out.append(f'<a href="{href}"{on}>{label}</a>')
    return (f'<div class="upbar">{"".join(out)}{extra}'
            f'<span class="sp"><a href="/">Documentazione di progetto →</a></span></div>')


def document(fname, title, desc, current, body, extra_nav=""):
    doc = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{FAVICON}">
<style>{CSS}</style>
</head>
<body>
<div class="shell">

{upbar(current, extra_nav)}
{body}

<footer class="ft">
  <p><strong>Sonit Srl · nuovo sito.</strong> Aggiornato al {DATA}. Documento riservato, non indicizzato.</p>
  <p><a href="/presentazione">Copertina</a> · <a href="/presentazione/struttura">Struttura del sito</a> · <a href="/presentazione/pagine">Le pagine e i contenuti</a> · <a href="/">Documentazione tecnica di progetto</a></p>
</footer>

</div>
</body>
</html>
"""
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(doc)


NO_GRAFICA = """<div class="note">
  <p><strong>Cosa non c'è, di proposito.</strong> Questi documenti non contengono la grafica. Il carattere, i colori pieni, le fotografie e lo stile dei pulsanti si decidono dopo, sulla struttura approvata: è l'ordine che costa meno, perché spostare una sezione ora è un minuto, spostarla a sito fatto è un giorno.</p>
</div>"""

os.makedirs(OUT, exist_ok=True)

# ─────────────────────────────────────────────── 0 · copertina

cover = f"""<header class="cover">
  <p class="kick">Sonit Srl · nuovo sito · proposta</p>
  <h1>Come sarà fatto il nuovo sito</h1>
  <p class="lead">Due documenti da leggere in quest'ordine: prima la struttura, cioè quali pagine esistono e come si raggiungono; poi il contenuto di ogni pagina, con lo schema di come sarà organizzata e i testi che proponiamo di scriverci dentro.</p>
  <div class="cmeta">
    <div><span>Pagine</span>{len(PAGES)}, di cui 9 pubbliche al lancio</div>
    <div><span>Sezioni</span>{tot_blocks}</div>
    <div><span>Testi pronti</span>{tot_blocks - tot_wait} su {tot_blocks}</div>
    <div><span>Aggiornato al</span>{DATA}</div>
  </div>
</header>

<h2 class="sec" id="documenti">I due documenti</h2>
<div class="pick">
  <a href="/presentazione/struttura">
    <p class="n">Documento 1</p>
    <h3>La struttura del sito</h3>
    <p>Quali pagine esistono, come sono annidate, cosa entra nel menu e cosa no. Il percorso dei privati per il fotovoltaico è tenuto separato: qui si vede dove e perché.</p>
    <p class="go">Apri la struttura →</p>
  </a>
  <a href="/presentazione/pagine">
    <p class="n">Documento 2</p>
    <h3>Le pagine e i contenuti</h3>
    <p>Per ognuna delle {len(PAGES)} pagine: a cosa serve, lo schema delle sezioni nell'ordine in cui si incontrano e i testi proposti dentro ogni blocco. In chiusura, cosa ci serve da voi.</p>
    <p class="go">Apri le pagine →</p>
  </a>
</div>

<h2 class="sec" id="approvazione">Cosa vi chiediamo</h2>
<p class="intro">Quattro risposte, in questo ordine. Non serve un documento: bastano note a margine o una chiamata.</p>
<ul class="ck">
  <li><b>La struttura va bene?</b> Numero di pagine, voci di menu, il fotovoltaico per i privati tenuto separato dal resto. → <a href="/presentazione/struttura">documento 1</a></li>
  <li><b>L'ordine delle sezioni di ogni pagina è quello giusto?</b> In particolare la home: cosa vedono prima i vostri clienti. → <a href="/presentazione/pagine">documento 2</a></li>
  <li><b>I testi dicono cose vere e dicono le cose giuste?</b> Segnalate ciò che va corretto, tolto o detto in modo diverso: è il momento in cui costa meno.</li>
  <li><b>I materiali che ci servono:</b> chi li recupera e in che tempi. Sono {tot_m} documenti da reperire e {tot_c} dati da confermare, elencati <a href="/presentazione/pagine#serve">in fondo al documento 2</a>.</li>
</ul>

{NO_GRAFICA}

<div class="note">
  <p><strong>Poi si passa alla grafica.</strong> Con la struttura e i testi approvati prepariamo due proposte di direzione visiva sul blu del vostro marchio, scegliete quella che vi rappresenta e da lì disegniamo tutte le pagine.</p>
</div>"""

document("index.html", "Sonit · Il nuovo sito: struttura e contenuti",
         "Proposta per il nuovo sito Sonit Srl: struttura delle pagine e contenuti, in due documenti.",
         "/presentazione", cover)

# ─────────────────────────────────────────────── 1 · struttura

rows = "".join(
 f'<tr><td><a href="/presentazione/pagine#p-{p["slug"]}">{H.escape(p["label"])}</a>'
 + (' <span class="tag t-off">fuori dal menu</span>' if p["slug"] in OFF_MENU else "")
 + f'</td><td><code>{H.escape(p["url"])}</code></td>'
 f'<td>{H.escape(PITCH.get(p["slug"], p["goal"]))}</td></tr>' for p in PAGES)

struct = f"""<header class="cover">
  <p class="kick">Sonit Srl · nuovo sito · documento 1 di 2</p>
  <h1>La struttura del sito</h1>
  <p class="lead">Nove pagine pubbliche al lancio, sei voci di menu, un solo livello di sottomenu sotto Soluzioni. Poche pagine, ognuna con un compito preciso: è la richiesta emersa in avvio di progetto.</p>
  <div class="cmeta">
    <div><span>Pagine al lancio</span>9, più il percorso privati</div>
    <div><span>Voci di menu</span>6</div>
    <div><span>Livelli</span>2 al massimo</div>
    <div><span>Aggiornato al</span>{DATA}</div>
  </div>
</header>

<h2 class="sec" id="menu">Il menu</h2>
<p class="intro">Sei voci, sempre le stesse su tutte le pagine. Il telefono e l'accesso all'area riservata restano a destra, fuori dal percorso commerciale.</p>
<div class="menustrip">
  <b>SONIT</b>{''.join(f'<span>{m}</span>' for m in MENU)}
  <span class="last">+39 0776 868072 · Area riservata</span>
</div>

<h2 class="sec" id="albero">L'albero delle pagine</h2>
<p class="intro">Ogni riquadro è una pagina: cliccandolo si apre il suo contenuto nel documento 2. Sotto Soluzioni stanno le tre aree di attività, allo stesso livello fra loro.</p>
{tree()}

<h2 class="sec" id="elenco">Le pagine e a cosa servono</h2>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Pagina</th><th>Indirizzo</th><th>A cosa serve</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
</div>

<h2 class="sec" id="cambia">Cosa cambia rispetto al sito di oggi</h2>
<ul class="ck">
  <li><b>Le tre aree di attività hanno una pagina ciascuna.</b> Oggi il fotovoltaico è una voce di elenco dentro "Impianti e Sistemi" e le voci di menu non corrispondono a come lavorate.</li>
  <li><b>Certificazioni, partner e progetti diventano pagine.</b> Oggi non esistono: sono le prove che un committente strutturato cerca prima di chiamarvi.</li>
  <li><b>"Lavori" non porta più a una pagina vuota.</b> Diventa Progetti, con i lavori raccontati come casi.</li>
  <li><b>I privati hanno un percorso proprio.</b> Non attraversano i contenuti industriali e non li disturbano.</li>
  <li><b>Privacy e cookie policy tornano sul vostro dominio.</b> Oggi l'unica informativa è su un sito di terzi.</li>
</ul>

<div class="note">
  <p><strong>La domanda di questo documento.</strong> La struttura va bene? Numero di pagine, voci di menu, il fotovoltaico per i privati tenuto separato dal resto. Se qui è tutto d'accordo, il passo successivo è il contenuto di ogni pagina: <a href="/presentazione/pagine">documento 2</a>.</p>
</div>"""

document("struttura.html", "Sonit · La struttura del nuovo sito",
         "Alberatura semplificata del nuovo sito Sonit Srl: pagine, menu e percorsi.",
         "/presentazione/struttura", struct)

# ─────────────────────────────────────────────── 2 · pagine e contenuti

pag = f"""<header class="cover">
  <p class="kick">Sonit Srl · nuovo sito · documento 2 di 2</p>
  <h1>Le pagine e i contenuti</h1>
  <p class="lead">Per ognuna delle {len(PAGES)} pagine: a cosa serve, lo schema delle sezioni nell'ordine in cui si incontrano scorrendo e i testi che proponiamo di scriverci dentro. La struttura complessiva è nel <a href="/presentazione/struttura" style="color:#fff">documento 1</a>.</p>
  <div class="cmeta">
    <div><span>Pagine</span>{len(PAGES)}</div>
    <div><span>Sezioni</span>{tot_blocks}</div>
    <div><span>Testi pronti</span>{tot_blocks - tot_wait} su {tot_blocks}</div>
    <div><span>In attesa di materiali</span>{tot_wait}</div>
  </div>
</header>

<h2 class="sec" id="come">Come si legge</h2>
<p class="intro">Ogni pagina è disegnata come una finestra di browser: le sezioni sono nell'ordine in cui si incontrano scorrendo, con i testi reali dentro. I rettangoli tratteggiati sono gli spazi dove andranno immagini, loghi, mappa o schede: il contenuto arriva dopo, la posizione è quella. I riquadri arancioni segnalano le sezioni che non possiamo completare senza materiali vostri.</p>

<div class="legend">
  <span><i style="background:#e9edf3;border:1px dashed #c3ccda"></i>spazio per immagini, loghi, mappa o schede</span>
  <span><i style="background:#fff4e0;border:1px solid #f0d9ae"></i>sezione in attesa di materiali vostri</span>
  <span><i style="background:#003A83"></i>pulsanti e azioni</span>
</div>

{NO_GRAFICA}

<h2 class="sec" id="pagine">Le pagine, una per una</h2>
<div class="jump">{jump}</div>

{pages_html}

<h2 class="sec" id="serve">Cosa serve da voi</h2>
<p class="intro">{tot_m} documenti da reperire e {tot_c} dati da confermare. Sono elencati sotto la pagina che sbloccano: ogni voce che arriva chiude una sezione oggi segnata in arancione. Le sezioni si possono comunque approvare prima: cambia cosa ci sta dentro, non dove sta.</p>
{needs_html}

<div class="note">
  <p><strong>Le domande di questo documento.</strong> L'ordine delle sezioni è quello giusto, a partire dalla home? I testi dicono cose vere e nel modo in cui le direste voi? Segnalate ciò che va corretto, tolto o detto diversamente: ora costa un minuto.</p>
</div>"""

document("pagine.html", "Sonit · Le pagine del nuovo sito e i contenuti",
         "Schema di ogni pagina del nuovo sito Sonit Srl con i contenuti proposti.",
         "/presentazione/pagine", pag)

print(f"presentazione: index.html · struttura.html · pagine.html — {len(PAGES)} pagine · "
      f"{tot_blocks} sezioni · {tot_wait} in attesa · richieste: {tot_m} materiali, {tot_c} conferme")
