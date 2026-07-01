# AI Marketing Ops Agent — Codex Build Plan for Kaggle Capstone

**Prepared for:** Shih Siang Yan  
**Project selected:** AI Marketing Ops Agent  
**Target competition:** Kaggle / Google — AI Agents: Intensive Vibe Coding Capstone Project  
**Prepared date:** 2026-06-20  
**Primary competition page:** https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/overview  
**Related course page:** https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google  
**Official Google announcement:** https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/  
**OpenAI Codex docs:** https://developers.openai.com/codex

---

## 1. Final Project Goal

Build a working **AI Marketing Ops Agent** that helps Vietnamese office workers, marketers, creators, and small business owners turn one business/content idea into a complete marketing campaign pack.

| Item | Decision |
|---|---|
| Project name | **AI Marketing Ops Agent** |
| Main user | Vietnamese office workers, marketers, creators, small business owners |
| Core problem | Users know what they want to promote, but struggle to turn it into a structured marketing workflow. |
| Main input | A business idea, product, campaign goal, target audience, tone, and platform. |
| Main output | Campaign brief, audience insight, positioning angle, LinkedIn post, carousel outline, short video script, CTA, publishing checklist, and quality score. |
| Submission strategy | Build a simple but complete MVP, explain the agentic workflow clearly, show evaluation/guardrails, and submit with public code + demo + Kaggle Writeup. |

---

## 2. Kaggle / Google Capstone Requirements Summary

> Important: Kaggle pages are partially dynamic. The safest approach is to include every asset below and manually verify the exact submission form before final upload.

| Requirement / Detail | What to Do for This Project | Source Confidence |
|---|---|---|
| Build an AI agent project | Build a working AI Marketing Ops Agent, not only a prompt template. | Official Kaggle capstone page snippet |
| Apply the 5-day course concepts | Explicitly map the project to vibe coding, tool/API use, memory/context, evaluation, guardrails, and production-readiness. | Official Google announcement + course context |
| Kaggle Writeup | Submit a clear project writeup explaining problem, solution, agent architecture, implementation, evaluation, and limitations. | Kaggle competition/writeup system |
| Attached resources | Include public links to code, demo video, and live/demo project where possible. | Kaggle competition docs and public capstone summaries |
| Public codebase | Use a public GitHub repository or public Kaggle Notebook. | Strongly recommended / safest submission practice |
| Video demo | Record a short screen demo showing the agent working end-to-end. | Public capstone summaries; verify in Kaggle form |
| Project/demo link | Provide a live app, public notebook, Hugging Face Space, Streamlit app, or clear runnable demo. | Public capstone summaries; verify in Kaggle form |
| Course dates | June 15–19, 2026. | Official Google announcement / Kaggle course page |
| Capstone live date | End of day, Friday, June 19, 2026. | Kaggle course page search result |
| Submission deadline | **Monday, July 6, 2026 at 11:59 PM PT**. Verify inside Kaggle before submitting. | Official Kaggle course page search result |
| Badge/certificate connection | Completion is tied to course recognition/badge/certificate. | Google Developer badge page |
| Rules / code sharing | Kaggle rules page exposes “Submission Code Requirements” and “Private Code Sharing” sections. Use public code and avoid private/unreachable resources. | Kaggle rules page snippet; verify manually |

---

## 3. Course Concepts This Project Must Demonstrate

| Course concept | How AI Marketing Ops Agent will demonstrate it |
|---|---|
| Vibe coding workflow | Use natural language as the main interface: user describes a marketing goal, and the agent turns it into a structured campaign. |
| Tool/API integration | Use at least one tool: source ingestion, web/search placeholder, file upload, memory store, markdown export, or quality evaluator. |
| “10x agent” leverage | Agent automates a multi-step marketing workflow: brief → audience insight → angle → content → evaluation → export. |
| Multi-step agent workflow | Use separate modules/agents for brief parsing, audience analysis, strategy, content generation, evaluation, and export. |
| Memory/context | Store brand voice, target audience, preferred language, previous campaigns, and reusable constraints. |
| Quality/testing | Include test examples, deterministic checks, and a scoring rubric for generated content. |
| Guardrails/security | Avoid unsupported factual claims, ask for missing context, protect API keys, and flag low-confidence outputs. |
| Production-readiness | Include README, environment setup, logging, clear deployment path, and reproducible demo. |

