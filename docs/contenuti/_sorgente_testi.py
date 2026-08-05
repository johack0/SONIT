# -*- coding: utf-8 -*-
"""Contenuti riscritti per il nuovo sito Sonit. Fase F3.
Ogni blocco: (nome, fonte, copy_html). fonte: riuso|nuovo|cliente
"""

TODO = lambda t: f'<span class="todo">DA CONFERMARE · {t}</span>'
CLI  = lambda t: f'<span class="cli">DA MATERIALI CLIENTE · {t}</span>'

PAGES = []

# ─────────────────────────────────────────── HOME
PAGES.append(dict(
 slug="home", url="/", label="Home", node="Home",
 goal="In quindici secondi far capire chi è Sonit, che dimensione ha, cosa sa fare come sistema integrato e a chi si rivolge.",
 audience="Buyer e tecnici B2B in primo luogo. Il privato trova un ingresso dedicato e riconoscibile.",
 cta="Vai alle soluzioni · Contattaci · (privati) Chiedi un preventivo per la casa",
 title="Impianti, telecomunicazioni e fotovoltaico | Sonit Srl",
 desc="Reti di telecomunicazione, impianti civili e industriali e fotovoltaico: progettazione, realizzazione e manutenzione con squadre interne. Roma e Frosinone.",
 h1="Una sola regia su reti, impianti ed energia",
 blocks=[
  ("Hero", "nuovo", """
<p class="c-h1">Una sola regia su reti, impianti ed energia.</p>
<p class="c-sub">Progettiamo, realizziamo e manteniamo infrastrutture di telecomunicazione, impianti civili e industriali e impianti fotovoltaici. Squadre interne, un unico responsabile per commessa, dall'analisi al collaudo.</p>
<p class="c-btn">[Sono un'impresa → /soluzioni] &nbsp; [Sono un privato e voglio il fotovoltaico → /fotovoltaico-casa]</p>
<p class="c-note">Sostituisce la citazione di Henry Ford. La riga di offerta è la riscrittura del paragrafo istituzionale oggi in home.</p>"""),

  ("Sonit in numeri", "cliente", f"""
<p class="c-lbl">Sonit in numeri</p>
<div class="c-nums">
  <div><b>45</b><span>dipendenti diretti</span></div>
  <div><b>5 anni</b><span>per passare da 2 a 45 persone</span></div>
  <div><b>2</b><span>sedi operative: Arpino e Roma</span></div>
  <div><b>Italia</b><span>area di intervento</span></div>
</div>
<p>Cresciamo mantenendo dentro l'azienda le competenze che contano: direzione generale, capicantiere e maestranze sono nostri. È la ragione per cui possiamo assumere la responsabilità di una commessa dall'inizio alla fine.</p>
<p class="c-note">{TODO("i quattro dati vanno confermati da Giorgio prima della pubblicazione: sono la prova principale della home")}</p>"""),

  ("Le tre business unit come sistema", "nuovo", """
<p class="c-lbl">Tre competenze, un solo interlocutore</p>
<p>Le nostre tre aree non sono servizi separati: si incontrano nello stesso cantiere. Un impianto elettrico e un impianto fotovoltaico sono lo stesso lavoro visto da due lati; una rete in fibra ha bisogno di opere civili e di impianti. Chi ci affida un intervento parla con una sola struttura.</p>
<div class="c-cards">
  <div><b>Telecomunicazioni</b>
   <p>Cablaggi strutturati e reti in fibra ottica: pianificazione, opere civili, posa, giunzione e collaudo. È il nostro core business.</p>
   <p class="c-link">Scopri le telecomunicazioni →</p></div>
  <div><b>Impianti civili e industriali</b>
   <p>Impianti elettrici, videosorveglianza, allarme, domotica e automazione, idraulico e climatizzazione, per edifici residenziali e industriali.</p>
   <p class="c-link">Scopri gli impianti →</p></div>
  <div><b>Fotovoltaico ed efficientamento</b>
   <p>Impianti fotovoltaici, solare termico e pompe di calore, con la gestione completa di incentivi e detrazioni.</p>
   <p class="c-link">Scopri il fotovoltaico →</p></div>
</div>"""),

  ("Come lavoriamo, in cinque passi", "riuso", """
<p class="c-lbl">Come lavoriamo</p>
<ol class="c-steps">
  <li><b>Analisi e progettazione</b> — pianifichiamo l'impianto più adatto alle esigenze del committente e realizziamo i progetti esecutivi.</li>
  <li><b>Opere civili</b> — eseguiamo tutte le opere edili e strutturali necessarie, compresi scavi e ripristini.</li>
  <li><b>Infrastrutture</b> — installiamo e configuriamo apparati e dispositivi.</li>
  <li><b>Incentivi e pratiche</b> — gestiamo incentivi fiscali, detrazioni e pratiche autorizzative, per massimizzare il beneficio economico del cliente.</li>
  <li><b>Manutenzione e pronto intervento</b> — restiamo il riferimento dopo la consegna, su danni e malfunzionamenti.</li>
</ol>
<p class="c-note">Riuso dei cinque blocchi di processo oggi duplicati su Impianti e Sistemi e su Efficentamento Energetico. Da qui in avanti sono scritti una volta sola.</p>"""),

  ("Certificazioni", "cliente", f"""
<p class="c-lbl">Lavoriamo secondo norma, e ce lo facciamo verificare</p>
<p>Le nostre qualifiche e certificazioni sono la parte del lavoro che il committente non vede in cantiere ma che determina se possiamo esserci.</p>
<p class="c-btn">[Vedi le certificazioni → /certificazioni]</p>
<p class="c-note">{CLI("elenco certificazioni con enti ed estremi, per mostrare qui le 3–4 principali")}</p>"""),

  ("Partner e fornitori", "cliente", f"""
<p class="c-lbl">Con chi lavoriamo</p>
<p>Lavoriamo con produttori e fornitori selezionati: la qualità di un impianto dipende anche da chi fornisce i materiali e da quanto è solida la catena che ce li porta in cantiere.</p>
<p class="c-btn">[Vedi partner e fornitori → /partner]</p>
<p class="c-note">{CLI("loghi e nomi pubblicabili, con autorizzazione all'uso")}</p>"""),

  ("Un progetto in evidenza", "cliente", f"""
<p class="c-lbl">Un lavoro raccontato per intero</p>
<p>Ogni cantiere cambia mentre lo esegui. La differenza la fa cosa si riesce a fare quando cambia.</p>
<p class="c-btn">[Leggi il progetto →] &nbsp; [Tutti i progetti → /progetti]</p>
<p class="c-note">{CLI("il progetto scelto tra i 3–5 candidati a case study")}</p>"""),

  ("Fotovoltaico per i privati", "nuovo", """
<p class="c-lbl">Sei un privato?</p>
<p>Installiamo impianti fotovoltaici anche per le abitazioni, con sopralluogo gratuito, progetto su misura e gestione completa delle detrazioni. Un percorso dedicato, separato dai nostri impianti industriali.</p>
<p class="c-btn">[Fotovoltaico per la casa → /fotovoltaico-casa]</p>
<p class="c-note">Unico punto di passaggio dal percorso B2B a quello B2C dentro il corpo della home, oltre alla CTA in hero. Blocco visivamente distinto.</p>"""),

  ("Contatti rapidi", "riuso", f"""
<p class="c-lbl">Parliamone</p>
<p>Sede operativa principale: Via S. Altissimo snc, 03033 Arpino (FR).<br>
Sede operativa di Roma: Via Pescara 2, 00182 Roma.<br>
Telefono: +39 0776 868072 · Email: info@sonit.it</p>
<p class="c-btn">[Contattaci → /contatti]</p>
<p class="c-note">Riuso dei dati di contatto attuali. Non il form completo: il form vive dove la richiesta si qualifica. {TODO("orari di apertura")}</p>"""),
 ]))

