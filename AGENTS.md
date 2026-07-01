# AGENTS.md

## Project
Build AI Marketing Ops Agent for the Kaggle / Google AI Agents Intensive Vibe Coding Capstone Project.

## Direction
- Python-first agent core.
- FastAPI + Jinja + Tailwind UI.
- No Streamlit.
- Keep the MVP runnable without API keys.
- Add Gemini / Google ADK integration only after deterministic workflow, tests, and UI work.

## Non-Negotiables
- Do not hardcode API keys or secrets.
- Use `.env.example` for environment variables.
- Use TDD for production logic: failing test first, minimal code second.
- Keep the app useful for Vietnamese office workers, marketers, creators, and small business owners.
- Generated campaign packs must include brief, audience insight, strategy, LinkedIn post, carousel outline, short video script, CTA, checklist, evaluation, warnings, and assumptions.
- The UI must feel like a professional product workbench, not a notebook demo.

## Commands
- Create venv: `python3 -m venv .venv`
- Install: `.venv/bin/python -m pip install -r requirements.txt`
- Run tests: `.venv/bin/python -m pytest`
- Run app: `.venv/bin/uvicorn app.main:app --reload`

## UI Principles
- Dense enough for repeated work, clean enough for a capstone demo.
- Use clear labels, visible focus states, accessible contrast, responsive layout, and honest sample content.
- Avoid generic AI-purple gradients, fake metrics, decorative clutter, and placeholder-only screens.
