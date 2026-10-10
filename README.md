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

The layout uses a white and black palette, a large sans-serif name, serif headings, monospaced labels and fine rules. Its visual direction follows [Lucas Montano's website](https://lucasmontano.com/). System font stacks require no font downloads. The hero's PS monogram is a typographic composition.

The page opens with a welcoming personal introduction, followed by a timeline organised by projects and a section of stories. Project contributions and two stories expand through native disclosures. Essential content, navigation and disclosures work without JavaScript. Mobile navigation supports Escape and keyboard focus restoration. The operating system's reduced-motion preference disables smooth scrolling and transitions.

JavaScript syntax, HTML structure, internal links and local assets were checked. The revised layout has not been validated in a browser because browser execution is unavailable in the current environment.

## Content

All visitor-facing content is in English. Project dates, contributions and the people and AI stories come from the supplied CV and career highlights. The security incident card contains only a teaser based on Paulo's description; incident details and outcomes have not been inferred. Clients are described by sector. Original attachments, private financial metrics and telephone numbers are excluded from the public site.