# ─────────────────────────────────────────── CHI SIAMO
PAGES.append(dict(
 slug="chi-siamo", url="/chi-siamo", label="Chi siamo", node="Chi siamo",
 goal="Dimostrare solidità e struttura organizzativa: è la pagina che sostiene il posizionamento.",
 audience="B2B in valutazione fornitore, potenziali partner, candidati.",
 cta="Scarica brochure e company profile · Contattaci",
 title="Chi siamo | Sonit Srl, reti, impianti ed energia",
 desc="Direzione, capicantiere e maestranze interne, due sedi operative e copertura nazionale su reti, impianti ed energia. Chi è Sonit Srl e come è organizzata.",
 h1="Una struttura costruita per gestire commesse complesse",
 blocks=[
  ("Chi siamo oggi", "nuovo", f"""
<p>Sonit Srl progetta, realizza e mantiene reti di telecomunicazione, impianti civili e industriali e impianti fotovoltaici su tutto il territorio nazionale, con due sedi operative in Lazio.</p>
<p>Siamo nati come squadra di tecnici e siamo diventati un'organizzazione: oggi la direzione generale, i capicantiere e le maestranze sono personale nostro. È quello che ci permette di prendere in carico un lavoro per intero, senza scaricare il coordinamento sul committente.</p>
<p class="c-note">Sostituisce il testo attuale, che parla di "azienda di recente costituzione" e mette i titolari al centro: dice l'opposto di ciò che serve comunicare. {TODO("anno di costituzione da usare nel title tag")}</p>"""),

  ("Crescita e struttura", "cliente", f"""
<p class="c-lbl">Come siamo cresciuti</p>
<p>In cinque anni siamo passati da 2 a 45 dipendenti diretti, e continuiamo ad assumere. La crescita è stata una scelta di struttura, non solo di numeri: abbiamo aggiunto figure di coordinamento e tecnici qualificati per poter dire di sì a commesse più grandi senza abbassare gli standard.</p>
<ul>
  <li><b>Direzione e coordinamento</b> — gestione delle commesse e rapporto diretto con il committente.</li>
  <li><b>Capicantiere</b> — presidio operativo su ogni cantiere, tutti interni.</li>
  <li><b>Maestranze specializzate</b> — squadre per reti, impianti ed energia.</li>
  <li><b>Formazione continua</b> — investiamo sulla qualità dell'esecuzione più che sul numero di cantieri aperti.</li>
</ul>
<p class="c-note">{CLI("numeri aggiornati di organico e ripartizione dei ruoli")} · {TODO("la previsione 50–55 persone con il subappalto: pubblicabile?")}</p>"""),

  ("Valori e responsabilità", "riuso", """
<p class="c-lbl">Come stiamo in cantiere</p>
<p>Siamo una squadra di professionisti con esperienza, competenza e mentalità innovativa. Il nostro obiettivo è l'erogazione di un servizio professionale, rispettoso dell'ambiente, della salute e della sicurezza dei lavoratori.</p>
<p>Poniamo attenzione costante all'attuazione della compliance legislativa e al miglioramento continuo delle nostre performance.</p>
<p class="c-note">Riuso quasi letterale dai testi attuali di Chi Siamo: sono due passaggi che funzionano già così. La parte su compliance viene richiamata anche in Certificazioni.</p>"""),

  ("Dove siamo", "riuso", f"""
<p class="c-lbl">Due sedi operative, una copertura nazionale</p>
<p><b>Sede operativa principale</b><br>Via S. Altissimo snc, 03033 Arpino (FR)</p>
<p><b>Sede operativa di Roma</b><br>Via Pescara 2, 00182 Roma</p>
<p>Operiamo su tutto il territorio nazionale. Il presidio in provincia di Frosinone e quello a Roma ci permettono di intervenire rapidamente nel Lazio e di seguire cantieri fuori regione con squadre nostre.</p>
<p class="c-note">Riuso degli indirizzi dalla pagina Contatti attuale. {TODO("la sede legale, oggi presente solo nei dati strutturati, va mostrata anche all'utente?")}</p>"""),

  ("Download brochure e company profile", "cliente", f"""
<p class="c-lbl">Documenti</p>
<p>Brochure aziendale e company profile in formato PDF, con l'inquadramento completo dell'azienda, le competenze e i riferimenti.</p>
<p class="c-btn">[Scarica la brochure · PDF] &nbsp; [Scarica il company profile · PDF]</p>
<p class="c-note">{CLI("i due PDF definitivi. Richiesta emersa in kick-off: nel 90% delle relazioni commerciali sostituiscono il cartaceo")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Se state valutando un fornitore per una commessa su reti, impianti o energia, il modo più rapido per capire se siamo la struttura giusta è parlarne.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── SOLUZIONI (hub)
PAGES.append(dict(
 slug="soluzioni", url="/soluzioni", label="Soluzioni integrate", node="Soluzioni integrate",
 goal="Spiegare l'ecosistema: una sola regia su reti, impianti ed energia, con squadre interne e un unico responsabile di commessa.",
 audience="B2B con un problema su più fronti, che non vuole coordinare tre fornitori.",
 cta="Entra nella business unit pertinente · Contattaci",
 title="Soluzioni integrate: reti, impianti ed energia | Sonit Srl",
 desc="Tre competenze, un solo interlocutore: telecomunicazioni, impianti civili e industriali, fotovoltaico ed efficientamento, dalla progettazione alla manutenzione.",
 h1="Tre competenze, un solo interlocutore",
 blocks=[
  ("L'ecosistema integrato", "nuovo", """
<p>La maggior parte dei lavori che ci vengono affidati non sta dentro una sola specializzazione. Una rete in fibra ha bisogno di scavi e di opere civili. Un impianto fotovoltaico è anche un impianto elettrico. Un edificio industriale mette insieme energia, sicurezza e automazione.</p>
<p>Le nostre tre business unit lavorano sullo stesso cantiere, con una sola direzione. Per il committente significa tre cose concrete: un solo responsabile a cui chiedere, nessun tempo perso a far parlare fornitori diversi tra loro, nessuna zona grigia di responsabilità quando qualcosa va rifatto.</p>
<p class="c-note">È il contenuto che oggi manca del tutto: la pagina "Servizi e Soluzioni" attuale ha 127 parole e solo quattro card. Questo blocco è il messaggio dell'ecosistema integrato chiesto in kick-off.</p>"""),

  ("Cosa realizziamo", "riuso", """
<p class="c-lbl">Le nostre competenze</p>
<ul class="c-two">
  <li>Impianti per le telecomunicazioni</li>
  <li>Impianti tecnologici</li>
  <li>Impianti di pubblica illuminazione e reti elettriche</li>
  <li>Impianti di videosorveglianza</li>
  <li>Impianti idraulici</li>
  <li>Impianti per l'efficientamento energetico</li>
</ul>
<p class="c-note">Riuso dell'elenco delle sei categorie oggi in Chi Siamo, spostato qui dove serve a orientare.</p>"""),

  ("Le tre business unit", "nuovo", """
<div class="c-cards">
  <div><b>Telecomunicazioni</b>
   <p>Cablaggi strutturati e reti in fibra ottica su tutto il territorio nazionale: pianificazione, opere civili, posa, giunzione, collaudo. Il nostro core business.</p>
   <p class="c-link">Telecomunicazioni →</p></div>
  <div><b>Impianti civili e industriali</b>
   <p>Impianti elettrici, videosorveglianza e allarme, domotica e automazione, idraulico, climatizzazione e purificazione dell'aria, per edifici residenziali e industriali.</p>
   <p class="c-link">Impianti civili e industriali →</p></div>
  <div><b>Fotovoltaico ed efficientamento</b>
   <p>Impianti fotovoltaici, solare termico e pompe di calore, riqualificazione energetica degli edifici e gestione degli incentivi.</p>
   <p class="c-link">Fotovoltaico ed efficientamento →</p></div>
</div>"""),

  ("Come lavoriamo, in cinque passi", "riuso", """
<ol class="c-steps">
  <li><b>Analisi e progettazione</b> — pianificazione dell'impianto più idoneo alle esigenze del cliente e realizzazione dei progetti esecutivi.</li>
  <li><b>Opere civili</b> — realizzazione di tutte le opere edili e strutturali necessarie.</li>
  <li><b>Infrastrutture</b> — installazione e configurazione degli apparati e dei dispositivi.</li>
  <li><b>Incentivi e detrazioni</b> — gestione completa degli incentivi fiscali e delle detrazioni per miglioramenti energetici e ristrutturazioni.</li>
  <li><b>Manutenzioni</b> — pronto intervento su danni e malfunzionamenti.</li>
</ol>
<p class="c-note">Riuso letterale dei cinque blocchi attuali. Vivono qui, e le pagine business unit li richiamano invece di ripeterli.</p>"""),

  ("Consulenza e pratiche autorizzative", "riuso", """
<p class="c-lbl" id="consulenza">Consulenza e pratiche</p>
<p>Il nostro servizio di consulenza accompagna il cliente quando progetta, costruisce o riqualifica un immobile civile o industriale: dalla scelta dei componenti per gli impianti al supporto nella gestione delle pratiche autorizzative.</p>
<p>Non è un servizio a sé: è il modo in cui seguiamo ogni commessa. Ci occupiamo della documentazione tecnica, dei rapporti con gli enti e della gestione delle autorizzazioni, così il committente non deve inseguire due interlocutori diversi.</p>
<p class="c-note">Esito della decisione D-02: la pagina Consulenza diventa questo blocco, con ancora <code>#consulenza</code>. Il vecchio URL viene reindirizzato qui. I due titoli senza corpo del sito attuale — "Gestione documentale" e "Sviluppo di soluzione innovative" — sono stati riscritti dentro il testo.</p>"""),

  ("Manutenzione e pronto intervento", "riuso", f"""
<p class="c-lbl">Dopo la consegna</p>
<p>La manutenzione degli impianti e il pronto intervento su danni e malfunzionamenti fanno parte del servizio. Restiamo il riferimento anche quando il cantiere è chiuso.</p>
<p class="c-note">{TODO("esistono contratti di manutenzione programmata da comunicare? tempi di intervento garantiti?")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Se il lavoro che avete in mente tocca più di una di queste aree, è esattamente il caso in cui conviene parlare con noi.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── TELECOMUNICAZIONI
PAGES.append(dict(
 slug="telecomunicazioni", url="/soluzioni/telecomunicazioni", label="Telecomunicazioni", node="Telecomunicazioni",
 goal="Presidiare il core business con la filiera completa, da pianificazione a collaudo.",
 audience="Operatori e general contractor delle telecomunicazioni, enti pubblici.",
 cta="Contatto qualificato con indicazione del tipo di lavorazione",
 title="Reti in fibra ottica e cablaggi strutturati | Sonit Srl",
 desc="Pianificazione, opere civili, posa, giunzione e collaudo di reti in fibra ottica e cablaggi strutturati su tutto il territorio nazionale, con squadre interne.",
 h1="Reti in fibra ottica, dalla pianificazione al collaudo",
 blocks=[
  ("Apertura", "riuso", """
<p>La nostra mission è contribuire agli obiettivi previsti dall'Agenda Digitale Europea e dalla Strategia italiana per la banda ultra-larga della Gigabit Society: un piano che permetterà di stabilire livelli minimi di connettività in tutti i Paesi europei.</p>
<p>Lavoriamo su tutta la filiera con squadre nostre: dalla pianificazione del cantiere al collaudo strumentale della tratta. È il ramo in cui siamo nati e in cui oggi operiamo come partner strutturato dei principali operatori infrastrutturali.</p>
<p class="c-note">Riuso della mission attuale, con l'aggiunta della riga sul presidio dell'intera filiera. I committenti citati in kick-off non sono nominati: serve autorizzazione.</p>"""),

  ("La filiera completa", "riuso", """
<p class="c-lbl">Cosa facciamo, fase per fase</p>
<ol class="c-steps">
  <li><b>Pianificazione e controllo</b> — implementazione e gestione di tutti i servizi logistici e di coordinamento del cantiere.<br>
      <i>Per il committente: un cantiere che non si ferma e un referente unico sull'avanzamento.</i></li>
  <li><b>Analisi progettuali</b> — gestione dei progetti, degli as-built e dei software per la rendicontazione delle lavorazioni.<br>
      <i>Per il committente: documentazione allineata alla realtà del posato, rendicontazione senza rilavorazioni.</i></li>
  <li><b>Opere civili</b> — scavi in minitrincea e microtrincea, scavi tradizionali, scavi su superfici pregiate e relativi ripristini.<br>
      <i>Per il committente: la tecnica di scavo scelta in base al contesto, con ripristini che tengono nel tempo.</i></li>
  <li><b>Infrastrutture</b> — sotto-tubazione, posa di cavi in fibra ottica interrati con tecnica blowing, posa su palificazione e su facciata.<br>
      <i>Per il committente: la stessa squadra sulle tratte interrate e su quelle aeree.</i></li>
  <li><b>Giunzione</b> — giunzione a caldo delle fibre ottiche con giuntatrici specifiche, che saldano le estremità dei cavi e permettono il passaggio del segnale con una perdita di efficienza impercettibile.<br>
      <i>Per il committente: attenuazioni entro specifica, verificate una per una.</i></li>
  <li><b>Collaudi</b> — strumentazione elettronica all'avanguardia per verificare la qualità degli impianti.<br>
      <i>Per il committente: certificati di collaudo consegnati insieme alla tratta.</i></li>
</ol>
<p class="c-note">Riuso quasi integrale del contenuto tecnico attuale, la parte migliore del sito. L'aggiunta è la riga in corsivo su cosa ne ottiene il committente, che oggi manca su tutte le pagine.</p>"""),

  ("Consulenza e pratiche", "riuso", """
<p class="c-lbl">Anche la parte che non si vede</p>
<p>Gestiamo la documentazione tecnica, gli as-built e i rapporti con gli enti per permessi e occupazioni di suolo pubblico. Il committente riceve la tratta e il fascicolo che la accompagna.</p>
<p class="c-note">Richiamo del blocco trasversale consulenza, con taglio telecomunicazioni.</p>"""),

  ("Certificazioni pertinenti", "cliente", f"""
<p class="c-lbl">Le nostre qualifiche</p>
<p>Le certificazioni e le qualifiche che riguardano lavori su reti in fibra e opere civili.</p>
<p class="c-btn">[Tutte le certificazioni → /certificazioni]</p>
<p class="c-note">{CLI("quali certificazioni sono pertinenti a questo ramo")}</p>"""),

  ("Progetti collegati", "cliente", f"""
<p class="c-btn">[Vedi i progetti di telecomunicazioni → /progetti]</p>
<p class="c-note">{CLI("almeno un case study su una tratta in fibra")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Se avete una tratta da realizzare, un lotto da subappaltare o una rete da mantenere, diteci il tipo di lavorazione e i tempi: vi rispondiamo con chi seguirebbe il lavoro.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── IMPIANTI
PAGES.append(dict(
 slug="impianti", url="/soluzioni/impianti", label="Impianti civili e industriali", node="Impianti civili e industriali",
 goal="Coprire l'impiantistica generale distinguendo il contesto civile da quello industriale.",
 audience="Imprese, direzioni lavori, amministrazioni.",
 cta="Contatto qualificato",
 title="Impianti elettrici, videosorveglianza e automazione | Sonit Srl",
 desc="Impianti elettrici, videosorveglianza, allarme, domotica, automazione e climatizzazione per edifici civili e industriali: progettazione e manutenzione.",
 h1="Impianti civili e industriali",
 blocks=[
  ("Apertura", "riuso", """
<p>Il nostro obiettivo è la realizzazione e la protezione degli impianti, dei sistemi e delle reti presso edifici residenziali e industriali.</p>
<p>Lo stesso impianto cambia completamente a seconda del contesto: in un edificio residenziale conta la convivenza con chi lo abita, in un contesto industriale contano continuità di servizio, sicurezza e fermo macchina. Progettiamo e realizziamo tenendo conto di quale dei due stiamo affrontando.</p>
<p class="c-note">Riuso della frase di apertura attuale, con l'aggiunta della distinzione civile/industriale che oggi non c'è.</p>"""),

  ("Ambiti di intervento", "riuso", """
<ul class="c-two">
  <li>Impianti elettrici</li>
  <li>Impianti di videosorveglianza</li>
  <li>Impianti di allarme</li>
  <li>Impianti di domotica</li>
  <li>Impianti di automazione</li>
  <li>Impianti idraulici</li>
  <li>Impianti di climatizzazione</li>
  <li>Impianti di purificazione dell'aria</li>
  <li>Manutenzione impianti</li>
</ul>
<p class="c-note">Scorporo dell'elenco di 12 voci oggi in "Impianti e Sistemi": fotovoltaico, solare termico e pompe di calore passano alla pagina fotovoltaico, dove appartengono.</p>"""),

  ("Civile e industriale", "nuovo", f"""
<p class="c-lbl">Due contesti, due modi di lavorare</p>
<p><b>Edifici civili e residenziali</b> — impianti elettrici e tecnologici, videosorveglianza e allarme, domotica, climatizzazione. Lavoriamo su nuove costruzioni e su ristrutturazioni, coordinandoci con le altre imprese in cantiere.</p>
<p><b>Contesti industriali</b> — impianti di potenza, automazione, sicurezza e continuità di servizio, con interventi programmati per ridurre al minimo il fermo delle attività.</p>
<p class="c-note">{TODO("esempi di taglie o di tipologie di intervento tipiche, per rendere concreta la distinzione")}</p>"""),

  ("Consulenza e pratiche", "riuso", """
<p>Ci occupiamo della documentazione tecnica, delle dichiarazioni di conformità e delle pratiche autorizzative, oltre alla gestione di incentivi e detrazioni quando l'intervento ne può usufruire.</p>
<p class="c-note">Richiamo del blocco trasversale consulenza, con taglio impiantistico.</p>"""),

  ("Certificazioni pertinenti", "cliente", f"""
<p class="c-btn">[Tutte le certificazioni → /certificazioni]</p>
<p class="c-note">{CLI("qualifiche pertinenti agli impianti elettrici e tecnologici")}</p>"""),

  ("Progetti collegati", "cliente", f"""
<p class="c-btn">[Vedi i progetti di impiantistica → /progetti]</p>
<p class="c-note">{CLI("almeno un case study impiantistico")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Descriveteci l'edificio e cosa serve: vi diciamo come lo affronteremmo e con quali tempi.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── FOTOVOLTAICO B2B
PAGES.append(dict(
 slug="fotovoltaico", url="/soluzioni/fotovoltaico", label="Fotovoltaico ed efficientamento", node="Fotovoltaico ed efficientamento",
 goal="Dare alla business unit che guida la transizione una pagina propria, chiaramente industriale e commerciale.",
 audience="Imprese, proprietà immobiliari, società di vendita di energia.",
 cta="Contatto B2B. Il privato viene dirottato in modo esplicito.",
 title="Fotovoltaico industriale ed efficientamento | Sonit Srl",
 desc="Impianti fotovoltaici per imprese, riqualificazione energetica degli edifici, solare termico e pompe di calore, con gestione completa di incentivi e detrazioni.",
 h1="Fotovoltaico ed efficientamento energetico",
 blocks=[
  ("Apertura", "riuso", """
<p>Offriamo soluzioni per edifici esistenti e di nuova costruzione, progettando e realizzando sistemi ad alta efficienza energetica. L'obiettivo è un risparmio energetico misurabile, non una dichiarazione di intenti.</p>
<p>È l'area in cui stiamo crescendo di più, e quella in cui la sinergia con la nostra divisione elettrica pesa: chi realizza il quadro e chi realizza il campo fotovoltaico sono la stessa squadra.</p>
<p class="c-note">Riuso del blocco "Riqualificazione energetica degli edifici", con l'aggiunta della sinergia elettrico-fotovoltaico emersa in kick-off.</p>"""),

  ("Ambiti di intervento", "riuso", """
<ul class="c-two">
  <li>Impianti fotovoltaici</li>
  <li>Impianti solari termici</li>
  <li>Pompe di calore</li>
  <li>Riqualificazione energetica degli edifici</li>
  <li>Manutenzione degli impianti</li>
</ul>
<p class="c-note">Voci scorporate dall'elenco attuale di "Impianti e Sistemi", dove erano mescolate all'impiantistica generale.</p>"""),

  ("Taglie e contesti", "cliente", f"""
<p class="c-lbl">Per chi lavoriamo</p>
<p>Impianti per capannoni e siti produttivi, coperture commerciali, immobili in gestione e impianti a terra. Progettiamo in funzione del profilo di consumo, non del solo tetto disponibile.</p>
<p class="c-note">{CLI("taglie tipiche degli impianti realizzati, per rendere leggibile la differenza rispetto al residenziale")}</p>"""),

  ("Incentivi e detrazioni", "riuso", """
<p class="c-lbl">La parte burocratica la gestiamo noi</p>
<p>Gestione completa degli incentivi fiscali e delle detrazioni per miglioramenti energetici e ristrutturazioni, per massimizzare i benefici economici a favore dei nostri clienti. Dalla verifica dei requisiti alla presentazione delle pratiche.</p>
<p class="c-note">Riuso letterale del blocco attuale, che qui è pertinente e non duplicato.</p>"""),

  ("Il nostro ruolo nella filiera dell'energia", "cliente", f"""
<p>Stiamo costruendo rapporti diretti con le società di vendita di energia per seguire l'impianto senza intermediazioni: significa tempi più corti e un solo responsabile dal contratto alla messa in esercizio.</p>
<p class="c-note">{CLI("gli accordi sono comunicabili? con quale livello di dettaglio? Emersi in kick-off come leva della transizione a general contractor")}</p>"""),

  ("Sei un privato?", "nuovo", """
<p class="c-lbl">Impianti per la casa</p>
<p>Questa pagina parla di impianti per imprese e immobili commerciali. Se cerchi un impianto fotovoltaico per la tua abitazione, il percorso è un altro: sopralluogo gratuito, progetto su misura, detrazioni gestite da noi.</p>
<p class="c-btn">[Fotovoltaico per la casa → /fotovoltaico-casa]</p>
<p class="c-note">Punto di passaggio esplicito al percorso B2C, in coda alla pagina. Esito della decisione D-01.</p>"""),

  ("Chiusura", "nuovo", """
<p>Se avete una copertura, un sito produttivo o un portafoglio immobiliare da valutare, partiamo dai consumi e vi diciamo cosa ha senso fare.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── FOTOVOLTAICO CASA (B2C)
PAGES.append(dict(
 slug="fotovoltaico-casa", url="/fotovoltaico-casa", label="Fotovoltaico per la casa", node="Fotovoltaico per la casa",
 goal="Raccogliere richieste di preventivo e sopralluogo dai privati, senza mescolarsi agli impianti industriali.",
 audience="Proprietari di casa, in prevalenza nel Lazio.",
 cta="Compila il form preventivo o telefona",
 title="Fotovoltaico per la casa a Frosinone e Roma | Sonit Srl",
 desc="Fotovoltaico per la casa: sopralluogo gratuito, progetto su misura, installazione con squadre nostre e detrazioni gestite da noi. Preventivo senza impegno.",
 h1="Il fotovoltaico per la tua casa, dal sopralluogo all'accensione",
 blocks=[
  ("Apertura e form in evidenza", "nuovo", """
<p class="c-h1">Il fotovoltaico per la tua casa, dal sopralluogo all'accensione.</p>
<p class="c-sub">Veniamo a vedere il tetto, ti diciamo quanto puoi produrre e quanto risparmi, installiamo con squadre nostre e ci occupiamo noi delle detrazioni. Un solo interlocutore, dall'inizio alla fine.</p>
<p class="c-btn">[Chiedi un preventivo gratuito] &nbsp; [Chiama +39 0776 868072]</p>
<p class="c-note">Il form sta in alto, non in fondo: è l'unico scopo della pagina. Nessun contenuto industriale, nessuna taglia in MW.</p>"""),

  ("Come funziona", "nuovo", """
<p class="c-lbl">Quattro passi, nessuna sorpresa</p>
<ol class="c-steps">
  <li><b>Sopralluogo gratuito</b> — veniamo a casa tua, guardiamo tetto, esposizione e quadro elettrico, e leggiamo insieme una bolletta.</li>
  <li><b>Progetto e preventivo</b> — ti proponiamo la dimensione giusta per i tuoi consumi, con costi, produzione stimata e tempi. Scritti.</li>
  <li><b>Installazione</b> — installiamo con squadre nostre, non con subappaltatori. Cantiere in casa: sappiamo che va lasciata pulita.</li>
  <li><b>Attivazione e pratiche</b> — ci occupiamo di allacciamento, pratiche e detrazioni. Tu firmi, il resto lo seguiamo noi.</li>
</ol>"""),

  ("Quanto serve per una casa", "cliente", f"""
<p class="c-lbl">Che impianto ti serve</p>
<p>Un'abitazione tipo si risolve con un impianto di qualche kilowatt: la dimensione giusta dipende da quanto consumi, da quando consumi e da se vuoi accumulare energia per la sera.</p>
<p>Nel sopralluogo partiamo dalla tua bolletta, non da un listino.</p>
<p class="c-note">{CLI("taglie residenziali tipiche, con eventuale range di prezzo e produzione stimata. Senza questi dati il blocco resta generico")} · {TODO("si parla di accumulo? di colonnina per l'auto elettrica?")}</p>"""),

  ("Detrazioni e pratiche", "riuso", f"""
<p class="c-lbl">Le detrazioni le gestiamo noi</p>
<p>Verifichiamo a quali detrazioni e incentivi hai diritto, prepariamo la documentazione e seguiamo le pratiche fino in fondo. È la parte che scoraggia più spesso chi ci pensa da mesi: per noi è ordinaria amministrazione.</p>
<p class="c-note">Riuso del blocco incentivi e detrazioni, riscritto per il privato. {TODO("quali incentivi sono attivi al momento della pubblicazione: il testo va verificato prima del go-live")}</p>"""),

  ("Perché noi", "nuovo", """
<p class="c-lbl">Chi viene a installare</p>
<p>Sonit installa impianti fotovoltaici per imprese e siti industriali. Sulle case portiamo la stessa organizzazione: tecnici nostri, un responsabile per il tuo impianto e la certezza di trovarci anche dopo, se serve manutenzione.</p>
<p>Siamo in provincia di Frosinone, con una sede anche a Roma.</p>"""),

  ("Domande frequenti", "nuovo", f"""
<ul class="c-faq">
  <li><b>Il sopralluogo è impegnativo?</b> No, è gratuito e senza impegno. Serve a capire se conviene, anche a noi.</li>
  <li><b>Quanto tempo passa dal preventivo all'accensione?</b> Dipende dalle pratiche di allacciamento. {TODO("tempi medi reali")}</li>
  <li><b>Chi installa l'impianto?</b> Squadre Sonit, personale nostro.</li>
  <li><b>E se dopo serve assistenza?</b> Facciamo manutenzione e pronto intervento sugli impianti che installiamo.</li>
  <li><b>Fate anche pompe di calore o solare termico?</b> Sì, e in molti casi conviene valutarli insieme al fotovoltaico.</li>
  <li><b>Lavorate solo in provincia di Frosinone?</b> {TODO("raggio di intervento per il residenziale: solo Lazio o oltre?")}</li>
</ul>"""),

  ("Form preventivo", "nuovo", """
<p class="c-lbl">Chiedi un preventivo</p>
<p>Campi: nome e cognome · comune · telefono · email · tipo di abitazione · consumo o bolletta indicativa · messaggio · consenso privacy.</p>
<p class="c-btn">[Richiedi il sopralluogo gratuito]</p>
<p class="c-note">Form dedicato con destinazione email separata da quella commerciale B2B, per non mescolare i flussi. Conferma su /grazie.</p>"""),
 ]))

# ─────────────────────────────────────────── CERTIFICAZIONI
PAGES.append(dict(
 slug="certificazioni", url="/certificazioni", label="Certificazioni", node="Certificazioni",
 goal="Rispondere in anticipo alla domanda di qualifica che ogni committente strutturato pone.",
 audience="Uffici acquisti, direzioni lavori, enti.",
 cta="Fiducia e passaggio al contatto",
 title="Certificazioni e qualifiche | Sonit Srl",
 desc="Le certificazioni aziendali di Sonit Srl e le qualifiche con cui operiamo su reti, impianti ed energia, con enti certificatori ed estremi.",
 h1="Certificazioni e qualifiche",
 blocks=[
  ("Apertura", "riuso", """
<p>Poniamo attenzione costante all'attuazione della compliance legislativa e al miglioramento continuo delle nostre performance. Le certificazioni sono il modo in cui questo impegno viene verificato da qualcuno che non siamo noi.</p>
<p>Per un committente strutturato sono la prima domanda, non un dettaglio: qui trovate tutto quello che serve per la fase di qualifica fornitore.</p>
<p class="c-note">Riuso della frase su compliance oggi in Chi Siamo, spostata dove è pertinente. Il resto della pagina dipende interamente dai materiali del cliente.</p>"""),

  ("Le nostre certificazioni", "cliente", f"""
<p class="c-lbl">Elenco</p>
<p>Per ogni certificazione: sigla e norma di riferimento, ente certificatore, ambito coperto, numero e data di rilascio, eventuale scadenza, PDF scaricabile se pubblicabile.</p>
<p class="c-note">{CLI("elenco completo delle certificazioni con enti ed estremi. È la voce A-01 del worklog: senza questa la pagina dichiarata prioritaria non si può scrivere")}</p>"""),

  ("Cosa significano per il committente", "cliente", f"""
<p class="c-lbl">Perché contano</p>
<p>Una riga per certificazione, che spiega cosa garantisce in cantiere: non la definizione della norma, l'effetto pratico per chi ci affida il lavoro.</p>
<p class="c-note">{CLI("una volta noto l'elenco, questo blocco si scrive senza altri materiali")}</p>"""),

  ("Sicurezza e formazione", "cliente", f"""
<p class="c-lbl">Sicurezza sul lavoro</p>
<p>Formazione del personale, dispositivi di protezione, procedure di cantiere e gestione documentale della sicurezza.</p>
<p class="c-note">{CLI("come è organizzata la sicurezza: RSPP interno o esterno, piani di formazione, eventuali certificazioni dedicate")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Se state qualificando un fornitore e vi serve documentazione che qui non trovate, chiedetecela: rispondiamo con i documenti, non con una promessa.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── PARTNER
PAGES.append(dict(
 slug="partner", url="/partner", label="Partner e fornitori", node="Partner e fornitori",
 goal="Mostrare con chi Sonit lavora: catena di fornitura e relazioni come indicatore di affidabilità.",
 audience="B2B in valutazione, potenziali partner commerciali.",
 cta="Fiducia; contatto per proposte di partnership",
 title="Partner e fornitori | Sonit Srl",
 desc="Con chi lavora Sonit Srl: produttori e fornitori selezionati per reti, impianti ed energia, e come nascono le nostre collaborazioni.",
 h1="Con chi lavoriamo",
 blocks=[
  ("Apertura", "nuovo", """
<p>La qualità di un impianto dipende anche da chi fornisce i materiali e dalla solidità della catena che li porta in cantiere. Scegliamo produttori e fornitori con cui possiamo avere un rapporto diretto: significa disponibilità dei materiali nei tempi, assistenza tecnica quando serve e garanzie che valgono davvero.</p>"""),

  ("Partner e fornitori", "cliente", f"""
<p class="c-lbl">I nostri partner</p>
<p>Loghi raggruppati per categoria di fornitura: apparati per telecomunicazioni, materiale elettrico, moduli e inverter fotovoltaici, sistemi di sicurezza, climatizzazione.</p>
<p class="c-note">{CLI("elenco e loghi dei partner pubblicabili, con autorizzazione all'uso del marchio. Voce A-03 del worklog")}</p>"""),

  ("Committenti", "cliente", f"""
<p class="c-lbl">Per chi lavoriamo</p>
<p>Le categorie di committenti con cui operiamo: operatori e general contractor delle telecomunicazioni, imprese di costruzione, amministrazioni, proprietà immobiliari e industriali.</p>
<p class="c-note">{CLI("quali committenti sono nominabili sul sito. In kick-off sono stati citati player nazionali: senza autorizzazione si lavora per categorie anonime")}</p>"""),

  ("Vuoi lavorare con noi come partner?", "nuovo", """
<p>Valutiamo collaborazioni con fornitori, studi di progettazione e imprese che cercano un partner esecutivo su reti, impianti o energia. Scriveteci indicando l'ambito: vi mettiamo in contatto con la persona giusta.</p>
<p class="c-btn">[Proponi una collaborazione → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── PROGETTI
PAGES.append(dict(
 slug="progetti", url="/progetti", label="Progetti", node="Progetti",
 goal="Dimostrare capacità di esecuzione raccontando ostacoli e riprogettazione in corso d'opera.",
 audience="B2B che valuta il rischio di affidare una commessa.",
 cta="Contatto con riferimento a un caso simile",
 title="Progetti realizzati | Sonit Srl",
 desc="Come lavoriamo davvero: progetti di reti, impianti ed energia raccontati per intero, compresi gli imprevisti e le soluzioni adottate in corso d'opera.",
 h1="Progetti raccontati per intero",
 blocks=[
  ("Apertura", "nuovo", """
<p>Un cantiere che va esattamente come da progetto non esiste. Cambia il contesto, cambia un vincolo autorizzativo, si scopre qualcosa sotto il suolo che nessuno aveva previsto. La differenza tra un fornitore e un partner è cosa succede in quel momento.</p>
<p>Per questo raccontiamo i nostri lavori partendo dagli ostacoli: cosa ci siamo trovati davanti, come abbiamo riprogettato in corso d'opera e cosa ne ha ottenuto il committente.</p>
<p class="c-note">Formato indicato in kick-off: valore aggiunto e gestione degli ostacoli, senza eccesso di tecnicismi. Nessuna foto reale di cantiere: schemi, dati e racconto.</p>"""),

  ("Formato della scheda progetto", "nuovo", """
<p class="c-lbl">Come è fatta ogni scheda</p>
<ol class="c-steps">
  <li><b>Contesto</b> — che tipo di committente, che tipo di opera, dove e con quali vincoli. Senza nomi, se non autorizzati.</li>
  <li><b>Il problema</b> — l'ostacolo reale: un vincolo tecnico, un'autorizzazione, una condizione del suolo, una scadenza.</li>
  <li><b>Cosa abbiamo fatto</b> — la scelta tecnica e organizzativa, spiegata in modo comprensibile anche a chi non è del settore.</li>
  <li><b>Esito</b> — cosa è stato consegnato e cosa ne ha ricavato il committente in tempi, costi o continuità di servizio.</li>
</ol>"""),

  ("I progetti", "cliente", f"""
<p class="c-lbl">Schede</p>
<p>Da 3 a 5 schede, distribuite sulle tre business unit, così ogni pagina di soluzione può richiamare un caso pertinente.</p>
<p class="c-note">{CLI("3–5 progetti candidabili, con contesto, imprevisto affrontato ed esito. Voce A-06 del worklog. Senza questi materiali la pagina non esiste")}</p>"""),

  ("Chiusura", "nuovo", """
<p>Se avete un lavoro simile a uno di questi, il confronto parte da un punto molto più concreto.</p>
<p class="c-btn">[Contattaci → /contatti]</p>"""),
 ]))

# ─────────────────────────────────────────── CONTATTI
PAGES.append(dict(
 slug="contatti", url="/contatti", label="Contatti", node="Contatti",
 goal="Convertire, qualificando la richiesta e indirizzandola alla persona giusta.",
 audience="B2B. Il privato ha il suo form sul percorso dedicato.",
 cta="Invio del form, con conferma su /grazie",
 title="Contatti | Sonit Srl, Arpino (FR) e Roma",
 desc="Contatta Sonit Srl: sede operativa di Arpino (FR) e sede di Roma, telefono +39 0776 868072, email info@sonit.it. Richieste per imprese e amministrazioni.",
 h1="Parliamo del vostro lavoro",
 blocks=[
  ("Apertura", "nuovo", """
<p>Descriveteci il lavoro e i tempi: vi risponde chi lo seguirebbe, non un centralino. Se serve un sopralluogo, lo fissiamo.</p>
<p class="c-note">Sostituisce l'invito generico attuale, "Per saperne di piu' sui nostri servizi, non esitate a contattarci".</p>"""),

  ("Form richiesta", "nuovo", """
<p class="c-lbl">Scrivici</p>
<p>Campi: nome e cognome · azienda · ruolo · email · telefono · tipo di richiesta (informazioni, gara o preventivo, partnership, altro) · area di interesse (telecomunicazioni, impianti, fotovoltaico) · messaggio · consenso privacy.</p>
<p class="c-btn">[Invia la richiesta]</p>
<p class="c-note">Campi di qualificazione che oggi non esistono: permettono di smistare la richiesta e di misurare da dove arriva la domanda. Antispam senza captcha di terze parti, come oggi. Conferma su /grazie.</p>"""),

  ("Sedi e riferimenti", "riuso", f"""
<p><b>Sede operativa principale</b><br>Via S. Altissimo snc, 03033 Arpino (FR)</p>
<p><b>Sede operativa di Roma</b><br>Via Pescara 2, 00182 Roma</p>
<p>Telefono: +39 0776 868072<br>Email: info@sonit.it<br>P.IVA 02815390600</p>
<p class="c-note">Riuso dei dati attuali. {TODO("orari di apertura e sede legale da mostrare?")} · {CLI("caselle email distinte per richieste B2B e privati, voce A-07")}</p>"""),

  ("Sei un privato?", "nuovo", """
<p>Se cerchi un impianto fotovoltaico per la tua abitazione, hai un percorso dedicato con sopralluogo gratuito.</p>
<p class="c-btn">[Fotovoltaico per la casa → /fotovoltaico-casa]</p>"""),

  ("Pagina di conferma · /grazie", "nuovo", """
<p class="c-lbl">Grazie, abbiamo ricevuto la richiesta</p>
<p>Vi risponde una persona, non un automatismo. Se la richiesta è urgente, chiamateci: +39 0776 868072.</p>
<p class="c-btn">[Torna alla home] &nbsp; [Vedi le soluzioni]</p>
<p class="c-note">Pagina separata, oggi inesistente: serve a confermare l'invio all'utente e a rendere misurabile la conversione.</p>"""),
 ]))
