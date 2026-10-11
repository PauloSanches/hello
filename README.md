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

The banner uses one continuous headline: “Welcome, human or agent — I’m Paulo Sanches and every day is game day. Let’s go!” The headline appears as a solid uppercase block with one type size and weight, compact line spacing and natural wrapping across screen widths. A simple underlined “Let’s talk” link leads directly to Paulo's LinkedIn profile. The link has a minimum 44px target, visible keyboard focus and an accessible notice that it opens LinkedIn in a new tab. Extra spacing adjustments keep it inside the banner in short landscape viewports. There is no page header. A white profile section follows the banner with the approved headline “I help companies transform their business through technology and AI, working with their teams and AI agents from strategy to execution.”, set in bold uppercase sans-serif type with responsive wrapping. The ruler continues alongside this section. A black navigation band follows the profile, with five anchor links: Experience, Field Notes, Mindset, Contributions and Certifications. Links use a two-column grid on desktop, with the final Certifications link spanning both columns, and one full-width row per link on mobile; hover and keyboard focus invert the colours. SVG arrows avoid font-dependent symbols, and links and anchor focus work without JavaScript. The project timeline, field notes, mindset, contributions, certifications and contact follow, with section numbers running from 01 through 07. Mindset retains its “Coming soon.” placeholder. Contributions features Paulo’s participation in the Cubo for Devs masterclass on becoming a Tech Lead, with a direct link to the recording, and a photo from FlashCamp 2010. These entries appear as vertical cards in a native swipe carousel, using the same track, controls and keyboard behavior as Certifications. Certifications presents all 25 credentials from the supplied LinkedIn screenshots as cards in a native horizontal carousel, ordered by relevance to Paulo’s profile and technical depth. Each card includes its issuer logo, name, a short description of its scope, issue month and expiry month where supplied. Cards use compact spacing and natural heights, with dates following the text rather than being pushed to a fixed bottom edge. Mobile shows one card with a glimpse of the next; wider screens show two or three cards plus a preview. Horizontal scrolling stays inside the track, with native swipe and scroll snapping. Optional arrow buttons, a visible position count and Arrow Left/Right, Home and End keyboard navigation enhance the carousel. The track retains list semantics for screen readers. Only the three most recent projects are initially visible. A full-width dark disclosure, separated from the last project, shows “Showing 3 of 9 experiences” and “View 6 earlier experiences”. Opening it reveals the six earlier projects and changes the text to “Showing all 9 experiences” and “Show only the 3 latest experiences”. The two lists preserve the complete newest-to-oldest order. Project contributions and two stories also expand through native disclosures. Essential content, the links and disclosures work without JavaScript. JavaScript refreshes the footer's year and adds the carousel controls; native swiping and scrolling remain available without it. The carousel does not auto-advance. The operating system's reduced-motion preference disables smooth scrolling and transitions.

JavaScript syntax, HTML structure, internal links and local assets were checked. Chromium checks at viewport widths of 320, 390, 760 and 1440 pixels verified that three projects are initially visible, expansion reveals all nine, and collapsing restores the first three. Enter/Space activation, keyboard focus order, nested project disclosures and the same flow with JavaScript disabled were checked. The profile text fits without horizontal scrolling and the portrait loads.

The navigation and placeholder sections follow the approved layout. LinkedIn is the only contact destination in the hero and contact section; the published page contains no email address or telephone link. The certification anchor, keyboard navigation and LinkedIn contact were checked in Chromium and Linux WebKit at widths of 280, 320, 390, 800 and 1440 pixels, with no horizontal overflow when disclosures were open or closed. All tracked public files were scanned for email addresses and contact URI schemes.

## Content

All visitor-facing content is in English. Project dates, contributions and the people and AI stories come from the supplied CV and career highlights. The security incident card contains only a teaser based on Paulo's description; incident details and outcomes have not been inferred. Clients are described by sector. Original attachments, private financial metrics, telephone numbers and personal email addresses are excluded from the public site.

