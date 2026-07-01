# Demo Video Script and Checklist

Target length: 3 to 5 minutes.

## Recording Setup

- Run tests first: `.venv/bin/python -m pytest`.
- Start the app: `.venv/bin/uvicorn app.main:app --reload`.
- Open `http://127.0.0.1:8000`.
- Use local app recording unless a real hosted URL exists.
- Do not claim image upload, Gemini/ADK runtime integration, or public deployment unless completed before recording.

## Demo Brief

Business name:

```text
Corner Kitchen
```

Business brief:

```text
Audience: office workers and nearby apartment residents. Offer: mac and cheese with spicy crispy chicken. Goal: increase lunch and dinner visits this week. Channels: Facebook, Instagram/Reels, Zalo, Google Business Profile. Constraint: low budget, no discount race, avoid guaranteed traffic claims.
```

## Script

### 0:00-0:30 - Problem

"Independent restaurants often need to promote a new dish or offer, but the owner or manager is also running service, staffing, suppliers, and customer issues. They do not need another blank prompt. They need a repeatable campaign workflow they can trust and edit."

### 0:30-1:00 - Product

"AI Marketing Ops Agent is a FastAPI workbench for turning one messy restaurant campaign brief into a structured campaign pack. The current MVP is deterministic and works without API keys, so judges can run it locally."

### 1:00-2:20 - Live Demo

1. Show the input form.
2. Paste the Corner Kitchen brief.
3. Click "Generate campaign pack."
4. Show the workflow status.
5. Show strategy and audience insight.
6. Show the generated content types, LinkedIn post, carousel outline, shot guidance, short content calendar, short video script, CTA, and publishing checklist.

### 2:20-3:20 - Evaluation and Guardrails

"The app does not just produce copy. It evaluates the pack and shows warnings or assumptions. It checks for missing audience, missing campaign goal, unsupported claims, discount traps, weak CTA, thin content, and incomplete carousel structure."

Show the score panel, guardrails, assumptions, and Markdown export.

### 3:20-4:20 - Architecture

"The workflow is split into parse, plan, generate, evaluate, and export steps. The core logic lives in `app/agent.py`, data contracts in `app/models.py`, guardrails in `app/guardrails.py`, and scoring in `app/evaluator.py`. Tests cover generation, parsing, guardrails, evaluation, Markdown export, and the FastAPI route."

### 4:20-5:00 - Honest Scope and Next Steps

"For this submission, the working surface is text brief to restaurant campaign pack with evaluation, shot guidance, short calendar, and Markdown export. The next slices are public deployment, image/menu upload, expanded 7- or 14-day calendars, and optional Gemini or Google ADK integration while keeping the no-key fallback."

## Pre-Submission Checklist

- Tests pass locally.
- README run commands work.
- Video shows a real local run or real hosted URL.
- Project link uses `https://github.com/ssyan110/ai-marketing-ops-agent`.
- Writeup links are updated with the actual video and project URLs.
- No public-link placeholders are described as complete.
- No secrets are committed.
- Submission uses `docs/final_writeup_draft.md` as the base and stays under the Kaggle word limit.