---

## 4. Recommended MVP Scope

Build the smallest project that still looks complete and capstone-worthy.

| Feature | Must Have | Nice to Have |
|---|---|---|
| User input form | Product/service, target audience, goal, platform, tone, language, constraints | File upload or URL source input |
| Brief Agent | Converts messy input into structured campaign brief | Detects missing fields and asks follow-up questions |
| Audience Agent | Generates pain points, objections, motivations, desired outcomes | Persona variants |
| Strategy Agent | Creates campaign angle, hook, positioning, message hierarchy | Multiple campaign angles |
| Content Agent | Generates LinkedIn post, carousel outline, video script, CTA | Repurposed email/newsletter/post variants |
| Evaluation Agent | Scores output using rubric | LLM-as-judge plus deterministic checks |
| Guardrails | Flags unsupported claims, generic output, weak CTA, missing audience | Source-based fact checking |
| Memory | Saves brand profile and preferences locally | User accounts / database sync |
| Export | Markdown output and copy-ready text | PDF export / Notion export |
| Demo UI | Streamlit app or Gradio app | Deployed public app |

---

## 5. Recommended Tech Stack

| Layer | Recommendation | Reason |
|---|---|---|
| Coding assistant | **OpenAI Codex** | You will use Codex to generate, edit, test, and refactor the project. |
| Language | Python | Fastest for agent workflows, Streamlit, evaluation, and Kaggle-friendly demos. |
| UI | Streamlit | Fastest working web demo for capstone. |
| Agent orchestration | Simple modular Python first; optionally LangGraph | Avoid overbuilding. Clear modules are easier to explain. |
| LLM provider | Gemini API preferred for Google/Kaggle alignment; provider abstraction recommended | Keeps the app aligned with course while allowing future model swaps. |
| Memory | SQLite or local JSON | Simple, reliable, demo-friendly. |
| Output format | Markdown | Easy to show, copy, export, and submit. |
| Tests | Pytest | Demonstrates quality and reproducibility. |
| Deployment | Streamlit Community Cloud / Hugging Face Spaces / local demo video | Quick public demo options. |
| Repo | GitHub public repository | Easy for judges/readers to inspect. |

---

## 6. Repository Structure to Ask Codex to Create

```text
ai-marketing-ops-agent/
├── AGENTS.md
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── app.py
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── agent_orchestrator.py
│   ├── llm_client.py
│   ├── memory_store.py
│   ├── export_markdown.py
│   ├── guardrails.py
│   ├── evaluators/
│   │   ├── __init__.py
│   │   └── content_quality.py
│   └── agents/
│       ├── __init__.py
│       ├── brief_agent.py
│       ├── audience_agent.py
│       ├── strategy_agent.py
│       ├── content_agent.py
│       └── evaluator_agent.py
├── examples/
│   ├── sample_input.json
│   └── sample_output.md
├── tests/
│   ├── test_guardrails.py
│   ├── test_evaluator.py
│   └── test_orchestrator.py
└── docs/
    ├── architecture.md
    ├── evaluation.md
    ├── kaggle_writeup.md
    ├── demo_script.md
    └── screenshots/
```

---

## 7. Codex Setup Instructions

### 7.1 Create the Project Folder

```bash
mkdir ai-marketing-ops-agent
cd ai-marketing-ops-agent
git init
```

### 7.2 Start Codex in the Project Root

Use Codex from the repository root so it can read the whole project context.

```bash
codex
```

### 7.3 Create `AGENTS.md` First

Codex reads `AGENTS.md` files before doing work, so create this file before asking Codex to implement features.

