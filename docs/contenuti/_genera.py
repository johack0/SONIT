# Rigenera i file di contenuto: python3 docs/contenuti/_genera.py
# I testi stanno in _sorgente_testi.py — si modificano lì, non nei file HTML.
# -*- coding: utf-8 -*-
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sorgente_testi import PAGES

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")
os.makedirs(OUT, exist_ok=True)

SRC_LABEL = {
 "riuso":  ("Riuso dal sito attuale", "s-riuso"),
 "nuovo":  ("Testo nuovo", "s-nuovo"),
 "cliente":("Serve materiale dal cliente", "s-cli"),
}

CSS = """
  :root{--blu:#003A83;--blu-scuro:#00265a;--blu-chiaro:#CFDDEC;--blu-tenue:#f2f6fb;
    --ink:#16202e;--ink-soft:#4a5768;--line:#dde4ee;--crit:#b3261e;--warn:#b26a00;--ok:#1b6b3a;
    --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    color:var(--ink);background:#fff;line-height:1.6;font-size:15px}
  .shell{max-width:980px;margin:0 auto;padding:0 26px 80px}
  .upbar{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.94);backdrop-filter:saturate(180%) blur(8px);
    border-bottom:1px solid var(--line);margin:0 -26px 24px;padding:11px 26px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:12.5px}
  .upbar a{display:inline-flex;text-decoration:none;color:var(--blu);font-weight:600;padding:4px 10px;
    border:1px solid var(--blu-chiaro);border-radius:20px;background:var(--blu-tenue)}
  .upbar a:hover{background:var(--blu);color:#fff;border-color:var(--blu)}
  .upbar span{color:var(--ink-soft)}
  header.hd{padding:22px 0 20px;border-bottom:3px solid var(--blu);margin-bottom:26px}
  header.hd .kick{font-size:11px;text-transform:uppercase;letter-spacing:.16em;color:var(--blu);font-weight:700}
  header.hd h1{font-size:30px;margin:8px 0 6px;letter-spacing:-.02em}
  header.hd .url{font-family:var(--mono);font-size:12.5px;color:var(--ink-soft)}
  dl.meta{display:grid;grid-template-columns:150px minmax(0,1fr);gap:6px 16px;margin:18px 0 0;font-size:13.5px}
  dl.meta dt{color:var(--ink-soft);font-size:12px;text-transform:uppercase;letter-spacing:.05em}
  dl.meta dd{margin:0}
  h2.sec{font-size:12.5px;text-transform:uppercase;letter-spacing:.13em;color:var(--blu);margin:38px 0 14px;
    padding-bottom:8px;border-bottom:1px solid var(--line)}
  .blk{border:1px solid var(--line);border-radius:10px;margin:0 0 16px;overflow:hidden}
  .blk > .bh{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:var(--blu-tenue);
    padding:9px 16px;border-bottom:1px solid var(--line)}
  .blk > .bh b{font-size:13.5px}
  .blk > .bh .n{font-family:var(--mono);font-size:11px;color:var(--blu);font-weight:700}
  .blk > .bh .src{margin-left:auto;font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;
    padding:2px 9px;border-radius:20px;white-space:nowrap}
  .s-riuso{background:#e7f4ec;color:var(--ok)}
  .s-nuovo{background:#e8f0fe;color:#0b5ed7}
  .s-cli{background:#fff4e0;color:var(--warn)}
  .blk > .bd{padding:18px 20px}
  .blk p{margin:0 0 11px}
  .c-h1{font-size:24px;font-weight:700;letter-spacing:-.02em;line-height:1.25;margin:0 0 10px!important;color:var(--blu-scuro)}
  .c-sub{font-size:16.5px;color:var(--ink-soft);max-width:64ch}
  .c-lbl{font-size:11.5px;text-transform:uppercase;letter-spacing:.1em;font-weight:700;color:var(--blu);margin:0 0 8px!important}
  .c-btn{margin-top:14px!important;font-family:var(--mono);font-size:12.2px;color:var(--blu-scuro);background:var(--blu-tenue);
    border:1px dashed var(--blu-chiaro);border-radius:7px;padding:9px 12px}
  .c-note{margin:14px 0 0!important;font-size:12.4px;color:var(--ink-soft);border-top:1px dotted var(--line);padding-top:10px}
  .c-note code{font-family:var(--mono);font-size:11.8px}
  .c-link{font-size:13px;font-weight:700;color:var(--blu);margin:0!important}
  ul,ol{margin:0 0 12px;padding-left:20px}
  li{margin-bottom:5px}
  ul.c-two{columns:2;column-gap:34px}
  @media (max-width:620px){ul.c-two{columns:1}}
  ol.c-steps{padding-left:20px}
  ol.c-steps li{margin-bottom:9px}
  ol.c-steps i{color:var(--ink-soft);font-style:italic}
  ul.c-faq{list-style:none;padding:0}
  ul.c-faq li{padding:9px 0;border-bottom:1px solid var(--line)}
  .c-nums{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin:0 0 14px}
  .c-nums div{border:1px solid var(--line);border-radius:8px;padding:12px 14px}
  .c-nums b{display:block;font-size:24px;color:var(--blu);letter-spacing:-.02em;line-height:1.1}
  .c-nums span{display:block;font-size:12px;color:var(--ink-soft);margin-top:3px}
  .c-cards{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));margin:0 0 14px}
  .c-cards > div{border:1px solid var(--line);border-radius:8px;padding:14px 16px}
  .c-cards b{display:block;margin-bottom:6px;color:var(--blu-scuro)}
  .c-cards p{font-size:13.6px}
  .todo,.cli{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.04em;padding:2px 8px;border-radius:5px}
  .todo{background:#fdecea;color:var(--crit)}
  .cli{background:#fff4e0;color:var(--warn)}
  code{font-family:var(--mono);font-size:12.2px;background:var(--blu-tenue);padding:1.5px 5px;border-radius:4px;color:var(--blu-scuro)}
  .pager{display:flex;flex-wrap:wrap;gap:6px;margin:34px 0 0;padding-top:18px;border-top:1px solid var(--line)}
  .pager a{font-size:12.4px;text-decoration:none;color:var(--blu);border:1px solid var(--line);border-radius:16px;padding:4px 10px}
  .pager a:hover{background:var(--blu-tenue)}
  .pager a.on{background:var(--blu);color:#fff;border-color:var(--blu);font-weight:700}
  footer.ft{margin-top:32px;padding-top:16px;border-top:1px solid var(--line);font-size:11.8px;color:var(--ink-soft)}
  .tbl-wrap{overflow-x:auto}
  table{border-collapse:collapse;width:100%;font-size:13.2px;min-width:560px}
  th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
  thead th{background:var(--blu-tenue);color:var(--blu-scuro);font-size:11.5px;text-transform:uppercase;letter-spacing:.06em}
  .cards{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));margin:0 0 20px}
  a.pg{display:block;border:1px solid var(--line);border-radius:9px;padding:14px 16px;text-decoration:none;color:inherit;transition:.15s}
  a.pg:hover{border-color:var(--blu);background:var(--blu-tenue)}
  a.pg b{display:block;font-size:15px}
  a.pg code{background:none;padding:0;font-size:11.5px;color:var(--ink-soft)}
  a.pg .st{display:block;margin-top:7px;font-size:11.5px;color:var(--ink-soft)}
  .bar{display:flex;height:8px;border-radius:5px;overflow:hidden;margin:4px 0 0;border:1px solid var(--line)}
  .bar i{display:block}
  @media (max-width:640px){.shell{padding:0 16px 60px}.upbar{margin:0 -16px 18px;padding:10px 16px}
    header.hd h1{font-size:23px}dl.meta{grid-template-columns:1fr}}
  @media print{.upbar,.pager{display:none}}
"""

