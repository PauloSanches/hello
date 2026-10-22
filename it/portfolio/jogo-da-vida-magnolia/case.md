# Jogo da Vida - Magnólia

[Torna al portfolio — AI/Agent](https://paulosanches.github.io/hello/it/agent/)

Language: it

Fonte: https://paulosanches.github.io/hello/it/portfolio/jogo-da-vida-magnolia/agent/

[English](https://paulosanches.github.io/hello/portfolio/jogo-da-vida-magnolia/case.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/portfolio/jogo-da-vida-magnolia/case.md) · [Italiano](https://paulosanches.github.io/hello/it/portfolio/jogo-da-vida-magnolia/case.md)

---

Portfolio / Side Quests

Un gioco da tavolo interattivo basato su storie e riflessione.

[![Schermata di Jogo da Vida - Magnólia, con il tabellone illustrato nella casella finale.](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

Il tabellone illustrato alla fine del gioco. [Visualizza la schermata a dimensione intera](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

## Il prodotto

Jogo da Vida - Magnólia riunisce 12 caselle illustrate, storie di personaggi e 10 domande di riflessione in un gioco per browser su computer e dispositivi mobili. I giocatori controllano il ritmo. Non ci sono punteggi né moduli di risposta; le domande sono pensate per essere discusse al di fuori dell’applicazione.

## L’esperienza

Ogni casella collega una posizione sul tabellone a una storia. Il testo appare progressivamente, seguito da una domanda che lascia la storia visibile come riferimento.

I giocatori possono avanzare, tornare a una casella precedente, mettere in pausa la comparsa del testo o ricominciare il gioco. Passare alla casella successiva è sempre una scelta manuale.

## Progettazione tecnica

### Architettura in esecuzione

HTML, CSS e SVG definiscono l’interfaccia e il tabellone illustrato. JavaScript gestisce la casella attiva, lo stato della storia e della domanda e le transizioni nel browser. GitHub Pages ospita l’applicazione statica; il gioco non richiede un backend applicativo né un database.

### Riproduzione e navigazione

Un controller dedicato gestisce il job di riproduzione corrente, il timer e gli stati di scrittura, attesa e pausa. Utilizza un intervallo di 24 ms e un’attesa di lettura di 3.000 ms prima di presentare una domanda. La presentazione automatica attende mentre è selezionato del testo, il pannello di lettura ha il focus da tastiera o rimane contenuto non letto sotto la posizione di scorrimento.

La navigazione annulla le operazioni di riproduzione in sospeso, mentre i controlli sullo stato di transizione impediscono movimenti sovrapposti. La pausa o il passaggio della scheda in secondo piano sospendono la pianificazione. Il passaggio tra le caselle del tabellone rimane manuale.

### Layout di lettura e accessibilità

Il testo completo riserva il proprio spazio nel layout prima dell’inizio dell’effetto di scrittura, invece di ridimensionare il fumetto a ogni carattere. Un livello visivo separato gestisce la rivelazione, mentre il testo completo rimane disponibile alle tecnologie assistive.

L’interfaccia supporta la navigazione da tastiera e prefers-reduced-motion. La storia e la domanda rimangono visibili insieme.

### Contenuti e versionamento

Google Sheets ha supportato la modifica collaborativa durante la preparazione. Dopo l’approvazione editoriale, questa dipendenza è stata rimossa e i contenuti definitivi sono stati pubblicati insieme al codice. La narrazione resta così legata a una versione, ma ogni modifica ai contenuti richiede una nuova pubblicazione.

### Test e pubblicazioni

I controlli automatizzati coprono contenuti, navigazione, immagini e layout, integrati da verifiche nel browser a diverse dimensioni dello schermo.

Uno script di pubblicazione scrive lo stesso timestamp UTC nella pagina e in version.json e aggiunge parametri di versione derivati da SHA-256 agli URL di JavaScript e CSS. La modalità di verifica controlla la coerenza dei timestamp; non ricalcola gli hash dei file. I file pubblicati e il comportamento nel browser vengono verificati separatamente per confermare la versione distribuita.

### Strumenti di sviluppo

Hermes Agent e Codex hanno supportato l’implementazione e i test su un MacBook Air M1, con richieste e revisioni tramite Telegram. ChatGPT ha generato le illustrazioni dei personaggi a partire dalle fotografie fornite; Hermes ha preparato e integrato i file. Skill riutilizzabili hanno guidato design, test, debug e revisione. Questi strumenti appartengono al flusso di sviluppo, non all’esecuzione del gioco.

## Esplora il progetto

- [Apri il gioco](https://paulosanches.github.io/magnolia-jogo-da-vida/)
- [Codice su GitHub](https://github.com/PauloSanches/magnolia-jogo-da-vida)
- [Dietro le quinte](https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/)

Gioco e retroscena in portoghese.
