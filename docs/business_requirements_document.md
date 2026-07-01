# Business Requirements Document: Restaurant Marketing Solo Ops Agent

Status: Restaurant target approved; current submission cut is text-first MVP
Owner: Adam Yan
Prepared date: 2026-06-21
Project: Kaggle / Google AI Agents Intensive Vibe Coding Capstone

## Current Submission Cut

The business target remains the restaurant solo-ops workflow, but the current shipped MVP is narrower than the full BRD. For submission, describe the app as a deterministic FastAPI workbench that accepts a text restaurant campaign brief and produces a quality-checked campaign pack with Markdown export.

Implemented now:

- Text brief intake.
- Brief normalization into product/service, audience, goal, platform, tone, language, constraints, and source notes.
- Campaign strategy, audience insight, content types, LinkedIn post, carousel outline, photo/shot guidance, short content calendar, short video script, CTA, publishing checklist, score, warnings, assumptions, and Markdown export.
- Local test coverage and no-key operation.

Not implemented yet:

- Product image/menu upload or vision analysis.
- Expanded 7-day or 14-day content calendar output.
- Restaurant-specific channel packs for Facebook, Instagram, TikTok/Reels, Zalo, and Google Business Profile.
- Local restaurant memory.
- Gemini / Google ADK runtime integration.
- Public hosted demo link.

## 1. Executive Summary

Restaurant Marketing Solo Ops Agent helps independent restaurant owners and managers create practical local marketing campaigns for a specific dish, menu item, offer, or restaurant event when they cannot afford a dedicated marketing team.

The product is for the person who has to run the restaurant and do the marketing themselves. It should accept a product photo, a simple image/menu image, or a plain text description, then turn that input into a full campaign plan, content types, channel-ready copy, a photo/video shot list, a content calendar, a posting checklist, and a quality review.

The capstone should show a focused real-world problem: restaurants need more visits, repeat customers, reservations, delivery orders, or event bookings, but the owner or manager does not have time, budget, or marketing expertise to build campaigns from scratch.

## 2. Hackathon Context

The Kaggle / Google capstone asks participants to build an AI agent project that solves a real-world problem, helps people, or improves everyday living. The course emphasizes natural-language workflows, tool/API integration, practical agent systems, quality checks, guardrails, and production-readiness.

Required submission evidence should map to this narrower restaurant use case:

| Evidence | Product implication |
|---|---|
| Real-world value | Help small restaurants run marketing without hiring an agency or in-house marketer. |
| Agentic behavior | Run a visible workflow: understand product input -> clarify restaurant context -> identify campaign angle -> plan content types/calendar -> create assets -> check risks -> export. |
| Tool/API integration | MVP should include at least one useful tool surface, such as image/menu upload, markdown export, local memory, or provider-ready LLM integration. |
| Evaluation | Score whether the campaign is specific, realistic, actionable, and safe for a local restaurant. |
| Guardrails | Flag missing audience, unrealistic sales promises, discount traps, unclear offers, and unsupported claims. |
| Communication | README, writeup, demo script, and architecture docs must make the restaurant problem obvious. |

Project-local marketing skills are documented in `docs/agent_skills.md` and live under `.codex/skills/`. Additional skills were pulled from `https://github.com/awesome-skills` and `https://github.com/coreyhaines31/marketingskills` to demonstrate online skill acquisition for the capstone. Together, these skills are evidence that the agent has specialized capabilities instead of being a one-shot content prompt.

## 3. Business Problem

Independent restaurants often operate on thin margins. The owner or manager may know the food, customers, and daily problems well, but marketing becomes one more task squeezed between staffing, inventory, service, suppliers, and customer complaints.

Typical failure modes:

- The restaurant has a new dish or offer but only has a photo and a rough idea of what to say.
- The restaurant posts random food photos without a campaign goal or posting plan.
- Promotions rely too heavily on discounts and hurt margins.
- The owner does not know what to say beyond "come try our food."
- Local channels are fragmented: Facebook, Instagram, Zalo, Google Business Profile, delivery apps, and in-store signage.
- The manager needs something usable today, not a complex marketing plan.
- Generic AI output does not reflect cuisine, neighborhood, capacity, margins, or service constraints.

Business problem statement:

Restaurant owners and managers without marketing support need a lightweight campaign assistant that turns a product photo or rough menu description into a specific, low-budget, quality-checked campaign and content calendar they can run themselves.

## 4. Target User

Primary MVP user:

An independent restaurant owner or manager who does not have the budget to hire a marketing team and must personally plan and execute weekly marketing.