def words(html_txt):
    t = re.sub(r'(?s)<p class="c-note">.*?</p>', ' ', html_txt)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"DA CONFERMARE ·[^<]*", " ", t)
    t = re.sub(r"DA MATERIALI CLIENTE ·[^<]*", " ", t)
    return len(t.split())

NAV = [(p["slug"], p["label"]) for p in PAGES]

def pager(cur):
    out = ['<a href="/docs/contenuti/">Panoramica</a>']
    for s, l in NAV:
        out.append(f'<a class="{"on" if s==cur else ""}" href="/docs/contenuti/{s}">{H.escape(l)}</a>')
    return "".join(out)

tot_words = 0
stats = []

for p in PAGES:
    blocks_html = []
    pw = 0
    counts = {"riuso": 0, "nuovo": 0, "cliente": 0}
    for i, (name, src, copy) in enumerate(p["blocks"], 1):
        lab, cls = SRC_LABEL[src]
        w = words(copy)
        pw += w
        counts[src] += 1
        blocks_html.append(f"""<div class="blk">
  <div class="bh"><span class="n">{i:02d}</span><b>{H.escape(name)}</b><span class="src {cls}">{lab}</span></div>
  <div class="bd">{copy.strip()}</div>
</div>""")
    tot_words += pw
    stats.append((p, pw, counts))

    doc = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contenuti · {H.escape(p['label'])} · {p['url']}</title>
