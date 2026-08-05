# SONIT · Progetto DXP — Worklog

Registro operativo del progetto di restyling di [sonit.it](https://www.sonit.it/).
Documentazione online: <https://sonit-jhkstudio.vercel.app> · Indice generale: [README.md](README.md)

Ultimo aggiornamento: **05/08/2026**

---

## Fasi

| Fase | Deliverable | Output | Stato |
|---|---|---|---|
| **F0** | Kick-off | Verbale, obiettivi condivisi, governance | ✅ completata 28/07/2026 |
| **F1** | Stato dell'arte | Doc 01, Doc 02, testi estratti | ✅ completata 05/08/2026 |
| **F2** | Architettura delle informazioni | Doc 03 + presentazione al cliente | 🔵 proposta pronta, da validare |
| **F3** | Contenuti e wireframe | Contenuti per sezione + wireframe low fidelity | ⬜ da avviare |
| **F4** | Direzione visiva | **Due** proposte di design | ⬜ da avviare |
| **F5** | Design completo | Tutte le pagine, desktop e mobile | ⬜ da avviare |
| **F6** | Sviluppo | Ambiente di staging | ⬜ da avviare |
| **F7** | Go-live | Sito online, redirect, analytics, collaudo | ⬜ da avviare |

Regola di validazione concordata in kick-off: ogni fase si chiude con presentazione, feedback e approvazione prima di passare alla successiva. Le variazioni di struttura e contenuto vanno concentrate tra F2 e F5, dove costano una frazione di quanto costerebbero in sviluppo.

---

## Attività

Legenda stato: ✅ fatto · 🔵 in corso · ⏳ atteso dal cliente · ⬜ da fare

| ID | Attività | Fase | Dipende da | Owner | Stato |
|---|---|---|---|---|---|
| W-001 | Analisi sito online: struttura, pagine, stack, SEO, performance | F1 | — | Team dev | ✅ |
| W-002 | Estrazione alberatura attuale | F1 | W-001 | Team dev | ✅ |
| W-003 | Inventario contenuti riutilizzabili | F1 | W-001 | Team dev | ✅ |
| W-004 | Gap analysis obiettivi vs sito | F1 | W-002 | Team dev | ✅ |
| W-005 | Estrazione palette e tipografia attuali | F1 | W-001 | Team dev | ✅ |
| W-006 | Invio Doc 01 a Giorgio e Beatrice | F1 | W-004 | Referente progetto | ⬜ |
| W-007 | Raccolta materiali dal cliente su Drive condiviso | F1 | — | Giorgio / Beatrice | ⏳ |
| W-032 | Viste grafiche verticale e orizzontale dell'alberatura attuale | F1 | W-002 | Team dev | ✅ |
| W-033 | Estrazione dei testi di tutte le 10 pagine in `docs/testi/` | F1 | W-002 | Team dev | ✅ |
| W-034 | Collegamento bidirezionale testi ↔ alberatura | F1 | W-033 | Team dev | ✅ |
| W-008 | Nuova architettura delle informazioni e sitemap con razionale | F2 | W-004 | Team dev | ✅ |
| W-009 | Strategia B2B / B2C fotovoltaico e punti di separazione | F2 | W-008 | Team dev + cliente | ✅ proposta |
| W-035 | Mappatura riuso dei contenuti estratti, blocco per blocco | F2 | W-033, W-008 | Team dev | ✅ |
| W-036 | Sistema di messaggi: posizionamento e pilastri di prova | F2 | W-008 | Team dev | ✅ proposta |
| W-010 | Presentazione architettura al cliente e raccolta feedback | F2 | W-008 | Referente progetto | 🔵 prossimo |
| W-011 | Validazione delle decisioni aperte D-01 → D-07 | F2 | W-010 | Cliente | ⬜ |
| W-012 | Stesura contenuti per pagina, con riuso e correzione dei testi esistenti | F3 | W-011, W-007 | Team contenuti | ⬜ |
| W-013 | Wireframe low fidelity di tutte le pagine | F3 | W-012 | Team design | ⬜ |
| W-014 | Definizione formato case study, senza foto reali di cantiere | F3 | W-011 | Team contenuti | ⬜ |
| W-015 | Selezione libreria immagini standard coerente con le linee guida | F3 | W-011 | Team design | ⬜ |
| W-016 | Due proposte di direzione visiva su base blu `#003A83` | F4 | W-013 | Team design | ⬜ |
| W-017 | Design system: scala blu, tipografia, componenti, stati | F5 | W-016 | Team design | ⬜ |
| W-018 | Design di tutte le pagine desktop e mobile con contenuti definitivi | F5 | W-017 | Team design | ⬜ |
| W-019 | Sviluppo front-end e template | F6 | W-018 | Team dev | ⬜ |
| W-020 | Form B2B e form B2C + pagina `/grazie` + antispam | F6 | W-019 | Team dev | ⬜ |
| W-021 | Blocco download brochure e company profile PDF | F6 | W-007, W-019 | Team dev | ⬜ |
| W-022 | Migrazione JSON-LD, canonical, Open Graph, sitemap, robots | F6 | W-019 | Team dev | ⬜ |
| W-023 | Ottimizzazione immagini: WebP/AVIF, responsive, lazy loading | F6 | W-019 | Team dev | ⬜ |
| W-024 | Accessibilità: zoom, `alt`, gerarchia titoli, contrasti, focus | F6 | W-019 | Team dev | ⬜ |
| W-025 | Privacy policy, cookie policy e termini su dominio proprio | F6 | W-019 | Team dev + cliente | ⬜ |
| W-026 | Setup GA4 e Search Console prima del go-live, per avere una baseline | F6 | — | Team dev | ⬜ |
| W-027 | Mappa redirect 301 dai vecchi URL `.php` | F6 | W-011 | Team dev | ⬜ |
| W-028 | Decisione su area riservata WebApp (`app.sonit.it`) | F6 | — | Cliente | ⏳ |
| W-029 | Configurazione hosting: cache, HSTS, header di sicurezza | F6 | W-019 | Team dev | ⬜ |
| W-030 | Collaudo pre-go-live: canonical, form, redirect, accessibilità, performance | F7 | W-019…W-029 | Team dev | ⬜ |
| W-031 | Pubblicazione e verifica post-lancio: indicizzazione, errori, conversioni | F7 | W-030 | Team dev | ⬜ |

---

## Decisioni aperte

Dettaglio e proposte nel [Doc 03](https://sonit-jhkstudio.vercel.app/docs/architettura-informazioni#decisioni).

| # | Decisione | Proposta del team | Stato |
|---|---|---|---|
| D-01 | B2C fotovoltaico: pagina autonoma o sezione della pagina business unit? | Pagina autonoma `/fotovoltaico-casa`, fuori dal menu | ⏳ da validare |
| D-02 | La consulenza resta una pagina o diventa un blocco trasversale? | Blocco trasversale in `/soluzioni` e nelle pagine BU | ⏳ da validare |
| D-03 | Menu principale a 6 voci: va bene questo peso? | Sei voci, con `Soluzioni` unica voce con sottomenu | ⏳ da validare |
| D-04 | Si nomina "general contractor" o si descrive la capacità? | Descrivere ora, adottare l'etichetta a riposizionamento compiuto | ⏳ da validare |
| D-05 | I numeri aziendali sono pubblicabili? | Sì: sono la prova più efficace di solidità | ⏳ da validare |
| D-06 | Si pubblica "Lavora con noi"? | Predisposta, da attivare se serve all'organico | ⏳ da validare |
| D-07 | Area riservata: header, footer o fuori dal sito pubblico? | Link discreto in header, accanto al telefono | ⏳ da validare |

## Materiali attesi dal cliente

| # | Materiale | Blocca |
|---|---|---|
| A-01 | Elenco certificazioni con enti ed estremi | `/certificazioni` — pagina dichiarata prioritaria |
| A-02 | Brochure e company profile PDF definitivi | download in `/chi-siamo` |
| A-03 | Partner e fornitori pubblicabili, con loghi e autorizzazione | `/partner` |
| A-04 | Committenti nominabili sul sito | `/partner`, `/progetti` |
| A-05 | Numeri aggiornati: organico, ruoli interni, cantieri | home, `/chi-siamo` |
| A-06 | 3–5 progetti candidabili a case study | `/progetti` |
| A-07 | Caselle email di destinazione, distinte B2B e B2C | form |
| A-08 | Decisione sull'area riservata WebApp | header o footer |
| A-09 | Accessi a dominio, DNS e hosting attuali | go-live |
| A-10 | Esistono account Google Analytics o Search Console? | baseline dei dati |
| A-11 | Pagina Facebook aziendale — l'attuale link è un profilo personale | footer |
| A-12 | Testi legali: titolare del trattamento, finalità, conservazione | pagine legali |
| A-13 | Taglie tipiche degli impianti fotovoltaici B2B e residenziali | pagine fotovoltaico |

---

## Criticità aperte sul sito attualmente online

Queste restano attive fino al go-live del nuovo sito. Le prime due si possono correggere subito sul sito esistente, se il cliente lo ritiene utile.

| Priorità | Criticità |
|---|---|
| 🔴 | `canonical` e `og:url` contengono codice PHP non interpretato su 7 pagine su 10 |
| 🔴 | `/partner.php` dichiarata in `sitemap.xml` ma risponde 404 |
| 🔴 | `/privacy.php` senza informativa; testi legali su dominio terzo |
| 🔴 | Nessuno strumento di analytics installato: zero baseline di traffico |
| 🟠 | "Lavori" nel menu porta a una pagina vuota |
| 🟠 | 2,57 MB di immagini caricate dalla sola home, di cui 1,58 MB di slider datato 2022 |
| 🟠 | `user-scalable=no` blocca lo zoom su mobile; oltre metà delle immagini senza `alt` |
| 🟠 | Refuso "Effic**e**ntamento" in URL, title, H1, menu e keywords |

Elenco completo, con severità e rimedio: [Doc 01 · criticità](https://sonit-jhkstudio.vercel.app/docs/stato-arte-sonit#criticita).

---

## Diario delle modifiche

Voci in ordine cronologico inverso.

### 05/08/2026 — Doc 03: nuova architettura delle informazioni
Pubblicata la proposta di alberatura per il nuovo sito, con viste verticale e orizzontale, albero con le sezioni di ogni pagina, confronto prima/dopo, schede delle 11 pagine previste, sistema di messaggi, struttura della home, template delle pagine business unit, percorso B2C, specifica dei form, slug e redirect. Mappati tutti i blocchi di testo estratti con verdetto di riuso: circa il 45% del contenuto attuale è riusabile con interventi minimi. Aperte 7 decisioni da validare (D-01 → D-07). Aggiunti `README.md` e questo worklog.

### 05/08/2026 — Testi estratti da tutte le pagine
Creata la cartella `docs/testi/` con un file HTML per pagina, nominato come la pagina di origine. Ogni file riporta il contenuto alla lettera, i blocchi ripetuti del template, gli attributi `alt`, i campi dei form e i link. Collegamento bidirezionale con le schede pagina del Doc 02; i nodi dei diagrammi dell'alberatura sono diventati cliccabili.

### 05/08/2026 — Viste grafiche dell'alberatura e navigazione
Aggiunte al Doc 02 le due viste grafiche dell'alberatura attuale, verticale e orizzontale, con legenda dello stato di ogni pagina. Inserita in testa a ogni documento una barra di navigazione persistente con il ritorno all'indice.

### 05/08/2026 — Doc 02: alberatura del sito attuale
Estratta la struttura completa di sonit.it: albero con le sezioni interne di ogni pagina, confronto menu / `sitemap.xml` / realtà, mappa dei link interni (121 link totali, di cui solo 9 contestuali), matrice dei blocchi di template, 11 schede pagina, risorse fuori albero, 13 anomalie strutturali. Rilevati due form in homepage con lo stesso `name`, il primo dei quali invia credenziali a `app.sonit.it` in tecnologia ASP.

### 05/08/2026 — Doc 01: stato dell'arte
Prima stesura. Analisi del sito online (10 pagine più 1 URL in 404), alberatura attuale, inventario contenuti, 20 criticità classificate, estrazione di palette e tipografia, gap analysis sugli obiettivi di kick-off, fasi di progetto, worklog, bozza di alberatura, elenco materiali da richiedere al cliente, bozza di piano redirect.

### 28/07/2026 — Kick-off
Definiti obiettivi strategici, vincoli visivi, strategia di canale B2B/B2C, contenuti prioritari e governance delle comunicazioni. Confermato che brand e marchio restano invariati.
