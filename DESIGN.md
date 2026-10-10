# Portfolio design guidelines

## Purpose and language

Help visitors understand Paulo Sanches’s architecture experience, leadership responsibilities and selected work, then contact him. All visitor-facing copy, metadata, accessibility labels and feedback must be in English. Write directly, with concrete responsibilities and outcomes grounded in the supplied documents.

## Visual system

The user selected https://kimiantonelli.online/ as the explicit reference for layout, colour and typography. Its live page and stylesheet were successfully inspected on 10 October 2026. This replaces the earlier sage/forest direction.

Use the observed dark palette: background `#060608`, alternate section `#0a0a0d`, cards `#0e0e11`, deep section `#101014`, foreground `#eceef2`, headings `#f4f5f7`, muted text `#949aa6`, and teal `#2dd4bf`. Borders are adapted to `#26262d` for legibility. Preserve visible keyboard focus and readable contrast.

Use Exo 2 for display typography and Inter for body text, as confirmed in the reference CSS. Both are self-hosted as Latin-subset variable WOFF2 fonts sourced from Google Fonts, with their Open Font Licenses included. Display headings use bold weights, tight line height and negative tracking no tighter than -0.03em. The hero name is uppercase with a teal surname.

Adapt the observed composition: compact sticky navigation, a slim contextual strip, a two-column hero, a six-cell facts strip, centred section headings with short teal dividers, bordered project cards, career timeline and a deep-neutral contact section. At mobile widths the hero stacks and the facts form two rows. The hero diagram represents Paulo’s work; no reference photography, sports statistics or branding is reused.

## Interaction and motion

Use motion to explain connections or preserve orientation. The hero diagram runs one finite introductory sequence. Project filtering animates position changes with transforms; newly shown projects have a short entrance. Approach descriptions transition when selected. Native case disclosures use a bounded height transition. Most interactions last 160–280 ms; the diagram route takes 1000 ms.

Avoid autoplay loops, scroll hijacking, hidden-on-load content and decorative effects that obstruct reading. Respect `prefers-reduced-motion` and the persistent footer animation switch. All essential content must work without JavaScript. Interactive controls should provide at least 44 px targets where practical, keyboard support and explicit state.

## Reference use

- Watermelon UI: component hierarchy and restrained interaction; no component source copied.
- Motion Primitives: concise state transitions and animated disclosure patterns, implemented here with native browser APIs.
- The supplied Instagram Reel: publicly accessible descriptive ideas only, including expertise grouping; the video itself was not inspected.
- Kimi Antonelli: primary visual reference. Live dark presentation and CSS `/_next/static/css/ff7e826600485e4a.css` inspected; Exo 2, Inter, dark neutral surfaces, teal accents and composition confirmed. Earlier CSS access limitations no longer apply.
- Vengeance UI, Uiverse and Animate UI: interaction references, adapted to this static site without React dependencies. No third-party component code copied.

Do not invent portraits, testimonials, client results or professional claims. Do not expose private source documents or internal financial metrics. Preserve relative URLs for GitHub Pages under `/hello/`.