<meta name="robots" content="noindex, nofollow">
<style>{CSS}</style>
</head>
<body>
<div class="shell">

<div class="upbar">
  <a href="/">← Indice dei documenti</a>
  <a href="/docs/contenuti/">← Panoramica contenuti</a>
  <a href="/docs/architettura-informazioni#albero">Alberatura · nodo</a>
  <span>Contenuti · {H.escape(p['label'])}</span>
</div>

<header class="hd">
  <p class="kick">Sonit · contenuti del nuovo sito · fase F3</p>
  <h1>{H.escape(p['label'])}</h1>
  <p class="url">{p['url']}</p>
  <dl class="meta">
    <dt>Obiettivo</dt><dd>{H.escape(p['goal'])}</dd>
    <dt>Pubblico</dt><dd>{H.escape(p['audience'])}</dd>
    <dt>Azione attesa</dt><dd>{H.escape(p['cta'])}</dd>
    <dt>Title tag</dt><dd><code>{H.escape(p['title'])}</code> <span style="color:var(--ink-soft)">· {len(p['title'])} caratteri</span></dd>
    <dt>Meta description</dt><dd><code>{H.escape(p['desc'])}</code> <span style="color:var(--ink-soft)">· {len(p['desc'])} caratteri</span></dd>
    <dt>H1</dt><dd>{H.escape(p['h1'])}</dd>
    <dt>Parole di copy</dt><dd>~{pw} · {len(p['blocks'])} blocchi</dd>
  </dl>
</header>

<h2 class="sec">Contenuti, blocco per blocco</h2>
{chr(10).join(blocks_html)}

<div class="pager">{pager(p['slug'])}</div>

<footer class="ft">
  <p>SONIT · Progetto DXP — contenuti riscritti per <code>{p['url']}</code>, fase F3. Le etichette <span class="todo">DA CONFERMARE</span> e <span class="cli">DA MATERIALI CLIENTE</span> segnalano ciò che non è ancora scrivibile in via definitiva.</p>
  <p><a href="/">Indice dei documenti</a> · <a href="/docs/contenuti/">Panoramica contenuti</a> · <a href="/docs/architettura-informazioni">Doc 03 · Architettura</a> · <a href="/docs/alberatura-attuale#schede">Testi del sito attuale</a></p>
</footer>

</div>
</body>
</html>
"""
    open(OUT + p["slug"] + ".html", "w", encoding="utf-8").write(doc)

# ─────────────────────────── PANORAMICA (Doc 04)
tot_blocks = sum(len(p["blocks"]) for p in PAGES)
c_riuso = sum(c["riuso"] for _, _, c in stats)
c_nuovo = sum(c["nuovo"] for _, _, c in stats)
c_cli   = sum(c["cliente"] for _, _, c in stats)

cards = []
for p, pw, c in stats:
    tot = len(p["blocks"])
    w_r = round(c["riuso"] / tot * 100)
    w_n = round(c["nuovo"] / tot * 100)
    w_c = 100 - w_r - w_n
    blocked = " · " + f'<span style="color:var(--warn);font-weight:700">{c["cliente"]} blocchi in attesa</span>' if c["cliente"] else ""
    cards.append(f"""<a class="pg" href="/docs/contenuti/{p['slug']}">
  <b>{H.escape(p['label'])}</b><code>{p['url']}</code>
  <div class="bar"><i style="width:{w_r}%;background:#1b6b3a"></i><i style="width:{w_n}%;background:#0b5ed7"></i><i style="width:{w_c}%;background:#e0b46a"></i></div>
  <span class="st">~{pw} parole · {tot} blocchi{blocked}</span>