```markdown
# AGENTS.md

## Project
Build AI Marketing Ops Agent for the Kaggle / Google AI Agents: Intensive Vibe Coding Capstone Project.

## Goal
Create a working Streamlit app that turns a marketing goal into a complete campaign pack: brief, audience insight, positioning angle, LinkedIn post, carousel outline, short video script, CTA, publishing checklist, and quality score.

## Non-negotiable Requirements
- Keep the project simple, runnable, and demo-friendly.
- Use Python and Streamlit unless explicitly changed.
- Do not hardcode API keys.
- Use `.env.example` for environment variables.
- Keep generated content practical for Vietnamese office workers and marketing teams.
- Include guardrails for unsupported factual claims, weak outputs, and missing user context.
- Include tests for guardrails, evaluator, and orchestration.
- Update README whenever setup or commands change.
- After each implementation step, run tests or explain why tests cannot run.

## Coding Standards
- Prefer small functions and clear modules.
- Use type hints where practical.
- Use dataclasses or Pydantic-style models for structured data.
- Keep prompts in agent modules, not scattered across the UI.
- Return structured dictionaries/objects before rendering final Markdown.

## Commands
- Install: `pip install -r requirements.txt`
- Run app: `streamlit run app.py`
- Run tests: `pytest`

## Output Quality
Every campaign pack must include:
1. Structured marketing brief
2. Audience pain points and objections
3. Campaign angle and hook
4. LinkedIn post
5. Carousel outline
6. Short video script
7. CTA
8. Publishing checklist
9. Evaluation score with improvement suggestions
10. Assumptions and unsupported-claim warnings
```

---

## 8. Step-by-Step Codex Build Plan

### Phase 0 — Confirm Requirements and Scope

| Goal | Create a clear product scope before coding. |
|---|---|
| Codex task | Create `docs/project_spec.md` based on this plan. |
| Acceptance criteria | Problem, target user, MVP features, non-goals, deliverables, and Kaggle requirement mapping are documented. |

**Prompt for Codex**

```text
Create docs/project_spec.md for this project.
Use the selected project: AI Marketing Ops Agent for Kaggle/Google AI Agents Intensive Vibe Coding Capstone.
Include: problem statement, target users, MVP scope, non-goals, agent workflow, Kaggle requirement mapping, and definition of done.
Do not write code yet.
```

---

### Phase 1 — Scaffold the App

| Goal | Create a runnable Streamlit skeleton with clean folder structure. |
|---|---|
| Codex task | Create files/folders, requirements, `.env.example`, config, and sample UI. |
| Acceptance criteria | `streamlit run app.py` opens a basic page with input fields and placeholder output. |

**Prompt for Codex**

```text
Scaffold the Python Streamlit project using the repository structure in AGENTS.md.
Create requirements.txt, .env.example, .gitignore, app.py, src/config.py, src/models.py, and docs/architecture.md.
The app should show a form with: business name, product/service, target audience, campaign goal, platform, tone, language, constraints, and optional source notes.
For now, return a placeholder campaign pack.
Run formatting checks if available and tell me the run command.
```

---

### Phase 2 — Define Data Models

| Goal | Make the workflow structured and easy to test. |
|---|---|
| Codex task | Add models for user input, marketing brief, campaign output, and evaluation result. |
| Acceptance criteria | App uses structured objects instead of loose strings. |

**Prompt for Codex**

```text
Implement src/models.py with dataclasses for:
- CampaignInput
- MarketingBrief
- AudienceInsight
- CampaignStrategy
- ContentPack
- EvaluationResult
- CampaignPack
Update app.py to convert form input into CampaignInput.
Add tests that validate required fields and default values.
```

---

### Phase 3 — Implement the Agent Workflow

| Goal | Build an actual multi-step agentic workflow. |
|---|---|
| Codex task | Implement modular agents and an orchestrator. |
| Acceptance criteria | One user input produces a complete structured campaign pack. |

**Prompt for Codex**