| User type | Situation | Need |
|---|---|---|
| Owner-operator | Runs the business daily and handles marketing after service hours | A fast product campaign tied to sales, bookings, repeat visits, or delivery orders |
| Restaurant manager | Manages staff and service, then has to post content and promotions | Clear copy, content types, calendar, checklist, and simple execution plan |
| Family-run restaurant | Limited budget, inconsistent posting, no formal brand team | Repeatable weekly campaign workflow for menu items and seasonal offers |
| New or quiet restaurant | Needs local awareness but cannot afford ads or agency retainers | Local-first campaign ideas and channel-ready assets |

The MVP should speak to this user in plain business language, not marketing jargon.

## 5. Product Objectives

| Objective | Success metric | Target |
|---|---|---|
| Reduce owner workload | Time from product photo/description to usable campaign pack | Under 5 minutes in demo flow |
| Improve campaign specificity | Output includes restaurant type, product/menu item, audience, channel, goal, constraint, and visual angle | 100% when provided in input |
| Protect margins | Campaign avoids defaulting to heavy discounts | Warnings when discounting is the main tactic |
| Make execution easy | Output includes content types, copy, shot list, content calendar, posting checklist, and next action | Present in every completed pack |
| Demonstrate capstone fit | App shows agent workflow, evaluation, guardrails, and export | Clear in UI and demo video |

## 6. Scope

### MVP Scope

The MVP should do one job well:

Convert a product image, simple menu image, or messy product description into a practical restaurant marketing campaign the owner or manager can execute without a marketing team.

MVP includes:

- Product input: uploaded food/product image, simple menu image, or text description.
- Simple restaurant context input.
- Online skills for first-principles analysis and 5-whys problem diagnosis.
- Online marketing skills for product marketing, offer framing, content strategy, copywriting, social, image, video, and marketing psychology.
- Project-local marketing skills for product positioning, content types, content calendar, and marketing QA.
- Missing-context detection.
- Brief normalization into restaurant type, location/neighborhood, target customer, product/menu item, visual cues, campaign goal, channel, budget/constraint, and tone.
- Campaign angle and local positioning.
- Content type recommendations, such as launch post, reel, story, offer post, behind-the-scenes post, UGC prompt, and Google Business Profile update.
- Channel-ready post copy for restaurant-relevant channels.
- Short video or reel script.
- Photo/shot checklist.
- 7-day or 14-day content calendar with post type, channel, hook, asset needed, and CTA.
- In-store or delivery-app promotion note when relevant.
- CTA.
- Publishing checklist.
- Evaluation score with explanations.
- Guardrail warnings and assumptions.
- Markdown export.
- One realistic restaurant demo scenario.

### Non-Goals for MVP

- No full social media scheduler.
- No paid ads optimization.
- No POS, delivery-app, or reservation-system integration.
- No user accounts.
- No agency-style brand strategy deck.
- No generic campaign generator for every business type.
- No multi-location enterprise restaurant suite.
- No reliance on API keys for the baseline demo.

## 7. Business Requirements

| ID | Requirement | Priority |
|---|---|---|
| BR-01 | The product must focus on independent restaurants where the owner or manager does marketing themselves. | Must |
| BR-02 | The first interaction must accept an image, simple image/menu input, or text description of the product the owner wants to market. | Must |
| BR-03 | The app must detect missing restaurant context such as customer type, product/menu item, location, goal, channel, budget, or constraint. | Must |
| BR-04 | The campaign pack must include strategy, content types, copy, visual execution guidance, content calendar, CTA, checklist, evaluation, warnings, and assumptions. | Must |
| BR-05 | The workflow must show agent steps, not just a generated answer. | Must |
| BR-06 | The output must be useful without external API keys. | Must |
| BR-07 | The app must avoid unsafe or unrealistic claims, especially guaranteed traffic, guaranteed revenue, health claims, and heavy discount assumptions. | Must |
| BR-08 | The project must be easy to explain in a 3-5 minute capstone demo. | Must |
| BR-09 | The project must include explicit marketing skills that can be shown in the capstone as agent capabilities. | Must |
| BR-10 | The project must demonstrate that skills can be acquired from an online source and incorporated into the app workflow. | Must |
| BR-11 | The project must incorporate marketing skills from `coreyhaines31/marketingskills` as part of the restaurant campaign workflow. | Must |
| BR-12 | The codebase should support future Gemini / Google ADK integration without making it mandatory for MVP. | Should |
| BR-13 | The product should save reusable restaurant profile context in a later slice. | Should |

