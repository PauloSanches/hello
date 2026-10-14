# Cosa puoi creare in un fine settimana con un telefono e l’IA?

[Torna al portfolio — AI/Agent](https://paulosanches.github.io/hello/it/agent/)

Language: it

Fonte: https://paulosanches.github.io/hello/it/field-notes/a-weekend-a-phone-and-ai/agent/

[English](https://paulosanches.github.io/hello/field-notes/a-weekend-a-phone-and-ai/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/a-weekend-a-phone-and-ai/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/a-weekend-a-phone-and-ai/story.md)

---

IA E INGEGNERIA

Come ho usato Codex tramite testo e voce per creare, testare e pubblicare il mio portfolio.

2 min di lettura

[![Diagramma del setup con istruzioni tramite testo e voce dal telefono, implementazione e test in Codex, commit su GitHub, hosting su GitHub Pages, tre lingue e un ciclo di revisione.](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

[Ingrandisci il diagramma](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

In un fine settimana, ho creato questo portfolio guidando Codex dal telefono. Ho condiviso il mio CV e le foto, fornito riferimenti visivi e definito come volevo presentare la mia esperienza. Ho scritto alcune storie e ne ho dettate altre.

Guidavo il lavoro con istruzioni brevi e verificavo i risultati nel browser. Codex modificava i file ed eseguiva comandi nel suo ambiente di sviluppo. Dal telefono rivedevo contenuti, layout e comportamento, poi indicavo le modifiche successive.

Ho pubblicato il portfolio con **hosting gratuito su GitHub Pages**, usando **HTML, CSS e JavaScript**, senza Vercel o Supabase. Le pagine statiche e le interazioni nel browser rispondevano a ciò che volevo creare. Codex registrava le modifiche su GitHub, e il workflow di build e deploy di GitHub Pages pubblicava i file.

Per offrire i contenuti in **inglese, italiano e portoghese brasiliano**, abbiamo usato uno script Python che genera le pagine dai file sorgente e dalle traduzioni. Ogni lingua ha URL propri, metadati e link alle altre versioni. Abbiamo aggiunto una sitemap, URL canonici e dati strutturati per il profilo e gli articoli.

Nelle interazioni ho incluso Easter egg che riconoscono `redbull`, `gameday` e `goodmorning`. JavaScript cambia il tema, la foto e una frase nel banner. Le variabili CSS applicano i colori, mentre `sessionStorage` conserva la scelta durante la navigazione nella stessa scheda.

La validazione faceva parte della consegna. Codex verificava le pagine in Chromium e WebKit con diverse larghezze dello schermo, controllando immagini, link, traduzioni e componenti. Le mie revisioni sul telefono completavano questi controlli con modifiche alla leggibilità, all’inquadratura e all’organizzazione.

Mi sono concentrato sull’esperienza di chi visita: un’identità visiva personale, navigazione responsive, card e pagine dedicate alle storie. Con un’architettura semplice e hosting gratuito, ho pubblicato un portfolio con interazioni pensate per il mio profilo, guidando il progetto tramite testo e voce.

## Continuiamo la conversazione

Stai usando IA e agenti nei tuoi progetti?

[Scrivimi su LinkedIn](https://www.linkedin.com/in/paulosanches)

Prendiamoci un caffè virtuale e scambiamoci esperienze.
