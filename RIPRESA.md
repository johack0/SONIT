# Punto di ripresa — SONIT · Progetto DXP

Documento da leggere **per primo** quando si riprende il lavoro dopo l'approvazione dei contenuti.
Ultimo aggiornamento: **17/08/2026**

---

## In una pagina

Struttura del nuovo sito **decisa e validata**, contenuti delle 11 pagine **scritti**, piano dei wireframe **pronto**,
versione da mostrare al cliente **pubblicata** su [`/presentazione`](https://sonit-jhkstudio.vercel.app/presentazione): alberatura semplificata e wireframe a blocchi con i contenuti dentro.
Il lavoro è fermo in attesa di due cose, indipendenti tra loro:

1. **Approvazione dei contenuti** da parte di Giorgio — sblocca i wireframe.
2. **Materiali del cliente** sul Drive condiviso — sbloccano 19 blocchi di contenuto su 67.

I wireframe si possono iniziare con la sola approvazione: la struttura delle sezioni non cambia con i materiali, cambia solo cosa ci sta dentro.

**Prossimo deliverable:** wireframe strutturali low fidelity, secondo l'ordine di produzione del [Doc 05](https://sonit-jhkstudio.vercel.app/docs/piano-wireframe#ordine).

---

## Primi cinque passi al rientro

1. **Leggere [`WORKLOG.md`](WORKLOG.md)** — fasi, attività con stato, decisioni chiuse, materiali attesi, diario. È il punto di verità.
2. **Verificare cosa è arrivato dal cliente** sul Drive condiviso e aggiornare le voci `A-01 → A-13` del worklog. Ogni materiale che arriva chiude uno o più blocchi segnaposto del Doc 04.
3. **Registrare l'approvazione** nel diario di `WORKLOG.md` e nel Doc 01: cosa è stato approvato, cosa è stato chiesto di cambiare, da chi e quando.
4. **Applicare le modifiche ai testi**, se ce ne sono: si modifica `docs/contenuti/_sorgente_testi.py` e si rigenera con `python3 docs/contenuti/_genera.py`. **Non** si editano i singoli HTML: la rigenerazione li sovrascrive.
5. **Partire dai wireframe** dall'impalcatura (header, footer, griglia, componenti ricorrenti) e poi dalla home, seguendo l'ordine del Doc 05.

---

## Stato per fase

| Fase | Deliverable | Stato |
|---|---|---|
| F0 | Kick-off, obiettivi, governance | ✅ 28/07/2026 |
| F1 | Stato dell'arte, alberatura attuale, testi estratti | ✅ 05/08/2026 |
| F2 | Architettura delle informazioni + 7 decisioni validate | ✅ 05/08/2026 |
| F3 | Contenuti: 11 pagine, 67 blocchi | 🔵 scritti, in attesa di approvazione |
| F3 | Wireframe low fidelity | 🔵 prima passata disegnata nella versione cliente, da rifinire dopo approvazione |
| F3 | Versione cliente (alberatura + wireframe + contenuti) | ✅ 17/08/2026, da presentare |
| F4 | Due proposte di direzione visiva | ⬜ |
| F5 | Design completo di tutte le pagine | ⬜ |
| F6 | Sviluppo | ⬜ |
| F7 | Go-live, redirect, analytics, collaudo | ⬜ |

---

## Cosa è già deciso e non va rimesso in discussione

Le sette decisioni di struttura sono state validate il 05/08/2026. Dettaglio in [`WORKLOG.md`](WORKLOG.md) e nel [Doc 03](https://sonit-jhkstudio.vercel.app/docs/architettura-informazioni#decisioni).

| # | Decisione |
|---|---|
| D-01 | Il B2C fotovoltaico vive su `/fotovoltaico-casa`, pagina autonoma **fuori dal menu** |
| D-02 | La consulenza è un **blocco trasversale**, ancora `/soluzioni#consulenza` |
| D-03 | Menu a **6 voci**: Chi siamo · Soluzioni · Certificazioni · Partner · Progetti · Contatti. Sottomenu solo su Soluzioni |
| D-04 | L'hero **descrive la capacità**, non usa l'etichetta "general contractor" |
| D-05 | I **numeri aziendali si pubblicano**, in home e in Chi siamo |
| D-06 | "Lavora con noi" è **predisposta ma non pubblicata** al lancio |
| D-07 | L'area riservata è un **link in header**; nessun form di login nelle pagine pubbliche |

Altri vincoli fissi, dal kick-off: brand e marchio **invariati**; **nessuna foto reale** di cantieri o mezzi; palette sui toni del blu, `#003A83`; poche pagine ben organizzate; nessuna integrazione tra form e gestionali.

---

## Alberatura approvata

```
/                                  Home
├─ /chi-siamo                      + download brochure e company profile PDF
├─ /soluzioni                      hub: ecosistema integrato, metodo, consulenza
│   ├─ /soluzioni/telecomunicazioni
│   ├─ /soluzioni/impianti         civili e industriali
│   └─ /soluzioni/fotovoltaico     B2B
│        └─ /fotovoltaico-casa      percorso B2C, fuori dal menu
├─ /certificazioni
├─ /partner
├─ /progetti
└─ /contatti                       + /grazie

fuori dal menu: /privacy-policy · /cookie-policy · area riservata (app.sonit.it)
predisposte, non pubblicate: /it-cybersecurity (2027) · /lavora-con-noi
```

---

## Cosa serve dal cliente

Ogni voce chiude uno o più blocchi segnaposto. Elenco completo con codici in [`WORKLOG.md`](WORKLOG.md).

| Priorità | Materiale | Sblocca |
|---|---|---|
| 🔴 | Elenco certificazioni con enti ed estremi | `/certificazioni` (3 blocchi), richiami nelle pagine BU, blocco home |
| 🔴 | Numeri aggiornati di organico e struttura | blocco numeri in home, Chi siamo |
| 🔴 | Brochure e company profile PDF definitivi | download in `/chi-siamo` |
| 🔴 | Partner e fornitori pubblicabili, con loghi e autorizzazione | `/partner`, striscia loghi in home |
| 🔴 | 3–5 progetti candidabili a case study | `/progetti`, progetto in evidenza in home, richiami nelle pagine BU |
| 🟠 | Committenti nominabili sul sito | `/partner`, `/progetti` |
| 🟠 | Taglie tipiche degli impianti fotovoltaici B2B e residenziali | `/soluzioni/fotovoltaico`, `/fotovoltaico-casa` |
| 🟠 | Caselle email distinte per richieste B2B e privati | form, in fase di sviluppo |
| 🟠 | Testi legali: titolare, finalità, conservazione | `/privacy-policy`, `/cookie-policy` |
| ⚪ | Orari di apertura, sede legale da mostrare, raggio di intervento per il residenziale | Contatti, landing B2C |
| ⚪ | Accessi a dominio, DNS e hosting · account GA4 e Search Console esistenti | go-live |
| ⚪ | Pagina Facebook aziendale (l'attuale link è un profilo personale) | footer |

---

## Da non dimenticare in fase di sviluppo

Difetti del sito attuale che il nuovo sito deve chiudere. A distanza di settimane è la parte che si perde più facilmente.

- `canonical` e `og:url` contengono codice PHP non interpretato su **7 pagine su 10** → generarli correttamente (W-022).
- `/partner.php` è dichiarata in `sitemap.xml` e risponde **404** → la nuova pagina partner lo chiude, sitemap da rigenerare dalle pagine reali.
- **GA4 e Search Console vanno attivati prima del go-live**, per avere una baseline di confronto (W-026). Oggi non esiste alcun analytics.
- Testi legali **su dominio proprio**: oggi l'unica informativa è un popup su `sitofelice.it` (W-025).
- Redirect 301 da tutti i vecchi URL `.php`, mappa nel [Doc 03](https://sonit-jhkstudio.vercel.app/docs/architettura-informazioni#slug) (W-027).
- `user-scalable=no` nel viewport, immagini senza `alt`, 2,57 MB di immagini in home: da non replicare (W-023, W-024).
- Il refuso "Effic**e**ntamento" non deve tornare: slug corretto `/soluzioni/fotovoltaico`.

---

## Dove sta cosa

| Percorso | Contenuto |
|---|---|
| [`README.md`](README.md) | Indice del repo, vincoli, convenzioni, comandi |
| [`WORKLOG.md`](WORKLOG.md) | Fasi, attività, decisioni, materiali attesi, diario |
| `docs/stato-arte-sonit.html` | Doc 01 — analisi del sito attuale, criticità, gap analysis |
| `docs/alberatura-attuale.html` | Doc 02 — alberatura del sito attuale, schede pagina |
| `docs/architettura-informazioni.html` | Doc 03 — nuova alberatura, decisioni validate, redirect |
| `docs/contenuti/` | Doc 04 — contenuti riscritti, un file per pagina |
| `docs/contenuti/_sorgente_testi.py` | **sorgente dei testi**: si modifica qui |
| `docs/contenuti/_genera.py` | rigenera i file di contenuto |
| `docs/piano-wireframe.html` | Doc 05 — piano dei wireframe, sezioni pagina per pagina, checklist |
| `presentazione/index.html` | **Versione cliente**: alberatura semplificata + wireframe con i contenuti |
| `docs/_genera-presentazione.py` | rigenera la versione cliente |
| `docs/_layout.py` | layout e forma dei blocchi, condivisi da Doc 05 e versione cliente |
| `docs/_genera-piano-wireframe.py` | rigenera il Doc 05 dalle stesse sorgenti |
| `docs/testi/` | testi del sito attuale, riportati alla lettera |

```bash
# anteprima locale
python3 -m http.server 4000

# rigenerare contenuti e piano wireframe dopo una modifica ai testi
python3 docs/contenuti/_genera.py
python3 docs/_genera-piano-wireframe.py
python3 docs/_genera-presentazione.py

# pubblicare
vercel deploy --prod
```

---

## Governance

- **Approvazione documenti ufficiali:** Giorgio.
- **Riferimenti operativi:** Giorgio e Beatrice.
- Ogni comunicazione e ogni deliverable vanno inviati a **entrambi** gli indirizzi.
- La documentazione online è su Vercel con protezione attiva: per condividerla col cliente va disattivata la Vercel Authentication o generato un link di bypass.
