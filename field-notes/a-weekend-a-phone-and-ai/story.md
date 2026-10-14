# What can you build in a weekend with a phone and AI?

[Back to portfolio — AI/Agent](https://paulosanches.github.io/hello/agent/)

Language: en

Source: https://paulosanches.github.io/hello/field-notes/a-weekend-a-phone-and-ai/agent/

[English](https://paulosanches.github.io/hello/field-notes/a-weekend-a-phone-and-ai/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/a-weekend-a-phone-and-ai/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/a-weekend-a-phone-and-ai/story.md)

---

AI & ENGINEERING

How I used Codex through text and voice to build, test and publish my portfolio.

2 min read

[![Setup diagram showing phone instructions by text and voice, Codex implementation and checks, GitHub commits, GitHub Pages hosting, three language versions and a review loop.](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

[View full-size diagram](https://paulosanches.github.io/hello/assets/portfolio-build-setup.webp?v=f8526c37b759)

Over a weekend, I built this portfolio by guiding Codex from my phone. I shared my CV and photos, provided visual references and defined how I wanted to present my experience. I wrote some stories and dictated others.

I directed the work with short instructions and reviewed the results in the browser. Codex edited the files and ran commands in its development environment. From my phone, I reviewed the content, layout and behaviour, then guided the next changes.

I published the portfolio with **free hosting on GitHub Pages**, using **HTML, CSS and JavaScript**, without Vercel or Supabase. Static pages and browser-side interactions covered what I wanted to build. Codex committed the changes to GitHub, and the GitHub Pages build and deployment workflow published the files.

To provide the content in **English, Italian and Brazilian Portuguese**, we used a Python script to generate pages from the source files and translations. Each language has its own URLs, metadata and links to the other versions. We added a sitemap, canonical URLs and structured data for the profile and articles.

For the interactions, I included Easter eggs that recognise `redbull`, `gameday` and `goodmorning`. JavaScript switches the theme, portrait and a phrase in the banner. CSS variables apply the colours, while `sessionStorage` preserves the selection as visitors navigate within the same tab.

Validation was part of the delivery. Codex checked the pages in Chromium and WebKit at different viewport widths, testing images, links, translations and components. My reviews on the phone complemented those checks with adjustments to readability, framing and organisation.

I focused on the visitor experience: a visual identity of my own, responsive navigation, cards and dedicated story pages. With a simple architecture and free hosting, I published a portfolio with interactions tailored to my profile, directing the project through text and voice.

## Continue the conversation

Are you using AI and agents in your projects?

[Message me on LinkedIn](https://www.linkedin.com/in/paulosanches)

Let’s have a virtual coffee and compare experiences.
