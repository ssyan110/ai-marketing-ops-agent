# AI Marketing Ops Agent: Restaurant Campaign Workbench

## 1. Problem Statement

Independent restaurant owners and managers often need to promote a dish, offer, or local campaign while also running daily operations. They may have a product idea and a rough note, but not enough time or marketing support to turn it into clear copy, content structure, CTA, and quality checks.

AI Marketing Ops Agent focuses on this solo-ops restaurant workflow: take one messy campaign brief and turn it into a reviewable campaign pack that can be edited and used by the owner or manager.

## 2. Solution Overview

The current MVP is a Python FastAPI workbench. A user enters a business name and compact campaign brief. The deterministic agent parses the brief, builds a marketing brief, generates audience insight, proposes a campaign strategy, drafts content assets, creates photo guidance and a short posting calendar, evaluates the pack, shows warnings and assumptions, and exports the output as Markdown.

The submission demo should use a restaurant scenario such as:

> Corner Kitchen is launching mac and cheese with spicy crispy chicken for office workers and nearby apartment residents. The goal is more lunch and dinner visits without a discount race.

## 3. Demo Links

- Video demo: TODO - add real video URL after recording.
- Project/demo link: TODO - add public repo, Kaggle notebook, or hosted app URL only after it exists.
- Local run path: clone the repo, install requirements, run tests, then start FastAPI with the README commands.

## 4. Agent Architecture

The app uses a staged workflow rather than one long prompt:

1. Normalize the input into a campaign model.
2. Build audience pain points, objections, motivations, and desired outcomes.
3. Create strategy: hook, positioning, message hierarchy, and CTA direction.
4. Generate campaign assets: content types, LinkedIn post, carousel outline, shot list, short content calendar, short video script, CTA, and publishing checklist.
5. Run guardrails for missing audience, missing goal, overclaims, margin-risky discount framing, weak CTA, thin content, and incomplete carousel story.
6. Score the output with a transparent evaluator, including restaurant specificity, calendar usefulness, and visual guidance.
7. Render the full pack and Markdown export in the UI.

The code is intentionally deterministic so judges can run it without API keys.

## 5. Course Concepts Demonstrated

- Agent workflow: the app performs parsing, planning, content generation, evaluation, warning generation, and export as separate steps.
- Agent skills: the repo includes project-local restaurant marketing skills and online-acquired marketing skills, documented in `docs/agent_skills.md`.
- Tool surface: Markdown export turns the generated pack, shot guidance, and calendar into a reusable artifact outside the UI.
- Guardrails and security: the MVP avoids committed secrets, documents environment setup through `.env.example`, and flags unsupported claims or missing campaign context.
- Evaluation: generated packs receive visible scores for audience specificity, content usefulness, actionability, CTA quality, and risk control.
- Vibe coding workflow: the repo documents the product direction, business requirements, agent skills, submission plan, and remaining blockers so the project can be iterated through natural-language development tasks.

## 6. Technical Implementation

Stack:

- FastAPI for the app server.
- Jinja templates for the UI.
- Tailwind CDN for the first professional workbench slice.
- Pydantic models for data contracts.
- Pytest for workflow, guardrail, evaluator, and route checks.

Key files:

- `app/agent.py`: deterministic campaign workflow and Markdown renderer.
- `app/guardrails.py`: warning checks.
- `app/evaluator.py`: transparent scoring for audience specificity, restaurant fit, calendar usefulness, visual guidance, actionability, CTA quality, and risk control.
- `templates/index.html`: demo workbench UI.
- `docs/agent_skills.md`: project-local and online-acquired marketing skill evidence.

## 7. Evaluation and Tests

The MVP can be checked locally with:

```bash
.venv/bin/python -m pytest
```

The tests cover campaign generation, labeled brief parsing, channel parsing, missing-context warnings, restaurant guardrails, evaluation behavior, Markdown export, and the `/generate` route.

## 8. Guardrails, Security, and Limitations

The app does not require API keys for the default demo and should not contain committed secrets. It flags missing target audience, missing campaign goal, potential overclaims, margin-risky discount framing, missing CTA, thin content, and incomplete carousel outlines.

Current limitations:

- No public hosted app link yet.
- No image/menu upload or vision analysis yet.
- No runtime Gemini / Google ADK integration yet.
- The output is a deterministic draft and should be reviewed before publishing.

## 9. Impact and Future Work

The practical value is speed and structure: a restaurant owner can move from a rough dish or offer idea to a campaign pack with CTA, assets, checklist, warnings, and export in minutes.

Next improvements:

- Publish a public repo or hosted runnable demo.
- Expand the short content calendar into a 7-day or 14-day campaign calendar.
- Add optional image/menu upload and Gemini vision support.
- Add optional Google ADK/Gemini provider while keeping the no-key deterministic fallback.
