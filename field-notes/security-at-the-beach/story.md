# A week at the beach. A security incident on day two.

[Back to portfolio — AI/Agent](https://paulosanches.github.io/hello/agent/)

Language: en

Source: https://paulosanches.github.io/hello/field-notes/security-at-the-beach/agent/

[English](https://paulosanches.github.io/hello/field-notes/security-at-the-beach/story.md) · [Português do Brasil](https://paulosanches.github.io/hello/pt/field-notes/security-at-the-beach/story.md) · [Italiano](https://paulosanches.github.io/hello/it/field-notes/security-at-the-beach/story.md)

---

SECURITY & LEADERSHIP

I went to a beach house for a week of remote work, hoping to spend more time with my family. On the second day, a production security incident changed the plan.

4 min read

![Pixelated coastal view with palm trees, a sandy beach and turquoise water.](https://paulosanches.github.io/hello/assets/field-notes-beach.png?v=cfb755a41222)

I had just been promoted to Manager. Among my new responsibilities, I had taken on the roles of Delivery Lead and Solution Architect for a marketing and CMS project serving one of Brazil’s leading agribusiness companies.

The solution used Liferay Portal and had been in production for three years. The project team had just two people, there were no significant issues on record, and the client was discussing a contract renewal. It was a small project in terms of team size, but an important one for the account.

With everything apparently under control, working from the beach house seemed straightforward. I expected a normal working week with more time close to my family.

## When instability became a security incident

On the second day, we identified a suspicious process running on the production server. Memory usage kept rising, putting the environment under strain and causing restarts. What first looked like a stability problem became a security incident.

We activated the company’s incident protocols, escalated the issue and set up a war room. My responsibility was to coordinate the technical response, organise the next actions and keep the client and leadership informed about the problem and our progress.

## Finding the fix was only part of the work

During the investigation, we found something that complicated the response. The project had been designed around Liferay’s Community edition during the sales phase. In that setup, we didn’t have the support or readily available fixes we needed to respond quickly.

We identified known vulnerabilities in the version we were running, but couldn’t find a ready-to-install update package to address them.

After searching forums and raising support requests with specialists, we discovered that the community had made a fix available. There was an extra step, though: we had to download several gigabytes of files and compile the application before installing the updated version on the server.

That was when the beach-house connection stopped being a minor detail. The downloads and build took two full nights.

## Keeping everyone informed

As the downloads progressed, the pressure grew. Leadership across Latin America was now following the incident, with updates requested several times a day.

I had to work on two fronts: help the team reach a solution and give stakeholders a clear account of what we knew, what was still under investigation and what would happen next.

> I had to make the next steps clear without promising a deadline we couldn’t yet stand behind.

Resolving the technical problem and communicating our progress were both part of the response. There were still uncertainties, and I needed to be transparent about them.

We eventually compiled and installed the updated version, addressed the vulnerabilities we had identified and closed the incident.

I barely got to enjoy the beach. Much of the week went into meetings, technical investigation and nights of work, in a setting that hadn’t been prepared for that routine. It became one of the most intense experiences of my career.

## What stayed with me

### Maintenance and support belong in the proposal

The cost of a solution needs to account for maintenance, updates and support. In this project, the choice of the Community edition created a difficulty that only became clear when we needed to respond to a crisis. If those capabilities are necessary to serve the client, they need to be part of the proposal from the start.

### Leadership means organising the whole response

The technical fix is only part of the job. Someone also needs to organise the response, support the team and communicate progress openly, even when there are still unanswered questions.

### Working from anywhere takes preparation

Being able to work from anywhere also means thinking about the conditions needed to handle the unexpected. The connection and working environment matter when a normal day turns into a crisis.

I had just stepped into management and expected a quiet week. Instead, from a beach house, I got a practical lesson in responsibility, decision-making and leadership under pressure.

## More on the technical side

If you’d like to know more about the technical details of this incident and think they could be useful to you, I’d be happy to talk it through.

[Message me on LinkedIn](https://www.linkedin.com/in/paulosanches)
