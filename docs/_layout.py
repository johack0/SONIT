# -*- coding: utf-8 -*-
"""Layout dei blocchi: sorgente condivisa fra il Doc 05 (piano wireframe)
e la presentazione cliente (wireframe disegnati). Si modifica solo qui."""

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

# forma del wireframe disegnato per ciascun blocco: (slug, indice) -> forma
# hero        due colonne, testo a sinistra, spazio visivo a destra
# hero-form   come hero, ma a destra il form già visibile
# split       due colonne, testo + spazio visivo contenuto
# narrow      colonna singola stretta, riga di lettura corta
# full        colonna piena
# duo         due colonne di testo affiancate
# trio        colonna piena + tre esempi affiancati
# tinted      fascia su fondo tenue
# numbers     fascia numeri su fondo tenue
# cards       tre card affiancate
# steps       sequenza numerata
# logos       striscia loghi su una riga
# logogrid    griglia loghi per categoria
# certgrid    griglia di schede certificazione
# project     una scheda progetto larga
# projectlist elenco di schede progetto
# highlight   fascia distinta, varco verso il percorso privati
# contact     due colonne: dati sede + mappa
# download    fascia con pulsanti file
# form        form a piena larghezza
# accordion   domande a fisarmonica
# cta         fascia di chiusura con pulsante
# thanks      pagina di conferma, layout centrato
SHAPE = {
 ("home",1):"hero", ("home",2):"numbers", ("home",3):"cards", ("home",4):"steps",
 ("home",5):"tinted", ("home",6):"logos", ("home",7):"project", ("home",8):"highlight",
 ("home",9):"contact",

 ("chi-siamo",1):"narrow", ("chi-siamo",2):"duo", ("chi-siamo",3):"tinted",
 ("chi-siamo",4):"duo", ("chi-siamo",5):"download", ("chi-siamo",6):"cta",

 ("soluzioni",1):"narrow", ("soluzioni",2):"full", ("soluzioni",3):"cards",
 ("soluzioni",4):"steps", ("soluzioni",5):"split", ("soluzioni",6):"tinted",
 ("soluzioni",7):"cta",

 ("telecomunicazioni",1):"split", ("telecomunicazioni",2):"steps",
 ("telecomunicazioni",3):"narrow", ("telecomunicazioni",4):"tinted",
 ("telecomunicazioni",5):"project", ("telecomunicazioni",6):"cta",

 ("impianti",1):"split", ("impianti",2):"full", ("impianti",3):"duo",
 ("impianti",4):"narrow", ("impianti",5):"tinted", ("impianti",6):"project",
 ("impianti",7):"cta",

 ("fotovoltaico",1):"split", ("fotovoltaico",2):"full", ("fotovoltaico",3):"trio",
 ("fotovoltaico",4):"tinted", ("fotovoltaico",5):"narrow", ("fotovoltaico",6):"highlight",
 ("fotovoltaico",7):"cta",

 ("fotovoltaico-casa",1):"hero-form", ("fotovoltaico-casa",2):"steps",
 ("fotovoltaico-casa",3):"split", ("fotovoltaico-casa",4):"tinted",
 ("fotovoltaico-casa",5):"duo", ("fotovoltaico-casa",6):"accordion",
 ("fotovoltaico-casa",7):"form",

 ("certificazioni",1):"narrow", ("certificazioni",2):"certgrid",
 ("certificazioni",3):"full", ("certificazioni",4):"narrow", ("certificazioni",5):"cta",

 ("partner",1):"narrow", ("partner",2):"logogrid", ("partner",3):"full", ("partner",4):"cta",

 ("progetti",1):"narrow", ("progetti",2):"steps", ("progetti",3):"projectlist",
 ("progetti",4):"cta",

 ("contatti",1):"narrow", ("contatti",2):"form", ("contatti",3):"contact",
 ("contatti",4):"highlight", ("contatti",5):"thanks",
}