Horizontal-overflow checks in Chromium and Linux WebKit each covered 23 viewport widths from 280 to 1440 pixels with all disclosures both closed and open. The document stayed within the viewport, menu labels did not overlap their arrows, and project titles stayed inside their columns. Project heading sizes also adapt on narrow phones to avoid awkward word breaks.

The credentials section includes certifications, completed courses and professional recognition. Names and month-level dates were transcribed from six LinkedIn screenshots and overlapping entries were deduplicated. The repeated word in “SAFe Agilist Certification Certification” was removed for display. Expiry dates are shown as dates rather than inferred current-validity badges. Credential URLs were not visible in the screenshots, so no verification links were inferred. Credential IDs and the screenshots themselves are not published.

The certification carousel was verified in Chromium and Linux WebKit at widths of 280, 320, 390, 760, 800, 1100 and 1440 pixels. Checks covered arrows, keyboard navigation, scroll bounds, position counts, reduced-motion behavior, access to the last card and native scrolling with JavaScript disabled. Chromium touch emulation verified horizontal swiping and vertical page scrolling over the cards without JavaScript. All 25 names, issuers and issue dates, plus the eight supplied expiry dates, were checked against the transcription. No page-level horizontal overflow or clipped card content was found with page disclosures open or closed. Mobile and desktop screenshots were reviewed. LinkedIn remains the only external contact link.

## Credential issuer icons

Each credential displays its issuer's logo above the title, following the icons Paulo identified in the LinkedIn screenshots. These are issuer marks, not individual earned-badge verification images. Google Cloud's actual logo replaces the generic company placeholder visible in the screenshots. AWS and SAFe use the official variants available from their sources. All six original assets are stored locally under `assets/issuers/`, loaded lazily, and fitted without cropping or changing their colours. Decorative empty alt text avoids repeating the adjacent issuer name. The reserved square size prevents layout shifts, and the card layout adapts to small screens.

All 25 issuer mappings and image loads were verified in Chromium and Linux WebKit at widths from 280 to 1440 pixels. The certification track remains scrollable without JavaScript, and the page has no horizontal overflow with disclosures open or closed. Source assets were checked against their downloaded originals.

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

## Icon colours

The approved palette gives each experience icon its own colour: public services blue (`#2854A6`), people terracotta (`#A44928`), telecom violet (`#7850A0`), banking green (`#227357`), cloud petrol (`#197083`), utilities ochre (`#9A690E`), finance bronze (`#846044`), commerce raspberry (`#A03E65`) and digital indigo (`#535DA1`). Only the icon strokes receive these accents; the typography, ruler, navigation and section surfaces retain their existing colours.

Field Notes uses multicolour drawings: the beach illustration has an amber sun (`#A97012`), blue water (`#237F94`), green umbrella (`#227357`) and coral shield (`#BE5333`). People & Trust combines terracotta and petrol; Applied AI combines violet and blue with an amber detail. The people story uses its own SVG symbol so its two colours do not alter the single-colour experience icon. The beach paths separate sun, water, umbrella and shield geometry. All colours come from shared CSS custom properties, while existing icon sizes, line widths, content and section layouts are retained. Credential issuer logos retain their official colours.

The nine experience colours and three story palettes were checked in Chromium and Linux WebKit at 320, 390 and 1440 pixels with JavaScript disabled. Checks covered SVG strokes, neutral labels, experience expansion, valid symbol references and no horizontal overflow with disclosures open or closed. Desktop and mobile screenshots were inspected; visitor-facing text and all issuer logo assets are unchanged.

## Credential descriptions

The 25 short English descriptions summarize programme scope from issuer pages, issuer-owned Credly entries and official course material researched on 11 October 2026. They describe what each credential covers, not additional claims about Paulo’s work or current credential validity. Names, issuers, descriptions and supplied dates are preserved when the cards are reordered.

