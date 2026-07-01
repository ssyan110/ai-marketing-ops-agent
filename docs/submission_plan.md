# Submission Plan

## Track

Agents for Business.

## Winning Angle

AI Marketing Ops Agent helps independent restaurant owners and managers turn one messy dish or offer brief into a quality-checked campaign pack they can review, edit, and publish without a marketing team.

## Eligibility Checklist

| Item | Status | Owner note |
| --- | --- | --- |
| Writeup under 2,500 words | Draft ready | See `docs/final_writeup_draft.md`; add final public links before submission. |
| Cover image | Local asset ready | Use `docs/assets/kaggle_cover.svg` or export it to PNG before upload. |
| Video under 5 minutes | Script/checklist ready | See `docs/demo_video_script_checklist.md`; record against local app unless a hosted URL exists. |
| Public project link | Ready | Use https://github.com/ssyan110/ai-marketing-ops-agent unless a hosted demo is added later. |
| Public codebase | Ready | Public GitHub repo: https://github.com/ssyan110/ai-marketing-ops-agent |

## Rubric Strategy

| Area | Points | Plan |
| --- | ---: | --- |
| Pitch | 30 | Make the problem concrete: busy restaurant owners/managers need repeatable local campaigns, not random prompts. |
| Implementation | 70 | Prioritize runnable app, clean architecture, tests, guardrails, docs, and reproducible setup. |

## Three Course Concepts

| Concept | Required evidence |
| --- | --- |
| Agent workflow | Code and video: deterministic workflow from brief to evaluated campaign pack. |
| Agent skills | Repo evidence: project-local skills and online-acquired marketing skills in `.codex/skills/` with mapping in `docs/agent_skills.md`. |
| Security features | Code and video: no secrets, `.env.example`, guardrail warnings, overclaim checks. |
| Tool surface / export | UI and video: Markdown export makes the generated pack usable outside the app. |
| Deployability | Video and README: local run path and reproducible setup. Add public URL only after it exists. |

## Official Submission Requirements Verified

- Submit a Kaggle Writeup under 2,500 words.
- Select a track; this repo should use `Agents for Business`.
- Attach a cover image.
- Attach a public YouTube video that is 5 minutes or less.
- Attach a public project link. A public GitHub repo with setup instructions is acceptable if no hosted demo exists.
- Deadline from indexed official Kaggle/course snippets: July 6, 2026 at 11:59 PM PT. Re-check the Kaggle page before final upload.

## Writeup Outline

1. Problem statement
2. Solution overview
3. Demo links
4. Agent architecture
5. Course concepts demonstrated
6. Technical implementation
7. Evaluation and tests
8. Guardrails, security, and limitations
9. Impact and future work

## Video Outline

1. 0:00-0:30 Problem and target user
2. 0:30-1:00 Why this should be an agent, not a prompt
3. 1:00-2:30 Live demo
4. 2:30-3:30 Architecture and tests
5. 3:30-4:30 Guardrails, security, and deployability
6. 4:30-5:00 Impact and next step

## Next Build Slice

1. Record the demo video using the checklist in `docs/demo_video_script_checklist.md`.
2. Upload the video to YouTube and paste the real URL into the writeup.
3. Upload `docs/assets/kaggle_cover.png` as the cover image.
4. If time remains, add a hosted demo, but do not block submission on deployment because the public repo is runnable.

## Honest Current Scope

Completed in the current local app:

- Text brief intake for a restaurant or small-business campaign.
- Deterministic workflow that works without API keys.
- Audience insight, strategy, content types, LinkedIn post, carousel outline, photo/shot guidance, short content calendar, short video script, CTA, checklist, score, warnings, assumptions, and Markdown export.
- Automated tests for the core workflow and route behavior.

Do not claim as completed yet:

- Hosted deployment.
- Image/menu upload or vision analysis.
- Runtime Gemini / Google ADK integration.