## 8. Functional Requirements

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-01 | Product campaign intake | User can provide a food/product image, simple menu image, or text description plus restaurant name. |
| FR-02 | Brief parser | System extracts restaurant type, neighborhood, target customer, product/menu item, visual cues, campaign goal, channel, and constraints. |
| FR-03 | Missing-context handling | If key context is missing, system shows warnings and suggests the next question. |
| FR-04 | Campaign planner | System creates a campaign angle, local promise, message hierarchy, and CTA direction. |
| FR-05 | Content type planner | System recommends campaign content types by channel, such as launch post, reel, story, menu spotlight, owner note, UGC prompt, and reminder post. |
| FR-06 | Content generator | System produces channel-ready copy, short video script, photo/shot checklist, CTA, and publishing checklist. |
| FR-07 | Content calendar | System creates a 7-day or 14-day posting calendar with date/day, channel, content type, hook, asset needed, caption direction, and CTA. |
| FR-08 | Evaluation engine | System scores restaurant specificity, product-goal fit, local relevance, calendar usefulness, actionability, CTA quality, and risk control. |
| FR-09 | Guardrails | System flags overclaims, discount traps, vague output, unsupported facts, missing CTA, missing context, and image/detail uncertainty. |
| FR-10 | Export | User can copy or export the full campaign pack and calendar as Markdown. |
| FR-11 | Demo sample | App includes one realistic restaurant product-launch scenario for fast judging/demo. |

## 9. Non-Functional Requirements

| Area | Requirement |
|---|---|
| Reliability | Core workflow must run deterministically without API keys. |
| Security | No secrets in source code. Environment variables documented in `.env.example`. |
| Accessibility | UI must use readable labels, keyboard-focusable controls, and sufficient contrast. |
| Performance | MVP generation should complete quickly enough for a live demo. |
| Maintainability | Business logic should be testable outside the UI. |
| Reproducibility | README must include setup, test, and run commands. |
| Localization | Product should support Vietnamese restaurant context and Vietnamese-labeled inputs. |

## 10. Agent Workflow

The app should behave like a restaurant marketing assistant with stages:

1. Intake: capture the product image, simple menu image, or text description.
2. 5-whys skill: diagnose the real business problem when the owner gives a vague goal.
3. First-principles skill: challenge assumptions before choosing workflow complexity.
4. Product positioning skill: identify target diner, business goal, product angle, and missing context.
5. Content types skill: choose restaurant-native formats and channel-specific directions.
6. Content calendar skill: plan the campaign cadence across channels.
7. Generate: produce channel-ready copy, short video script, photo checklist, and publishing checklist.
8. Marketing QA skill: score quality, flag risks, and suggest improvements.
9. Export: produce a shareable campaign pack and content calendar the owner or manager can execute.

This workflow should be visible in the UI and documentation.

## 11. Evaluation Rubric

| Criterion | Score range | What it measures |
|---|---:|---|
| Restaurant specificity | 1-5 | Does the output reflect the restaurant type, location, cuisine, and operating context? |
| Customer specificity | 1-5 | Is the target diner concrete and reflected in the campaign? |
| Product-goal fit | 1-5 | Does the campaign connect the dish/menu item/offer to the business goal? |
| Local relevance | 1-5 | Does the campaign make sense for the neighborhood/channel? |
| Calendar usefulness | 1-5 | Does the calendar give a realistic sequence the owner can follow? |
| Actionability | 1-5 | Can the owner or manager execute the plan without a marketing team? |
| Visual guidance | 1-5 | Are photo/video instructions concrete enough to shoot quickly from the product image or description? |
| CTA quality | 1-5 | Is the next action clear, realistic, and channel-appropriate? |
| Risk control | 1-5 | Are overpromises, unsupported claims, and margin-risky discounts avoided or flagged? |

Pass condition:

The pack is demo-ready only if it scores at least 70% and has no blocking guardrail warnings.

Current implementation note:

The deterministic evaluator now includes restaurant specificity, calendar usefulness, visual guidance, actionability, CTA quality, and risk control. The current calendar is a short submission-ready sequence, not yet a full 7-day or 14-day scheduler.

## 12. UX Requirements

The result screen should reduce confusion and help the owner decide what to do next.

Recommended UI structure:

1. Input quality panel: what the agent understood from the image/description and what is missing.
2. Restaurant campaign summary: restaurant, audience, product, goal, channel, constraint.
3. Workflow progress: intake, clarify, plan, generate, evaluate, export.
4. Content strategy: campaign angle, content types, channels, and CTA.
5. Content calendar: what to post, where to post, what asset is needed, and when.
6. Content pack sections.
7. Evaluation and warnings.
8. Markdown export.

Do not show fake analytics, vanity metrics, or agency-style dashboards. Every visible element must help the restaurant owner or manager run the campaign.

