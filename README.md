# Paulo Sanches · Portfolio

An English-language portfolio based on Paulo’s supplied career documents. Built with static HTML, CSS and JavaScript and published at https://paulosanches.github.io/hello/.

## Local development

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/. No build step or runtime dependencies are required. Content lives in `index.html`, styles in `assets/style.css`, and interaction logic in `assets/app.js`.

## GitHub Pages

In **Settings → Pages**, choose **Deploy from a branch**, branch **main**, folder **/ (root)**. Pushing to `main` triggers GitHub’s **pages build and deployment** workflow. The `.nojekyll` file enables direct static publishing; relative asset URLs support the `/hello/` project path.

## Design and accessibility

The site uses self-hosted Exo 2 and Inter fonts, with their Open Font Licenses in `assets/fonts/`. See `DESIGN.md` for the visual system and motion rules.

Project filters, approach controls and case disclosures use short animations. A persistent animation switch and the operating system’s reduced-motion preference control motion. Essential content, navigation and native disclosures work without JavaScript. Mobile navigation supports Escape and keyboard focus restoration.

Browser validation covers widths from 320 to 1440 pixels, keyboard interaction, project filtering, reduced motion, clipboard feedback and JavaScript-disabled use. An axe-core WCAG A/AA scan complements manual visual checks; automated checks do not establish complete accessibility conformance.

## Content

All visitor-facing content must remain in English. Professional claims are based on the supplied documents and distinguish individual contributions from team outcomes. Clients are described by sector. Original attachments, private financial metrics and telephone numbers are excluded from the public site.

Credential dates reflect the source documents, not independent verification of current certification status. Internal credentials are separated from external certifications. The AWS Solutions Architect date is omitted because the sources disagree.