```text
Implement the agent workflow with these modules:
- brief_agent.py: converts CampaignInput into MarketingBrief
- audience_agent.py: creates pain points, objections, desired outcomes
- strategy_agent.py: creates hook, positioning, key message, CTA direction
- content_agent.py: creates LinkedIn post, carousel outline, short video script, publishing checklist
- evaluator_agent.py: evaluates the output
- agent_orchestrator.py: runs the full workflow in order
Use simple deterministic logic first so the app works without an API key.
Add a clear TODO path for replacing deterministic logic with LLM calls.
Update tests for the orchestrator.
```

---

### Phase 4 — Add LLM Provider Abstraction

| Goal | Allow the project to use Gemini or another model without rewriting the app. |
|---|---|
| Codex task | Create a provider abstraction in `llm_client.py`. |
| Acceptance criteria | App works in mock mode without API keys and can use real API if configured. |

**Prompt for Codex**

```text
Create src/llm_client.py with an LLMClient interface and two implementations:
1. MockLLMClient for offline demo/testing
2. GeminiLLMClient placeholder that reads GEMINI_API_KEY from environment and raises a clear setup error if missing
Do not hardcode credentials.
Update agents so they can optionally use LLMClient but still work in mock mode.
Update README with environment setup.
```

---

### Phase 5 — Add Memory

| Goal | Demonstrate context and long-term state. |
|---|---|
| Codex task | Implement local memory for brand profile and previous campaigns. |
| Acceptance criteria | User can save/load brand preferences and the latest campaign output. |

**Prompt for Codex**

```text
Implement src/memory_store.py using local JSON or SQLite.
Store:
- brand name
- target audience
- preferred tone
- preferred language
- past campaign topics
- last generated campaign pack summary
Add Streamlit controls to save and load brand memory.
Add tests for memory save/load.
```

---

### Phase 6 — Add Guardrails

| Goal | Show responsible and reliable agent behavior. |
|---|---|
| Codex task | Implement content and safety checks. |
| Acceptance criteria | Output includes warnings for weak/missing/unsupported information. |

**Prompt for Codex**

```text
Implement src/guardrails.py with checks for:
- missing target audience
- unsupported factual claims
- overpromising results
- vague/generic content
- missing CTA
- sensitive or risky claims
The guardrail function should return warnings and improvement suggestions.
Integrate guardrails into the evaluator and final output.
Add tests for each guardrail.
```

---

### Phase 7 — Add Evaluation Rubric

| Goal | Make judging easier by showing measurable quality. |
|---|---|
| Codex task | Build a scoring evaluator with transparent criteria. |
| Acceptance criteria | Every campaign pack gets scores and recommended improvements. |

**Rubric**

| Criterion | Score | What It Checks |
|---|---:|---|
| Audience specificity | 1–5 | Is the target user clear? |
| Pain point relevance | 1–5 | Does it solve a real problem? |
| Hook strength | 1–5 | Is the first line strong enough? |
| Content usefulness | 1–5 | Does it give practical value? |
| Actionability | 1–5 | Can the user execute the advice? |
| Brand/tone fit | 1–5 | Does it match the requested tone/language? |
| CTA quality | 1–5 | Is the next action clear? |
| Risk control | 1–5 | Are unsupported claims or unsafe claims flagged? |

**Prompt for Codex**

```text
Implement src/evaluators/content_quality.py.
Create a transparent scoring rubric from 1 to 5 for each criterion:
- audience specificity
- pain point relevance
- hook strength
- content usefulness
- actionability
- brand/tone fit
- CTA quality
- risk control
Return total score, pass/fail, warnings, and improvement suggestions.
Integrate this into evaluator_agent.py and the Streamlit UI.
Add tests for high-quality and low-quality examples.
```

---

### Phase 8 — Add Markdown Export

| Goal | Make outputs easy to submit, copy, and demo. |
|---|---|
| Codex task | Generate a full Markdown campaign pack. |
| Acceptance criteria | User can download or copy a `.md` campaign output. |

**Prompt for Codex**

```text
Implement src/export_markdown.py.
Export the CampaignPack into clean Markdown with these sections:
1. Campaign Brief
2. Audience Insight
3. Campaign Strategy
4. LinkedIn Post
5. Carousel Outline
6. Short Video Script
7. CTA
8. Publishing Checklist
9. Evaluation Score
10. Guardrail Warnings
11. Assumptions
Add a Streamlit download button for the Markdown output.
Add sample output to examples/sample_output.md.
```