## 13. Phased Delivery Plan

| Phase | Goal | Deliverable |
|---|---|---|
| 0 | Align restaurant business requirements | Narrow BRD approved |
| 1 | Fix product workflow | Product-image/text intake plus restaurant-first workflow UI |
| 2 | Strengthen deterministic agent | Better product parsing, clarification, calendar generation, scoring, and sample scenario |
| 3 | Add one capstone tool surface | Image/menu upload, markdown export, local restaurant memory, or source input |
| 4 | Add optional LLM provider | Gemini/mock provider with no-key fallback |
| 5 | Prepare submission | README, architecture, writeup, demo script, final checklist |

## 14. Demo Scenario

Recommended primary demo:

Restaurant: Corner Kitchen

Brief:

I have a new product: mac and cheese with spicy crispy chicken. I have a simple food photo and want to market this product on social media. We are a casual restaurant near an office and apartment area. I want a full campaign, content types, captions, short video ideas, and a content calendar. Budget is low. Channels: Facebook, Instagram, TikTok/Reels, Zalo, and Google Business Profile.

Expected product behavior:

- Accept either the uploaded product image or text description as the campaign starting point.
- Extract restaurant type, location context, target customer, product, visual cues, goal, channel, and constraint.
- Show what is missing or assumed.
- Create a practical product-launch campaign for mac and cheese with spicy crispy chicken.
- Recommend content types by channel.
- Generate channel-ready copy for local restaurant marketing.
- Create a short video/reel script and simple shot checklist.
- Create a 7-day or 14-day content calendar.
- Warn that traffic/revenue claims must not be guaranteed.
- Provide a clear CTA and publishing checklist.
- Export a Markdown campaign pack and calendar.

## 15. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Output still feels generic | Weak demo and low perceived value | Evaluate restaurant/customer/offer specificity. |
| App becomes a content wall | Owner will not know what to do | Show summary, action plan, and checklist before long copy. |
| Campaign defaults to discounts | Hurts margins and trust | Add discount-trap warning and require non-discount alternatives. |
| Image input is unclear | Agent may invent details | Require uncertainty notes and ask for missing product details. |
| Calendar is too ambitious | Owner will not execute it | Keep MVP calendar short, practical, and asset-aware. |
| Scope grows too fast | Unfinished capstone | Follow phased plan; no LLM/memory before core restaurant flow is useful. |
| API setup fails during demo | Demo risk | Keep deterministic no-key path as default. |
| Submission requirements change | Missing asset risk | Verify Kaggle submission form before final upload. |

## 16. Open Questions

| Question | Owner | Decision needed |
|---|---|---|
| Should the first demo focus on a new menu item launch, dine-in lunch traffic, delivery orders, repeat customers, or event bookings? | Adam | Before UI redesign |
| Which channels should MVP support first: Facebook/Instagram/Zalo/Google Business Profile, or fewer? | Adam | Before content templates |
| Should MVP calendar length be 7 days or 14 days? | Adam | Before calendar generator |
| Should image support be upload/display only first, or true vision-based analysis when a model key is available? | Adam | Before implementation |
| Should output language be Vietnamese-first, English-first for judges, or bilingual? | Adam | Before final demo script |
| Which capstone tool surface is most valuable: local restaurant memory, menu upload/source input, or Gemini integration? | Adam | Before Phase 3 |
| What is the final public demo path: local video, GitHub-only, Hugging Face Spaces, or another host? | Adam | Before submission prep |

## 17. Definition of Done

The full restaurant MVP is ready when:

- A restaurant owner or manager can understand the workflow from the first screen.
- The app turns one realistic restaurant product image or description into a specific local campaign pack.
- The app produces a useful content calendar with content types, channels, assets needed, and CTAs.
- Missing context is clearly flagged.
- The plan avoids defaulting to deep discounts.
- Evaluation and warnings are visible and useful.
- The output can be exported as Markdown.
- Tests cover parsing, guardrails, evaluation, and end-to-end pack generation.
- README and Kaggle writeup explain the restaurant problem and agent workflow.
- The demo can be completed in under 5 minutes.

The current submission package is documentation-ready when:

- README and docs state the current text-first scope honestly.
- Final writeup draft exists and leaves placeholders for real public links.
- Demo script/checklist exists for a local recording.
- Submission checklist distinguishes completed docs from deployment/code-publishing blockers.

## Sources

- Local capstone summary: `kaggle_vibe_coding_agents_capstone_requirements.md`
- Local project spec: `docs/project_spec.md`
- Local submission plan: `docs/submission_plan.md`
- Google announcement: https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/
- Kaggle capstone page listed in local docs: https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/overview