The Node.js description combines the supplied credential title with Accenture’s published description of its Cloud Native College; no unpublished syllabus is inferred. The 2023 Information Security description follows the programme’s contemporary overview. SAFe uses its historical SAFe 5 entry, and Migrating to Google Cloud uses the original Google-authored course listing rather than a newer replacement.

The compact cards and all 25 descriptions were checked in Chromium and Linux WebKit at 320, 390, 760 and 1440 pixels. Text remains fully visible, swipe and keyboard navigation reach the final card, and the page has no horizontal overflow. Native horizontal swipe and vertical page scrolling were also verified with JavaScript disabled. Cards size naturally to their contents; dates follow the description with a 16px gap.

| Credential | Description source |
| --- | --- |
| Global Leader \| Certified by Deel | [Source 1](https://www.deel.com/global-badges/) |
| Senior Technology Architect | [Source 1](https://www.credly.com/org/accenture/badge/senior-technology-architect) |
| AWS Certified Solutions Architect – Associate | [Source 1](https://aws.amazon.com/certification/certified-solutions-architect-associate/), [Source 2](https://www.credly.com/org/amazon-web-services/badge/aws-certified-solutions-architect-associate) |
| Cloud Solution Architect Certified | [Source 1](https://www.credly.com/org/accenture/badge/cloud-solution-architect-certified-certification) |
| Certified Delivery Professional | [Source 1](https://www.credly.com/org/accenture/badge/certified-delivery-professional) |
| AWS Certified Developer – Associate | [Source 1](https://aws.amazon.com/certification/certified-developer-associate/) |
| Technology Architect | [Source 1](https://www.credly.com/org/accenture/badge/technology-architect-certification) |
| Reinvention with Agentic AI | [Source 1](https://www.credly.com/org/accenture/badge/reinvention-with-agentic-ai) |
| AWS Certified AI Practitioner | [Source 1](https://aws.amazon.com/certification/certified-ai-practitioner/) |
| Well-Architected Proficient | [Source 1](https://www.credly.com/org/amazon-web-services/badge/well-architected-proficient) |
| SAFe Agilist Certification | [Source 1](https://www.credly.com/org/scaled-agile/badge/certified-safe-5-agilist) |
| Certified ScrumMaster | [Source 1](https://www.scrumalliance.org/get-certified/scrum-master-track/certified-scrummaster) |
| Cloud Digital Leader | [Source 1](https://cloud.google.com/learn/certification/cloud-digital-leader) |
| AWS Certified Cloud Practitioner | [Source 1](https://aws.amazon.com/certification/certified-cloud-practitioner/) |
| Accenture Cloud Native College – Node.js Associate Developer | [Source 1](https://newsroom.accenture.com/content/1101/files/everestsoftwareproductengineering.pdf) |
| Reliable Google Cloud Infrastructure: Design and Process | [Source 1](https://www.skills.google/course_templates/41?locale=en) |
| Elastic Google Cloud Infrastructure: Scaling and Automation | [Source 1](https://www.skills.google/paths/11/course_templates/178) |
| Migrating to Google Cloud | [Source 1](https://www.pluralsight.com/courses/migrating-google-cloud-4) |
| Essential Google Cloud Infrastructure: Core Services | [Source 1](https://www.skills.google/paths/11/course_templates/49) |
| Getting Started with Google Kubernetes Engine | [Source 1](https://www.skills.google/course_templates/2?locale=en) |
| Essential Google Cloud Infrastructure: Foundation | [Source 1](https://www.skills.google/course_templates/50?locale=en) |
| Google Cloud Fundamentals: Core Infrastructure | [Source 1](https://www.skills.google/course_templates/60?locale=en) |
| FY25 IS Elite Advocate | [Source 1](https://www.credly.com/org/accenture/badge/fy25-is-elite-advocate) |
| FY24 IS Elite Advocate | [Source 1](https://www.credly.com/org/accenture/badge/fy24-is-elite-advocate/) |
| Accenture Information Security Elite Advocate | [Source 1](https://www.accenture.com/content/dam/accenture/final/accenture-com/document/Accenture-Information-Security-Overview-2023.pdf) |

## Credential order

The carousel uses an editorial order that considers both relevance to Paulo’s architecture, leadership, execution and AI profile and the depth of the credential’s scope. It is not a standardized difficulty ranking across issuers. Global Leader | Certified by Deel appears first at Paulo’s request. Senior architecture, AWS architecture, cloud solution planning, delivery management and AWS development follow. Applied AI and architectural review follow; agile leadership, cloud foundations, supporting technical courses and broader recognition round out the list. Expiry dates remain visible and are not changed or interpreted as renewed validity.

The first eight cards are:

1. Global Leader | Certified by Deel
2. Senior Technology Architect
3. AWS Certified Solutions Architect – Associate
4. Cloud Solution Architect Certified
5. Certified Delivery Professional
6. AWS Certified Developer – Associate
7. Technology Architect
8. Reinvention with Agentic AI

## Talks and contributions

The Contributions section includes [Cubo for Devs — Masterclass #2: Como me tornar um Tech Lead?](https://www.youtube.com/watch?v=1hOnAOXTUeM), published by Cubo Itaú. Paulo supplied the recording as a talk he participated in. The video ID, original title and channel were confirmed through [Noembed’s YouTube metadata endpoint](https://noembed.com/embed?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D1hOnAOXTUeM). The portfolio uses the English title “How to become a Tech Lead.” and a short introduction grounded in that title and Paulo’s participation. A date, duration and specific discussion points are omitted because they were not verified.

The Cubo for Devs card uses an editorial cover made from HTML, CSS and a decorative SVG play icon; it is not the original video thumbnail. A single keyboard-accessible link opens the recording on YouTube in a new tab, announced in its accessible description. There is no embedded player or autoplay, and the card needs no JavaScript or third-party image request. The existing monochrome layout, grid motif and coral accent are retained. LinkedIn remains the sole contact destination.

Chromium and Linux WebKit checks at 280, 390 and 1440 pixels verified text containment, keyboard activation, link destination and new-tab behavior with JavaScript disabled. The page has no horizontal overflow, and the other sections and credential order are unchanged.

FlashCamp 2010 appears as a second event card using Paulo’s supplied group photo and year. The original 1024×683 JPEG is served locally as `assets/flashcamp-2010.jpg`, unchanged and without cropping; explicit dimensions and lazy loading reserve its aspect ratio. The English caption states that Paulo was representing Ogilvy at Brazil’s largest Adobe community event, following his supplied description. It does not infer a speaking role, venue, exact date or the identities of other attendees. The photo card is noninteractive, with its image above the text at every screen size.

The event card was checked in Chromium and Linux WebKit at 280, 390 and 1440 pixels. The original image decodes at the correct aspect ratio, all four attendees remain visible, and the page stays within the viewport. The Cubo recording link, all existing content and the credential order are preserved.

Talks and events share the certification carousel’s native scroll snapping, arrow buttons, position count and keyboard navigation. Mobile shows one card and a glimpse of the next; when both cards fit on wider screens, the swipe hint and arrows are hidden while the count remains visible. Each carousel manages its own scroll position and controls. Arrow/Home/End shortcuts apply only when its track is focused, preserving normal activation of the Cubo video link. That link draws its focus ring inside the card so it remains visible within the scrolling area. Images retain their original proportions, and native swipe works without JavaScript.

The shared carousels were verified in Chromium and Linux WebKit at 280, 390, 800 and 1440 pixels. Checks covered independent scroll positions, arrow states, counts, Home/End and arrow-key navigation, resizing, the Cubo link, image proportions and absence of clipped content or page-level overflow. Native touch swiping and vertical page scrolling were checked in Chromium without JavaScript; WebKit’s native scrolling fallback was also checked. A ResizeObserver refreshes controls after track or card layout changes, including WebKit’s delayed initial layout of an offscreen grid.