---

### Phase 9 — Improve UI for Demo

| Goal | Make the app easy to understand in a 3–5 minute video. |
|---|---|
| Codex task | Polish Streamlit layout and demo flow. |
| Acceptance criteria | The UI clearly shows input → agent steps → final output → evaluation. |

**Prompt for Codex**

```text
Improve the Streamlit UI for demo quality.
Use tabs or sections:
- Input Brief
- Agent Workflow
- Campaign Pack
- Evaluation
- Memory
Show each agent step clearly with status messages.
Add a sample input button for quick demo.
Do not add unnecessary complexity.
```

---

### Phase 10 — Add Tests and Quality Checks

| Goal | Make the submission credible and reproducible. |
|---|---|
| Codex task | Add tests and document commands. |
| Acceptance criteria | `pytest` runs successfully. README includes exact test command. |

**Prompt for Codex**

```text
Review the codebase and add/repair tests for:
- models validation/defaults
- guardrails
- evaluator rubric
- memory store
- orchestrator output shape
Run pytest and fix failures.
Update README with test instructions and known limitations.
```

---

### Phase 11 — Documentation for Kaggle

| Goal | Prepare all submission assets. |
|---|---|
| Codex task | Generate docs for GitHub and Kaggle Writeup. |
| Acceptance criteria | README, architecture, evaluation, demo script, and Kaggle writeup are ready. |

**Prompt for Codex**

```text
Create and update the documentation needed for Kaggle submission:
- README.md
- docs/architecture.md
- docs/evaluation.md
- docs/demo_script.md
- docs/kaggle_writeup.md

The writeup must include:
problem statement, target user, solution overview, agent architecture, vibe coding connection, tool/API use, memory/context, evaluation, guardrails, demo links placeholders, code link placeholder, limitations, and future work.
Keep it clear and submission-ready.
```

---

### Phase 12 — Final Review and Submission Prep

| Goal | Ensure no missing assets before Kaggle submission. |
|---|---|
| Codex task | Audit the project against the checklist. |
| Acceptance criteria | All required links/files are ready or clearly marked as TODO. |

**Prompt for Codex**

```text
Perform a final capstone submission audit.
Check:
- app runs from fresh clone
- README setup works
- no API keys/secrets committed
- tests pass
- sample input/output included
- Kaggle writeup complete
- demo script complete
- project maps clearly to Kaggle/Google course requirements
- public code/demo/video placeholders are easy to fill
Create docs/final_submission_checklist.md with pass/fail status and remaining TODOs.
```

---

## 9. Product Requirements

### 9.1 Input Requirements

| Field | Required | Example |
|---|---:|---|
| Business / creator name | Yes | Adam Yan AI |
| Product / service | Yes | AI workflow education for Vietnamese office workers |
| Target audience | Yes | Vietnamese office marketers and office workers |
| Campaign goal | Yes | Teach how to use AI agents for content production |
| Platform | Yes | LinkedIn |
| Tone | Yes | Practical, professional, direct |
| Language | Yes | English / Vietnamese / bilingual |
| Constraints | Optional | No hype, include actionable steps |
| Source notes | Optional | Existing product details, customer pain points, links, notes |

### 9.2 Output Requirements

| Output | Required Content |
|---|---|
| Campaign brief | Goal, target user, promise, product, platform, constraints |
| Audience insight | Pain points, objections, motivations, desired outcome |
| Campaign strategy | Core angle, hook, positioning, message hierarchy |
| LinkedIn post | Copy-ready post with hook, body, CTA |
| Carousel outline | 6–8 slides with slide title and body copy |
| Short video script | 30–60 second script with hook, main points, CTA |
| Publishing checklist | Final checks before posting |
| Evaluation score | Rubric scores, total score, pass/fail |
| Guardrail warnings | Unsupported claims, vague claims, missing context |
| Assumptions | What the agent assumed because user did not provide it |

