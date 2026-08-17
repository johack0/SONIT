# SONIT · Progetto DXP — Restyling sito

Documentazione di progetto per il rifacimento del sito **[sonit.it](https://www.sonit.it/)** di Sonit Srl.
Repo di lavoro: contiene analisi, alberature, testi estratti dal sito attuale e l'architettura validata del nuovo sito.

**Documentazione online:** <https://sonitgamma.vercel.app>
La documentazione è pubblicata su Vercel e non è indicizzabile (`X-Robots-Tag: noindex`), ma è raggiungibile senza autenticazione: il link si può mandare al cliente così com'è. La versione da mostrare in riunione è <https://sonitgamma.vercel.app/presentazione>.

---

## Cosa c'è dentro

| Percorso | Contenuto |
|---|---|
| `RIPRESA.md` | **Punto di ripresa: da leggere per primo al rientro** |
| `index.html` | Hub della documentazione: elenco documenti, avanzamento fasi, sintesi dell'analisi |
| `docs/stato-arte-sonit.html` | **Doc 01** — Stato dell'arte: analisi del sito online, criticità, gap analysis, fasi, worklog, diario |
| `docs/alberatura-attuale.html` | **Doc 02** — Alberatura del sito attuale: viste verticale e orizzontale, schede pagina, anomalie strutturali |
| `docs/architettura-informazioni.html` | **Doc 03** — Nuova alberatura e organizzazione dei contenuti (fase F2, decisioni validate) |
| `docs/contenuti/` | **Doc 04** — Contenuti del nuovo sito: un file per pagina della nuova alberatura, copy pronto blocco per blocco |
| `docs/piano-wireframe.html` | **Doc 05** — Piano dei wireframe e punto di ripresa: ordine di produzione, sezioni per pagina, schemi, checklist |
| `presentazione/index.html` | **Versione cliente** — Documento unico da presentare: alberatura semplificata e wireframe a blocchi con i contenuti dentro |
| `docs/testi/` | Testi estratti dal sito online, un file per pagina, riportati alla lettera |
| `WORKLOG.md` | Worklog operativo: fasi, attività con stato, decisioni chiuse, materiali attesi, diario delle modifiche |
| `SONIT _ Kick Off DXP … .docx` | Verbale del kick-off del 28/07/2026 |
| `vercel.json` | Configurazione hosting: clean URLs, header `noindex` |

### I testi estratti

Un file per ogni pagina del sito attuale, nominato come la pagina di origine:

```
docs/testi/index.html                      ← index.php          (Home)
docs/testi/sonit-srl.html                  ← sonit-srl.php      (Chi Siamo)
docs/testi/servizi-sonit.html              ← servizi-sonit.php  (Servizi e Soluzioni)
docs/testi/impianti-sistemi.html           ← impianti-sistemi.php
docs/testi/telecomunicazioni.html          ← telecomunicazioni.php
docs/testi/efficentamento-energetico.html  ← efficentamento-energetico.php
docs/testi/consulenza.html                 ← consulenza.php
docs/testi/foto.html                       ← foto.php           (Lavori)
docs/testi/contatti.html                   ← contatti.php
docs/testi/privacy.html                    ← privacy.php
```

Ogni file contiene i metadati della pagina, il contenuto **riportato alla lettera** (refusi compresi, non corretti), i blocchi ripetuti del template, gli attributi `alt`, i campi dei form e i link. È il materiale di partenza per la riscrittura in fase F3.

### La versione cliente

`presentazione/index.html` è l'unico documento da mettere in mano al cliente: alberatura semplificata delle nove pagine, poi ogni pagina disegnata come una finestra di browser con le sezioni nell'ordine reale e il copy dentro i blocchi. I rettangoli tratteggiati sono gli spazi per immagini, loghi, mappa e schede; i riquadri arancioni sono le sezioni che dipendono dai materiali del cliente, con la richiesta scritta. In chiusura, l'elenco delle richieste raggruppate per pagina e le domande di approvazione. Non contiene codici interni, title tag né conteggi di caratteri.

Si rigenera con `python3 docs/_genera-presentazione.py`.

### I contenuti del nuovo sito

Un file per ogni pagina della nuova alberatura, in `docs/contenuti/`:

```
docs/contenuti/index.html              Panoramica: stato, riepilogo, regole redazionali
docs/contenuti/home.html               /
docs/contenuti/chi-siamo.html          /chi-siamo
docs/contenuti/soluzioni.html          /soluzioni
docs/contenuti/telecomunicazioni.html  /soluzioni/telecomunicazioni
docs/contenuti/impianti.html           /soluzioni/impianti
docs/contenuti/fotovoltaico.html       /soluzioni/fotovoltaico
docs/contenuti/fotovoltaico-casa.html  /fotovoltaico-casa
docs/contenuti/certificazioni.html     /certificazioni
docs/contenuti/partner.html            /partner
docs/contenuti/progetti.html           /progetti
docs/contenuti/contatti.html           /contatti
```

Ogni file riporta obiettivo, pubblico e azione attesa della pagina, `title` e `meta description` proposti, e il copy pronto blocco per blocco con la provenienza: riuso dal sito attuale, testo nuovo, oppure in attesa di materiali dal cliente. Le etichette `DA CONFERMARE` e `DA MATERIALI CLIENTE` segnalano ciò che non è ancora definitivo.

---

## Come si naviga

Tutti i documenti sono collegati tra loro:

- ogni sotto-pagina ha in testa una barra con il ritorno all'**indice dei documenti** e i link ai documenti gemelli;
- nel Doc 02 i **nodi dei diagrammi sono cliccabili** e aprono i testi estratti di quella pagina;
- nel Doc 03 i **nodi dei diagrammi** aprono i contenuti riscritti della pagina corrispondente;
- ogni scheda pagina del Doc 02 ha un pulsante `Testi estratti →`;
- ogni file di testo rimanda alla scheda corrispondente del Doc 02.

---

## Stato del progetto

| Fase | Deliverable | Stato |
|---|---|---|
| F0 | Kick-off, obiettivi e governance | ✅ completata 28/07/2026 |
| F1 | Stato dell'arte, alberatura attuale, testi estratti | ✅ completata 05/08/2026 |
| F2 | Architettura delle informazioni | ✅ completata 05/08/2026, decisioni validate |
| F3 | Contenuti e wireframe low fidelity | 🔵 contenuti scritti (11 pagine), versione cliente pubblicata, wireframe di dettaglio dopo l'approvazione |
| F4 | Due proposte di direzione visiva | ⬜ da avviare |
| F5 | Design completo di tutte le pagine | ⬜ da avviare |
| F6 | Sviluppo | ⬜ da avviare |
| F7 | Go-live, redirect, analytics, collaudo | ⬜ da avviare |

Dettaglio delle attività, delle dipendenze e delle decisioni prese: **[WORKLOG.md](WORKLOG.md)**.

---

## Vincoli di progetto

- **Brand invariato**: logo e marchio registrato restano quelli attuali, ridisegnati di recente.
- **Nessuna foto reale** di cantieri o mezzi: immagini standard, di ampio respiro.
- **Palette sui toni del blu** del brand — il blu istituzionale già in uso è `#003A83`.
- **Poche pagine, ben organizzate.**
- **B2B istituzionale**, con B2C solo sul fotovoltaico e netta separazione tra i due percorsi.
- **Nessuna integrazione** tra i form del sito e i gestionali interni, per ora.

## Governance

- **Approvazione documenti ufficiali:** Giorgio.
- **Riferimenti operativi per le chiamate:** Giorgio e Beatrice.
- Ogni comunicazione e ogni deliverable vanno inviati a **entrambi** gli indirizzi.
- I materiali aziendali vengono caricati sulla cartella Google Drive condivisa.

---

## Lavorare su questo repo

I documenti sono HTML statici autoconsistenti: nessuna build, nessuna dipendenza esterna, CSS e SVG inline.

> **Riprendi da qui:** se stai tornando sul progetto dopo una pausa, leggi [`RIPRESA.md`](RIPRESA.md) prima di ogni altra cosa.

```bash
# anteprima locale
python3 -m http.server 4000
# poi apri http://localhost:4000

# anteprima con le stesse regole di Vercel (clean URLs)
vercel dev

# pubblicazione
vercel deploy --prod
```

### Convenzioni

- Ogni documento porta un numero (`Doc 01`, `Doc 02`, …), una versione e la data in sidebar e nel footer.
- Ogni modifica sostanziale va registrata nel **diario delle modifiche** del Doc 01 e in `WORKLOG.md`, aggiungendo la voce in cima.
- I testi estratti da `docs/testi/` **non si correggono**: sono la fotografia del sito attuale. Le correzioni si fanno nei nuovi contenuti.
- I contenuti in `docs/contenuti/` sono **generati**: i testi stanno in `docs/contenuti/_sorgente_testi.py`, si modificano lì e si rigenera con `python3 docs/contenuti/_genera.py`. Non si editano i singoli HTML, altrimenti la prossima rigenerazione li sovrascrive.
- Il Doc 05 e la versione cliente leggono le stesse sorgenti: dopo ogni modifica ai testi rigenerare anche con `python3 docs/_genera-piano-wireframe.py` e `python3 docs/_genera-presentazione.py`, così sezioni e wireframe restano allineati.
- I layout dei blocchi stanno in `docs/_layout.py` (`LAY` = layout previsto, `SHAPE` = forma del wireframe disegnato): si modificano lì, sono condivisi dai due documenti.
- Nuovi documenti: si aggiunge la card in `index.html` e i link incrociati nelle barre di navigazione degli altri documenti.
