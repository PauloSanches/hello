# Portfolio design guidelines

## Purpose and language

Help visitors understand Paulo Sanches’s architecture experience, leadership responsibilities and selected work, then contact him. All visitor-facing copy, metadata, accessibility labels and feedback must be in English. Write directly, with concrete responsibilities and outcomes grounded in the supplied documents.

## Visual system

Retain the portfolio’s sage and forest palette: warm paper `#f7f8f2`, primary ink `#1b2925`, muted text `#536356`, accent `#bddf89`, dark background `#111b19`, and dark-surface text `#f0f5e9`. Use self-hosted Space Grotesk for headings and Manrope for body text. Preserve readable contrast, visible keyboard focus and generous spacing.

The opening presents Paulo’s name and actual role alongside a diagram connecting people, architecture and delivery. Selected work uses a featured architecture case, concise project summaries and expandable evidence. Expertise links back to relevant projects. Career history and credentials precede direct contact options.

## Interaction and motion

Use motion to explain connections or preserve orientation. The hero diagram runs one finite introductory sequence. Project filtering animates position changes with transforms; newly shown projects have a short entrance. Approach descriptions transition when selected. Native case disclosures use a bounded height transition. Most interactions last 160–280 ms; the diagram route takes 1000 ms.

Avoid autoplay loops, scroll hijacking, hidden-on-load content and decorative effects that obstruct reading. Respect `prefers-reduced-motion` and the persistent footer animation switch. All essential content must work without JavaScript. Interactive controls should provide at least 44 px targets where practical, keyboard support and explicit state.

## Reference use

- Watermelon UI: component hierarchy and restrained interaction; no component source copied.
- Motion Primitives: concise state transitions and animated disclosure patterns, implemented here with native browser APIs.
- The supplied Instagram Reel: publicly accessible descriptive ideas only, including expertise grouping; the video itself was not inspected.
- Kimi Antonelli: structural organisation reference. Its CSS was inaccessible during research, so no exact colour or font match is claimed.
- Vengeance UI, Uiverse and Animate UI: interaction references, adapted to this static site without React dependencies. No third-party component code copied.

Do not invent portraits, testimonials, client results or professional claims. Do not expose private source documents or internal financial metrics. Preserve relative URLs for GitHub Pages under `/hello/`.
