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

### Runtime architecture

HTML, CSS and SVG define the interface and illustrated board. JavaScript manages the active space, story/question state and transitions in the browser. GitHub Pages serves the static application; the game requires no application backend or database.

### Playback and navigation

A dedicated playback controller manages the current job, timer and typing, waiting and paused states. It uses a 24 ms timer step and a 3,000 ms reading delay before presenting a question. Automatic presentation waits while text is selected, the reading panel has keyboard focus or unread content remains below the scroll position.

Navigation cancels pending playback work, while busy-state guards prevent overlapping transitions. Pausing or hiding the tab suspends scheduling. Moving between board spaces remains manual.

### Reading layout and accessibility

The full text reserves its layout space before the typing effect begins, rather than resizing the bubble with each character. A separate visual layer handles the reveal while the complete text remains available to assistive technology.

The interface supports keyboard navigation and prefers-reduced-motion. Story and question remain visible together.

### Content and versioning

Google Sheets supported collaborative editing during preparation. After editorial approval, that dependency was removed and the final content was published alongside the code. This keeps the narrative tied to a release, at the cost of requiring a new deployment for content changes.

### Testing and releases

Automated checks cover content, navigation, images and layout, complemented by browser verification at different viewport sizes.

A release script writes the same UTC timestamp into the page and version.json, and adds SHA-256-derived version parameters to JavaScript and CSS URLs. Its check mode verifies timestamp consistency; it does not recalculate asset hashes. Published files and browser behavior are checked separately to confirm the delivered revision.

### Development tooling

Hermes Agent and Codex supported implementation and testing on a MacBook Air M1, with requests and reviews through Telegram. ChatGPT generated character illustrations from supplied photographs; Hermes prepared and integrated the assets. Reusable skills guided design, testing, debugging and review. These tools belong to the development workflow, not the game's runtime.

## Explore the project

- [Open the game](https://paulosanches.github.io/magnolia-jogo-da-vida/)
- [Code on GitHub](https://github.com/PauloSanches/magnolia-jogo-da-vida)
- [Behind the scenes](https://paulosanches.github.io/magnolia-jogo-da-vida/backstage/)

Game and backstage in Portuguese.
