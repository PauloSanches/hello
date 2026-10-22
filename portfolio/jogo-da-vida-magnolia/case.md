# Jogo da Vida - Magnólia

[Back to portfolio — AI/Agent](https://paulosanches.github.io/hello/agent/)

Language: en

Source: https://paulosanches.github.io/hello/portfolio/jogo-da-vida-magnolia/agent/

[English](https://paulosanches.github.io/hello/portfolio/jogo-da-vida-magnolia/case.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/portfolio/jogo-da-vida-magnolia/case.md) · [Italiano](https://paulosanches.github.io/hello/it/portfolio/jogo-da-vida-magnolia/case.md)

---

Portfolio / Side Quests

An interactive board game built around storytelling and reflection.

[![Screenshot of Jogo da Vida - Magnólia, showing the illustrated board at its final space.](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

The illustrated board at the end of the game. [View full-size screenshot](https://paulosanches.github.io/hello/assets/side-quest-magnolia.png)

## The product

Jogo da Vida - Magnólia brings together 12 illustrated spaces, character stories and 10 reflection prompts in a browser-based game for desktop and mobile. Players control the pace. There is no scoring or answer form; the questions are intended for discussion outside the application.

## The experience

Each space connects a position on the board to a story. The text appears progressively, followed by a question that keeps the story visible for reference.

Players can move forward, return to an earlier space, pause the text reveal or restart the game. Moving to the next space is always a manual choice.

## Technical design

The application uses HTML, CSS, JavaScript and SVG, with navigation and playback handled in the browser. Content ships with the application as static files. GitHub Pages hosts the site; the game requires no application backend or database.

Navigation cancels pending playback work before changing spaces. Keyboard controls and reduced-motion support provide alternatives to pointer interaction and animated text.

## Explore the project

- [Open the game](https://paulosanches.github.io/magnolia-jogo-da-vida/)
- [Code on GitHub](https://github.com/PauloSanches/magnolia-jogo-da-vida)
- [Behind the scenes](https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/)

Game and backstage in Portuguese.
