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

The layout uses a white and black palette, large sans-serif opening text, serif section headings, monospaced labels and fine rules. Its visual direction follows [Lucas Montano's website](https://lucasmontano.com/). System font stacks require no font downloads. The page opens directly with a full-width dark banner occupying 56% of the viewport height. Paulo's colourised portrait appears against a dark charcoal-grey (#262626) background and shifts to the right, with his chosen game-day statement on the left. The image fills the banner height. A continuous linear mask fades from transparent at the photo's left edge to opaque at its right edge, proportional to the photo's own width; the mask uses both standard and WebKit properties. A subtle grid shares the portrait mask. The decorative ruler starts below the banner and becomes the project timeline. It is 20px wide on desktop and 12px on mobile. Flexible grid tracks and text wrapping keep headings and navigation inside the viewport; project rows stack into one column at 600px and below. A shared viewport-height variable keeps the banner and ruler aligned, with small viewport units enabled only when supported. On mobile, the statement sits at the lower left. Short viewports use smaller type and vertical spacing to keep the statement inside the banner.

The banner uses one continuous headline: “Welcome, human or agent — I’m Paulo Sanches and every day is game day. Let’s go!” The headline appears as a solid uppercase block with one type size and weight, compact line spacing and natural wrapping across screen widths. A simple underlined “Let’s talk” link leads directly to Paulo's LinkedIn profile. The link has a minimum 44px target, visible keyboard focus and an accessible notice that it opens LinkedIn in a new tab. Extra spacing adjustments keep it inside the banner in short landscape viewports. There is no page header. A white profile section follows the banner with the approved headline “I help companies transform their business through technology and AI, working with their teams and AI agents from strategy to execution.”, set in bold uppercase sans-serif type with responsive wrapping. The ruler continues alongside this section. A black navigation band follows the profile, with five anchor links: Experience, Field Notes, Mindset, Contributions and Certifications. Links use a two-column grid on desktop, with the final Certifications link spanning both columns, and one full-width row per link on mobile; hover and keyboard focus invert the colours. SVG arrows avoid font-dependent symbols, and links and anchor focus work without JavaScript. The project timeline, field notes, mindset, contributions, certifications and contact follow, with section numbers running from 01 through 07. Mindset and Contributions contain the approved headings and “Coming soon.” placeholders. Certifications lists 25 credentials from the supplied LinkedIn screenshots, newest first. The three latest are visible initially; a native “Show more (22)” disclosure reveals the rest and switches to “Show less”. Each entry includes its issuer, issue month and expiry month where supplied. Only the three most recent projects are initially visible. A full-width dark disclosure, separated from the last project, shows “Showing 3 of 9 experiences” and “View 6 earlier experiences”. Opening it reveals the six earlier projects and changes the text to “Showing all 9 experiences” and “Show only the 3 latest experiences”. The two lists preserve the complete newest-to-oldest order. Project contributions and two stories also expand through native disclosures. Essential content, the links and disclosures work without JavaScript. JavaScript only refreshes the footer's year. The operating system's reduced-motion preference disables smooth scrolling and transitions.

JavaScript syntax, HTML structure, internal links and local assets were checked. Chromium checks at viewport widths of 320, 390, 760 and 1440 pixels verified that three projects are initially visible, expansion reveals all nine, and collapsing restores the first three. Enter/Space activation, keyboard focus order, nested project disclosures and the same flow with JavaScript disabled were checked. The profile text fits without horizontal scrolling and the portrait loads.

The navigation and placeholder sections follow the approved layout. LinkedIn is the only contact destination in the hero and contact section; the published page contains no email address or telephone link. The certification anchor, keyboard navigation and LinkedIn contact were checked in Chromium and Linux WebKit at widths of 280, 320, 390, 800 and 1440 pixels, with no horizontal overflow when disclosures were open or closed. All tracked public files were scanned for email addresses and contact URI schemes.

## Content

All visitor-facing content is in English. Project dates, contributions and the people and AI stories come from the supplied CV and career highlights. The security incident card contains only a teaser based on Paulo's description; incident details and outcomes have not been inferred. Clients are described by sector. Original attachments, private financial metrics, telephone numbers and personal email addresses are excluded from the public site.

Horizontal-overflow checks in Chromium and Linux WebKit each covered 23 viewport widths from 280 to 1440 pixels with all disclosures both closed and open. The document stayed within the viewport, menu labels did not overlap their arrows, and project titles stayed inside their columns. Project heading sizes also adapt on narrow phones to avoid awkward word breaks.

The credentials section includes certifications, completed courses and professional recognition. Names and month-level dates were transcribed from six LinkedIn screenshots and overlapping entries were deduplicated. The repeated word in “SAFe Agilist Certification Certification” was removed for display. Expiry dates are shown as dates rather than inferred current-validity badges. Credential URLs were not visible in the screenshots, so no verification links were inferred. Credential IDs and the screenshots themselves are not published.

The populated credentials section was verified in Chromium and Linux WebKit at widths of 280, 320, 390, 760, 800, 1100 and 1440 pixels with JavaScript disabled. Enter and Space expand and collapse the list, the labels and item counts update, and keyboard focus stays on the disclosure. All 25 names, issuers and issue dates, plus the eight supplied expiry dates, were checked against the transcription. No horizontal overflow was found with all page disclosures open or closed; LinkedIn remains the only external contact link.

## Credential issuer icons

Each credential displays its issuer's logo beside the title, following the icons Paulo identified in the LinkedIn screenshots. These are issuer marks, not individual earned-badge verification images. Google Cloud's actual logo replaces the generic company placeholder visible in the screenshots. AWS and SAFe use the official variants available from their sources. All six original assets are stored locally under `assets/issuers/`, loaded lazily, and fitted without cropping or changing their colours. Decorative empty alt text avoids repeating the adjacent issuer name. The reserved square size prevents layout shifts, and the icon/text grid adapts to small screens.

All 25 issuer mappings and image loads were verified in Chromium and Linux WebKit at widths from 280 to 1440 pixels. The certification disclosure still works by keyboard without JavaScript, and the page has no horizontal overflow with disclosures open or closed. Source assets were checked against their downloaded originals.

| Asset | Official source |
| --- | --- |
| `deel.svg` | [Deel website wordmark](https://website-media.deel.com/logo_revamp_white_3237bd2303.svg) |
| `accenture.png` | [Accenture issuer profile](https://www.credly.com/organizations/accenture/badges), [image](https://images.credly.com/images/5d71fd0f-1408-425d-a617-9c7d17b7e065/blob.png) |
| `aws.png` | [AWS static CDN wordmark](https://a0.awsstatic.com/libra-css/images/logos/aws_smile-header-desktop-en-white_59x35@2x.png) |
| `google-cloud.png` | [Google-hosted product icon](https://www.gstatic.com/images/branding/product/2x/google_cloud_64dp.png) |
| `safe.png` | [SAFe issuer profile](https://www.credly.com/organizations/scaled-agile/badges), [image](https://images.credly.com/images/34405e63-6468-4b08-90c3-ccb22c735b13/blob) |
| `scrum-alliance.png` | [Scrum Alliance support](https://support.scrumalliance.org/), [image](https://support.scrumalliance.org/hc/theming_assets/01J94ZG0G5EN0Z891XQZ40VMQM) |

The current banner portrait was colourised from the existing black-and-white image with natural tones and a dark grey backdrop. The generated image is served as an optimised WebP with its original 1122×1402 framing. The grayscale CSS filter has been removed. The 56% viewport height, proportional fade, right offset, grid and existing text are preserved.

The colour banner was verified in Chromium and Linux WebKit at 320×740, 390×844, 844×390 and 1440×900. Checks covered image decoding and colour, the computed grey background, unchanged banner height, fade and grid, text containment, and absence of horizontal overflow. Mobile and desktop screenshots were inspected.

Main content sections use full-width 2px top borders and alternate white and light-grey backgrounds to distinguish their boundaries. Section labels use contrasting black backgrounds and white text. Field Notes and the contact card retain white interiors on grey section backgrounds. The original narrow ruler and timeline geometry are preserved. The experience disclosure is a separate full-width list control; individual project detail links keep their inline appearance. All disclosure behaviour remains native HTML with no JavaScript dependency.

Section boundaries and the experience control were checked in Chromium and Linux WebKit at 280, 320, 390, 760, 800, 1100 and 1440 pixels with JavaScript disabled. Enter/Space toggle the six earlier experiences, visible counts and labels match each state, and project-level disclosures work independently. Full-width boundaries, all credential image loads and absence of horizontal overflow were verified with disclosures both open and closed. Mobile and desktop screenshots were reviewed.