---

## 10. Agent Architecture

| Agent / Module | Responsibility | Input | Output |
|---|---|---|---|
| Brief Agent | Normalize messy user input into structured brief | CampaignInput | MarketingBrief |
| Audience Agent | Identify target audience pain points and objections | MarketingBrief | AudienceInsight |
| Strategy Agent | Create positioning, hook, and campaign message | MarketingBrief + AudienceInsight | CampaignStrategy |
| Content Agent | Generate content assets | Strategy + AudienceInsight | ContentPack |
| Evaluator Agent | Score and critique output | CampaignPack | EvaluationResult |
| Guardrails Module | Detect risk and quality problems | Input + output | Warnings |
| Memory Store | Save/load brand context | Brand profile + campaign | Memory records |
| Export Module | Format final result | CampaignPack | Markdown |

---

## 11. Kaggle Writeup Outline

Use this in `docs/kaggle_writeup.md`.

```markdown
# AI Marketing Ops Agent

## 1. Problem Statement
Vietnamese office workers, marketers, creators, and small business owners often know what they want to promote, but struggle to turn ideas into structured, high-quality content campaigns.

## 2. Target Users
- Vietnamese office workers
- Marketing teams
- Small business owners
- LinkedIn creators and consultants

## 3. Solution Overview
AI Marketing Ops Agent turns a short business/content idea into a complete marketing campaign pack.

## 4. Why This Is an Agent
The system performs a multi-step workflow:
brief parsing → audience analysis → strategy → content generation → evaluation → export.

## 5. Vibe Coding Connection
The user controls the workflow through natural language campaign goals, and Codex was used to build the project through step-by-step natural-language implementation tasks.

## 6. Agent Architecture
Describe each module/agent and include diagram/screenshot.

## 7. Tools and APIs
Mention LLM provider, memory store, export tool, evaluation tool, and any optional API integrations.

## 8. Memory and Context
Explain saved brand profile, target audience, tone, language, and previous campaign context.

## 9. Evaluation
Show rubric, example scores, test cases, and improvement suggestions.

## 10. Guardrails and Security
Explain unsupported-claim warnings, missing-context checks, no hardcoded API keys, and safe output behavior.

## 11. Demo
- Live demo:
- Video demo:
- GitHub repo:

## 12. Results
Show sample input and sample output.

## 13. Limitations
Explain current limitations honestly.

## 14. Future Work
Mention source-grounded research, Notion export, scheduling, analytics, and multi-platform campaign generation.
```

---

## 12. Demo Video Script

Target length: **3–5 minutes**.

| Time | What to Show | Script Goal |
|---:|---|---|
| 0:00–0:20 | Title + problem | Explain who the project helps. |
| 0:20–0:50 | Input form | Show campaign goal and target audience. |
| 0:50–1:40 | Agent workflow | Show brief, audience, strategy, content, evaluation steps. |
| 1:40–2:40 | Final campaign pack | Show LinkedIn post, carousel outline, video script, CTA. |
| 2:40–3:20 | Evaluation/guardrails | Show score, warnings, and improvement suggestions. |
| 3:20–4:00 | Memory/export | Show saved brand profile and Markdown export. |
| 4:00–5:00 | Architecture + close | Explain how it maps to Kaggle course requirements. |

---

## 13. Final Submission Assets

| Asset | File / Link | Status |
|---|---|---|
| Public GitHub repository | `TODO` | ☐ |
| Live demo or runnable notebook | `TODO` | ☐ |
| Demo video | `TODO` | ☐ |
| Kaggle Writeup | `docs/kaggle_writeup.md` | ☐ |
| README | `README.md` | ☐ |
| Architecture docs | `docs/architecture.md` | ☐ |
| Evaluation docs | `docs/evaluation.md` | ☐ |
| Sample input/output | `examples/` | ☐ |
| Tests | `tests/` | ☐ |
| Final checklist | `docs/final_submission_checklist.md` | ☐ |

---

## 14. Final Quality Checklist

