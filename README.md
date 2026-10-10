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

The layout uses a white and black palette, large sans-serif opening text, serif section headings, monospaced labels and fine rules. Its visual direction follows [Lucas Montano's website](https://lucasmontano.com/). System font stacks require no font downloads. The page opens directly with a full-width dark banner occupying 56% of the viewport height. Paulo's black-and-white portrait shifts to the right, with his chosen game-day statement on the left. The image fills the banner height. A continuous linear mask fades from transparent at the photo's left edge to opaque at its right edge, proportional to the photo's own width; the mask uses both standard and WebKit properties. A subtle grid shares the portrait mask. The decorative ruler starts below the banner and becomes the project timeline. A shared viewport-height variable keeps the banner and ruler aligned, with small viewport units enabled only when supported. On mobile, the statement sits at the lower left. Short viewports use smaller type and vertical spacing to keep the statement inside the banner.

The banner contains only the game-day statement and the signature “I am Paulo Sanches. I get things done.” There is no page header or menu. The project timeline and stories follow the banner. Project contributions and two stories expand through native disclosures. Essential content, the skip link and disclosures work without JavaScript. JavaScript only refreshes the footer's year. The operating system's reduced-motion preference disables smooth scrolling and transitions.

JavaScript syntax, HTML structure, internal links and local assets were checked. The revised layout has not been validated in a browser because browser execution is unavailable in the current environment.

## Content

All visitor-facing content is in English. Project dates, contributions and the people and AI stories come from the supplied CV and career highlights. The security incident card contains only a teaser based on Paulo's description; incident details and outcomes have not been inferred. Clients are described by sector. Original attachments, private financial metrics and telephone numbers are excluded from the public site.