</a>""")

rows = "".join(
 f'<tr><td><a href="/docs/contenuti/{p["slug"]}">{H.escape(p["label"])}</a></td><td><code>{p["url"]}</code></td>'
 f'<td class="num">~{pw}</td><td class="num">{c["riuso"]}</td><td class="num">{c["nuovo"]}</td>'
 f'<td class="num">{c["cliente"]}</td></tr>'
 for p, pw, c in stats)

panor = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SONIT — Contenuti del nuovo sito, pagina per pagina</title>
<meta name="robots" content="noindex, nofollow">
<style>{CSS}
  .num{{text-align:right;font-family:var(--mono);font-size:12.2px;white-space:nowrap}}
  .legend{{display:flex;flex-wrap:wrap;gap:16px;margin:0 0 20px;font-size:12.4px;color:var(--ink-soft)}}
  .legend i{{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:6px;vertical-align:-1px}}
  .box{{border:1px solid var(--line);border-left:4px solid var(--blu);background:var(--blu-tenue);
    padding:14px 16px;border-radius:0 8px 8px 0;margin:0 0 18px;font-size:14px}}
  .box.warn{{border-left-color:var(--warn);background:#fffaf0}}
  .box p:last-child{{margin-bottom:0}}
  .kpis{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));margin:0 0 22px}}
  .kpi{{border:1px solid var(--line);border-radius:9px;padding:14px 16px}}
  .kpi b{{display:block;font-size:25px;color:var(--blu);line-height:1.05;letter-spacing:-.02em}}
  .kpi span{{display:block;font-size:12px;color:var(--ink-soft);margin-top:4px}}
</style>
</head>
<body>
<div class="shell">

<div class="upbar">
  <a href="/">← Indice dei documenti</a>
  <a href="/docs/architettura-informazioni">← Doc 03 · Architettura</a>
  <span>Stai leggendo: Doc 04 · Contenuti del nuovo sito</span>
</div>

<header class="hd">
  <p class="kick">Progetto DXP · Documento 04 · Fase F3</p>
  <h1>Contenuti del nuovo sito, pagina per pagina</h1>
  <p class="url">Un file per ogni nodo dell'alberatura validata · {tot_blocks} blocchi di copy · ~{tot_words} parole</p>
</header>

<div class="kpis">
  <div class="kpi"><b>{len(PAGES)}</b><span>pagine con contenuti scritti</span></div>
  <div class="kpi"><b>{tot_blocks}</b><span>blocchi di copy</span></div>
  <div class="kpi"><b>~{tot_words}</b><span>parole, contro ~1.100 del sito attuale</span></div>
  <div class="kpi"><b>{c_riuso}</b><span>blocchi da riuso del sito attuale</span></div>
  <div class="kpi"><b>{c_nuovo}</b><span>blocchi di testo nuovo, pronti</span></div>
  <div class="kpi"><b>{c_cli}</b><span>blocchi in attesa di materiali</span></div>
</div>

<h2 class="sec">Come leggere questi file</h2>
<p>Ogni pagina della nuova alberatura ha un file con i suoi contenuti pronti, divisi nei blocchi in cui compaiono scorrendo la pagina. Per ogni blocco è indicata la provenienza: <b>riuso</b> dal sito attuale, <b>testo nuovo</b> già scritto, oppure <b>in attesa di materiali</b> dal cliente. Ogni file riporta anche il <code>title</code>, la <code>meta description</code> e l'H1 proposti, con il conteggio dei caratteri.</p>
<p>Due etichette segnalano ciò che non è ancora definitivo: <span class="todo">DA CONFERMARE</span> per i dati da validare con il cliente e <span class="cli">DA MATERIALI CLIENTE</span> per i blocchi che non si possono scrivere senza documenti.</p>

<div class="legend">
  <span><i style="background:#1b6b3a"></i>riuso dal sito attuale</span>
  <span><i style="background:#0b5ed7"></i>testo nuovo, pronto</span>
  <span><i style="background:#e0b46a"></i>in attesa di materiali dal cliente</span>
</div>

<h2 class="sec">Le pagine</h2>
<div class="cards">{"".join(cards)}</div>

<h2 class="sec">Riepilogo</h2>
<div class="tbl-wrap">
<table>
  <thead><tr><th>Pagina</th><th>URL</th><th class="num">Parole</th><th class="num">Riuso</th><th class="num">Nuovi</th><th class="num">In attesa</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
</div>

<div class="box warn">
  <p><strong>Cosa blocca la chiusura della fase F3.</strong> {c_cli} blocchi su {tot_blocks} non si possono chiudere senza materiali del cliente, e sono concentrati esattamente dove serve la prova: certificazioni, partner, progetti, numeri aziendali, taglie degli impianti e caselle email di destinazione. Le pagine a riuso alto — telecomunicazioni, impianti, fotovoltaico B2B, hub soluzioni — sono invece complete e possono andare direttamente in wireframe.</p>
</div>

<h2 class="sec">Regole redazionali usate</h2>
<ul>
  <li><b>Frasi corte, verbi concreti.</b> Si dice cosa si fa e cosa ne ottiene il committente, senza aggettivi di rinforzo.</li>
  <li><b>Nessuna promessa non verificabile.</b> Ogni affermazione di solidità è accompagnata da un dato o da una certificazione.</li>
  <li><b>Termini tecnici mantenuti</b> dove sono il linguaggio del committente: minitrincea, microtrincea, blowing, as-built, giunzione a caldo, collaudo strumentale.</li>
  <li><b>Refusi del sito attuale corretti</b>: "efficientamento" con la i, "intraprendenti", "soluzioni innovative".</li>
  <li><b>Niente "azienda giovane"</b> né "di recente costituzione": contraddicono il posizionamento.</li>
  <li><b>L'etichetta "general contractor" non compare</b> nei testi pubblici, per la decisione D-04: si descrive la capacità di regia.</li>
  <li><b>Committenti non nominati</b> finché non arriva l'autorizzazione.</li>
  <li><b>Title tag</b> entro 60–70 caratteri, con il riferimento territoriale dove è utile; <b>meta description</b> entro 150–160.</li>
</ul>

<div class="box">
  <p><strong>Passo successivo.</strong> Con questi contenuti si costruiscono i wireframe strutturali a bassa fedeltà (W-013): ogni blocco elencato qui diventa una sezione del wireframe, nello stesso ordine. In parallelo si sollecitano i materiali mancanti, che sono l'unica dipendenza rimasta.</p>
</div>

<footer class="ft">
  <p><strong>SONIT · Progetto DXP — Documento 04: contenuti del nuovo sito.</strong> Versione 1.0 del 05/08/2026. Costruito sull'alberatura validata del <a href="/docs/architettura-informazioni">Documento 03</a> e sui testi estratti dal sito attuale raccolti nel <a href="/docs/alberatura-attuale#schede">Documento 02</a>.</p>
  <p><a href="/">Indice dei documenti</a> · <a href="/docs/architettura-informazioni">Architettura</a> · <a href="/docs/alberatura-attuale">Alberatura attuale</a> · <a href="/docs/stato-arte-sonit">Stato dell'arte</a></p>
</footer>

</div>
</body>
</html>
"""
open(OUT + "index.html", "w", encoding="utf-8").write(panor)
print(f"pagine: {len(PAGES)} · blocchi: {tot_blocks} · parole: ~{tot_words}")
print(f"riuso {c_riuso} · nuovi {c_nuovo} · in attesa {c_cli}")
for p, pw, c in stats:
    print(f"  {p['slug']:20s} {pw:5d} parole  {len(p['blocks'])} blocchi  (riuso {c['riuso']}, nuovo {c['nuovo']}, cliente {c['cliente']})")
