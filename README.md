# AI Marketing Ops Agent

Python-first Kaggle / Google AI Agents capstone app for turning one restaurant campaign brief into a structured, reviewable campaign pack.

The target user is an independent restaurant owner or manager who needs to promote a dish, offer, or local campaign without hiring a marketing team.

Public submission repo: https://github.com/ssyan110/ai-marketing-ops-agent

## Current Submission Cut

This MVP is intentionally deterministic and keyless: it runs locally, parses a text brief, generates campaign assets, shows guardrail warnings and evaluation scores, and exports the result as Markdown.

Implemented:

- FastAPI + Jinja product workbench.
- Restaurant-oriented text intake through a compact business brief.
- Deterministic agent workflow: brief -> audience insight -> strategy -> assets -> evaluation -> export.
- LinkedIn post, content types, carousel outline, photo/shot guidance, short content calendar, short video script, CTA, publishing checklist, warnings, assumptions, and Markdown export.
- Pytest coverage for parsing, workflow generation, guardrails, evaluation, and route rendering.

Not implemented yet:

- Public hosted demo link.
- True image/menu upload or Gemini vision analysis.
- Runtime ADK/Gemini provider integration.

## Stack

- FastAPI
- Jinja
- Tailwind CDN for the first UI slice
- Pytest

## What the Agent Produces

- Marketing brief
- Audience insight
- Campaign strategy
- LinkedIn post
- Content types
- Carousel outline
- Photo/shot guidance
- Short content calendar
- Short video script
- CTA
- Publishing checklist
- Evaluation score
- Guardrail warnings
- Assumptions

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Run Tests

```bash
.venv/bin/python -m pytest
```

## Run App

```bash
.venv/bin/uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Capstone Rubric Map

| Rubric area | Evidence in this repo |
| --- | --- |
| Pitch | Independent restaurant owner/manager story with a concrete product-campaign workflow. |
| Technical implementation | FastAPI app, deterministic agent workflow, typed models, guardrails, evaluator, content calendar, Markdown export, tests. |
| Documentation | README, project spec, BRD, agent skills, submission plan, writeup draft, demo script/checklist. |
| Security | No committed secrets, `.env.example`, deterministic no-key MVP. |
| Evaluation | Transparent campaign quality score and pytest coverage. |

## Course Concepts to Show

| Concept | Where to show it |
| --- | --- |
| Agent workflow | `app/agent.py` and demo video. |
| Agent skills | `.codex/skills/` and `docs/agent_skills.md`. |
| Tool surface | Markdown export in the UI and `app/agent.py`. |
| Security and guardrails | `app/guardrails.py`, UI warnings, and demo video. |
| Deployability | README run commands and public repo once published. Do not claim a hosted app until one exists. |

## Notes

The MVP uses deterministic Python generation so it works without API keys. Gemini / Google ADK integration should come after the core workflow, guardrails, UI, and tests stay stable.