| Check | Required Result |
|---|---|
| App runs locally | `streamlit run app.py` works from fresh clone. |
| Tests pass | `pytest` passes or known failures are documented. |
| No secrets committed | API keys are only in local `.env`, not GitHub. |
| README complete | Setup, run, test, demo, limitations included. |
| Clear agent workflow | Multi-step flow is visible in UI and docs. |
| Memory included | Brand/user preferences can be saved or loaded. |
| Evaluation included | Score and suggestions are generated. |
| Guardrails included | Warnings for missing context/unsupported claims/generic output. |
| Sample output included | Judges can quickly understand the result. |
| Kaggle Writeup complete | Problem, solution, architecture, demo, eval, limitations. |
| Video public | Link works without permission request. |
| Code public | GitHub/Kaggle Notebook accessible. |
| Demo accessible | Live app or reproducible run instructions available. |
| Deadline verified | Check final deadline/timezone inside Kaggle before submission. |

---

## 15. Submission Risk Controls

| Risk | Prevention |
|---|---|
| Missing Kaggle field | Manually open Kaggle submission page before final day and list required fields. |
| Private/unreachable video | Use YouTube unlisted or public Drive link with viewer access. |
| Private code repo | Make GitHub repository public before submitting. |
| App fails during demo | Record working video and include sample output in repo. |
| API key missing | Provide mock mode and `.env.example`. |
| Overbuilt project unfinished | Finish MVP first, then add optional features. |
| Generic output | Use evaluator to penalize vague content. |
| Hallucinated claims | Require assumptions/warnings and avoid unsupported factual claims. |
| Weak capstone alignment | Include a requirement-mapping table in README and Kaggle Writeup. |

---

## 16. Recommended Build Order

| Priority | Build Item | Reason |
|---:|---|---|
| 1 | Streamlit skeleton | Gives immediate demo surface. |
| 2 | Structured models | Prevents messy workflow. |
| 3 | Deterministic agent workflow | Ensures app works without API. |
| 4 | Evaluation + guardrails | Strong Kaggle differentiator. |
| 5 | Memory | Shows course concept clearly. |
| 6 | LLM integration | Improves quality after core app works. |
| 7 | Markdown export | Makes output useful and demo-friendly. |
| 8 | Tests | Proves reliability. |
| 9 | README/docs/writeup | Required for submission. |
| 10 | Video/demo links | Final Kaggle assets. |

---

## 17. Source Notes

| Source | What It Supports |
|---|---|
| Kaggle Capstone Page | Competition title, capstone context, submission requirements section. |
| Kaggle Course Page | Course timeline, capstone live timing, official deadline search result. |
| Google Official Announcement | Course dates, vibe coding focus, production-ready agents, tools/API integration, capstone context. |
| Google Developer Badge Page | Badge/certificate context: prototype to scalable/observable deployments culminating in capstone. |
| Kaggle Competition Docs | Judges review writeups and attached resources for relevant competitions. |
| OpenAI Codex Docs | Codex as a coding agent; AGENTS.md project guidance; CLI/IDE workflows. |

---

## 18. Reference Links

1. Kaggle Capstone Page  
   https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/overview

2. Kaggle Course Page  
   https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google

3. Google Official Announcement  
   https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/

4. Google Developer Badge Page  
   https://developers.google.com/profile/badges/events/cloud/five-day-ai-agents

5. Kaggle Competition Documentation  
   https://www.kaggle.com/docs/competitions

6. OpenAI Codex Docs  
   https://developers.openai.com/codex

7. Codex `AGENTS.md` Guide  
   https://developers.openai.com/codex/guides/agents-md

---

## 19. Immediate Next Action

Start with **Phase 0 and Phase 1** only. Do not jump directly into advanced agent frameworks.

**First Codex prompt to use:**

```text
Read AGENTS.md and create docs/project_spec.md for AI Marketing Ops Agent.
Then scaffold the Streamlit app with the repository structure described in AGENTS.md.
Keep the first version simple and runnable.
Do not add complex dependencies yet.
After scaffolding, show me the exact commands to install, run, and test the project.
```
