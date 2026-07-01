# Agent Skills

The capstone agent uses project-local marketing skills to make the workflow more than a generic content generator.

## Project Skills

| Skill | Role in the agent workflow |
|---|---|
| `.codex/skills/restaurant-product-positioning` | Turns a dish image or product description into a target diner, business goal, campaign angle, and missing-context questions. |
| `.codex/skills/restaurant-content-types` | Recommends restaurant-native content types and channel-specific copy directions. |
| `.codex/skills/restaurant-content-calendar` | Builds a 7-day or 14-day posting calendar with channel, hook, asset, caption direction, CTA, and status. |
| `.codex/skills/restaurant-marketing-qa` | Scores the output and flags unsupported claims, margin-risky discounts, missing context, and vague copy. |

## Online Skills Pulled From GitHub

| Skill | Source | Role in this app |
|---|---|---|
| `.codex/skills/online-first-principles` | `https://github.com/awesome-skills/first-principles-skill` | Challenges assumptions before adding features, channels, or workflow complexity. |
| `.codex/skills/online-5-whys` | `https://github.com/awesome-skills/5-whys-skill` | Diagnoses the restaurant's real marketing problem before generating a campaign. |

## Marketing Skills Pulled From GitHub

Source: `https://github.com/coreyhaines31/marketingskills`

| Skill | Role in this app |
|---|---|
| `.codex/skills/product-marketing` | Establishes restaurant/product/audience positioning context before other marketing work. |
| `.codex/skills/offers` | Frames the dish or menu item as a compelling, margin-aware offer. |
| `.codex/skills/content-strategy` | Chooses content pillars and campaign themes before writing posts. |
| `.codex/skills/copywriting` | Writes persuasive but clear captions, hooks, CTAs, and campaign copy. |
| `.codex/skills/social` | Adapts content for Facebook, Instagram, TikTok/Reels, Zalo, and Google Business Profile. |
| `.codex/skills/image` | Guides product-photo and social graphic requirements. |
| `.codex/skills/video` | Guides short-form video/reel concepts and scripts. |
| `.codex/skills/marketing-psychology` | Applies framing, social proof, urgency, and decision-making principles without overclaiming. |

## Current App Integration

The current deterministic app uses the skills as documented design evidence and generation guidance. It does not dynamically load or execute skill files at runtime. For submission, describe them as project-local and online-acquired skill artifacts that shaped the workflow, not as a live plugin framework.

Implemented in the app today:

- Brief parsing from text input.
- Audience, strategy, content types, shot guidance, short content calendar, checklist, evaluation, guardrails, assumptions, and Markdown export.

Planned but not wired yet:

- Image/menu skill execution.
- Runtime orchestration across the skill folders.
- Gemini / ADK-backed tool calls.

## Target Workflow Mapping

This is the intended restaurant workflow. The current submitted app implements the text-brief subset and Markdown export.

1. Intake text description now; product image or menu image later.
2. Run `online-5-whys` when the owner's problem is vague, such as "sales are slow."
3. Run `online-first-principles` when choosing the smallest useful campaign workflow.
4. Run `product-marketing`, `offers`, and `restaurant-product-positioning`.
5. Run `content-strategy`, `social`, `image`, and `video`.
6. Run `copywriting` and `marketing-psychology`.
7. Run `restaurant-content-types`.
8. Run `restaurant-content-calendar` as deterministic short-calendar generation.
9. Run `restaurant-marketing-qa`.
10. Export the complete campaign pack now; add content calendar export when calendar output is implemented.

## Capstone Evidence

These skills support the required agent behavior:

- Real-world value: focused restaurant owner/manager marketing problem.
- Agentic behavior: staged skill workflow instead of one-shot generation.
- Online skill acquisition: two skills pulled from `github.com/awesome-skills`.
- Marketing skill acquisition: eight marketing skills pulled from `github.com/coreyhaines31/marketingskills`.
- Tool/API integration path: Markdown export now; image/menu input and optional Gemini vision later.
- Evaluation: restaurant-specific QA rubric.
- Guardrails: unsupported claim, discount trap, missing context, and image uncertainty checks.
