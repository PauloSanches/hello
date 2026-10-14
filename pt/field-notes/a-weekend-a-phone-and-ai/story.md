# O que dá para criar em um fim de semana com um telemóvel e IA?

[Voltar ao portfólio — AI/Agent](https://paulosanches.github.io/hello/pt/agent/)

Language: pt-BR

Fonte: https://paulosanches.github.io/hello/pt/field-notes/a-weekend-a-phone-and-ai/agent/

[English](https://paulosanches.github.io/hello/field-notes/a-weekend-a-phone-and-ai/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/a-weekend-a-phone-and-ai/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/a-weekend-a-phone-and-ai/story.md)

---

IA E ENGENHARIA

Como usei o Codex por chat e voz para construir, testar e publicar meu portfólio.

2 min de leitura

[![Diagrama do setup com instruções por texto e voz no celular, implementação e testes no Codex, commits no GitHub, hospedagem no GitHub Pages, três idiomas e um ciclo de revisão.](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

[Ampliar diagrama](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

Em um fim de semana, construí este portfólio orientando o Codex pelo celular. Enviei meu currículo e fotos, compartilhei referências visuais e defini como queria apresentar minha experiência. Algumas histórias eu escrevi; outras, contei por voz.

Eu conduzia o trabalho com instruções curtas e conferia o resultado no navegador. O Codex editava os arquivos e executava comandos no seu ambiente de desenvolvimento. Pelo celular, eu revisava conteúdo, layout e comportamento, depois orientava os próximos ajustes.

Publiquei o portfólio **de graça no GitHub Pages**, usando **HTML, CSS e JavaScript**, sem utilizar Vercel ou Supabase. Para este projeto, páginas estáticas e interações no navegador atendiam ao que eu queria construir. O Codex versionava as alterações no GitHub, e o fluxo de build e deploy do GitHub Pages publicava os arquivos.

Para oferecer o conteúdo em **inglês, italiano e português do Brasil**, usamos um script em Python que gera as páginas a partir dos arquivos de origem e das traduções. Cada idioma tem URLs próprias, metadados e links para as outras versões. Acrescentamos sitemap, URLs canônicas e dados estruturados para o perfil e os artigos.

Nas interações, incluí Easter eggs que reconhecem `redbull`, `gameday` e `goodmorning`. O JavaScript troca o tema, a foto e uma frase do banner. Variáveis CSS aplicam as cores, e o `sessionStorage` mantém a escolha durante a navegação na mesma aba.

A validação fez parte da entrega. O Codex verificou as páginas em Chromium e WebKit, com diferentes larguras de tela, conferindo imagens, links, traduções e componentes. Minha revisão no celular complementava essas verificações com ajustes de legibilidade, enquadramento e organização.

Concentrei o trabalho na experiência de quem visita: uma apresentação visual própria, navegação responsiva, cards e histórias em páginas dedicadas. Com uma arquitetura simples e hospedagem gratuita, publiquei um portfólio com identidade e interações feitas para o meu perfil, conduzindo o projeto por chat e voz.

## Vamos continuar a conversa

Você está usando IA e agentes nos seus projetos?

[Me chama no LinkedIn](https://www.linkedin.com/in/paulosanches)

Vamos tomar um café virtual e trocar experiências.
