# AI Marketing Ops Agent Project Spec

## Problem
Independent restaurant owners and managers often know what they want to promote, but struggle to turn a dish, offer, or local campaign idea into a structured campaign workflow.

## Goal
Build a working AI Marketing Ops Agent that turns structured restaurant campaign intake into a complete, copy-ready marketing campaign pack.

## Target Users
- Independent restaurant owners
- Restaurant managers handling marketing after operations work
- Family-run or low-budget restaurants
- Small business operators who need a repeatable content workflow

## MVP Scope
- Professional FastAPI web app with form-based input.
- One-question-at-a-time campaign intake with visible progress.
- Deterministic Python agent workflow that works without API keys.
- Structured campaign output.
- Guardrail warnings for missing context, overclaims, weak CTA, and generic content.
- Transparent evaluation score.
- Markdown export.
- Content type recommendations.
- Photo/shot guidance.
- Short content calendar.
- Text-first structured restaurant campaign intake for the current submission cut.

## Non-Goals
- No Streamlit UI.
- No user accounts.
- No payment or production SaaS billing.
- No heavy multi-agent framework until the basic workflow is proven.
- No external web research in the first MVP.
- No claim of hosted deployment until a real public link exists.
- No claim of image/menu analysis until upload or vision support is implemented.

## Agent Workflow
1. Normalize staged user input into a marketing brief.
2. Generate audience pain points, objections, motivations, and desired outcomes.
3. Create campaign strategy: hook, positioning, message hierarchy, CTA direction.
4. Generate content types, LinkedIn post, carousel outline, photo/shot guidance, short content calendar, short video script, CTA, and checklist.
5. Evaluate the pack with a transparent rubric.
6. Return warnings and assumptions.

## Data Contract
Primary UI fields:
- business_name
- industry
- location
- target_audience
- campaign_goal
- platform
- customer_pain_points
- requested_content_types
- content_calendar_length
- constraints

The agent normalizes the brief into:
- business_name
- product_service
- target_audience
- campaign_goal
- platform
- tone
- language

Optional normalized fields:
- constraints
- source_notes

## BDD Scenarios

```gherkin
Scenario: Generate a complete campaign pack from structured intake
  Given a user provides staged campaign intake fields
  When the agent workflow runs
  Then it returns a campaign pack with brief, audience, strategy, content, evaluation, warnings, and assumptions
  And the output works without an API key
```

```gherkin
Scenario: Flag missing audience context
  Given a user omits the target audience
  When guardrails run
  Then the system returns a warning that audience context is missing
  And the evaluation score is reduced
```

## Acceptance Criteria
- `python3 -m pytest` passes.
- `uvicorn app.main:app --reload` starts the UI.
- The UI renders input, workflow, campaign output, evaluation, and export surfaces.
- No secrets are committed.
- README documents setup, run, and test commands.

## Current Submission Notes

The current app is a deterministic local MVP. It is strongest as a judge-facing demo of agent workflow, guardrails, evaluation, tests, short calendar generation, shot guidance, and export. Image/menu intake, public deployment, and Gemini / Google ADK runtime integration remain next-slice work unless implemented before final upload.
