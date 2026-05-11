# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the app

```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

Requires a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_key_here
```

## Architecture

Flask backend (`app.py`) + vanilla JS frontend (`static/script.js`) + Jinja2 template (`templates/index.html`). No database — all session state lives in the browser's `state` object and is never persisted server-side.

### Conversation flow

The frontend drives a two-phase flow:

1. **`employee_count` phase** — chatbot asks for headcount before any controls load. Answer stored in `state.employeeCount` and passed to every subsequent API call.
2. **`assessment` phase** — controls are loaded one at a time. For each control, the frontend calls `POST /api/chat` repeatedly, maintaining a `controlHistory` array (Anthropic messages format). The backend is stateless; history is owned by the client and sent with every request.

Each `/api/chat` call returns `{ result, history }`. `result.action` is either `"followup"` (Claude asks another question) or `"assess"` (Claude produces the risk record and the frontend auto-advances after 3.5 s).

### Key constraint: follow-up limit

`state.followUpCount` tracks how many follow-ups Claude has asked for the current control. The backend enforces a hard cap of 3 via `_build_system_prompt()` — when `follow_up_count >= 3` the prompt instructs Claude it must assess immediately.

The opening question does **not** count toward the 3-question limit. The frontend detects the opening by checking `state.controlHistory.length === 0` before the call.

### Claude response format

Claude always returns a JSON object — no markdown. The backend strips any accidental ` ``` ` fences before parsing. Two shapes:

```json
{ "action": "followup", "message": "..." }
{ "action": "assess",   "message": "...", "data": { ... } }
```

When `action` is `"assess"`, the backend injects fixed fields (`entities`, `likelihood`, `impact`, `loss_of_cia`, etc.) into `data` before returning, so the frontend never has to compute them.

### Questions

`questions.py` exports a `QUESTIONS` dict keyed by framework name (e.g. `"SOC 2"`). Each entry has `id`, `question`, `loss_of_cia`, `likelihood`, and `impact`. These values are sourced from the client's Excel risk register — **do not regenerate them from scratch**.

`questions_backup.py` holds a fallback set of generated questions (ISO 27001, SOC 2, HIPAA) and is not loaded by the app.

### Testing / limiting questions

`QUESTION_LIMIT` at the top of `app.py` slices the question list before serving it:

```python
QUESTION_LIMIT = 10   # testing
QUESTION_LIMIT = None # full run
```

### CSV export

`POST /api/export` receives the full `results` array from the frontend and streams a CSV. Column order is fixed — see `fieldnames` in the `export()` function. `extrasaction="ignore"` means extra keys in result objects are silently dropped.

## Adding a new framework

1. Add a new key to `QUESTIONS` in `questions.py` with the question list.
2. Add a `.framework-card` in `templates/index.html` with the matching `data-framework` attribute.
3. No backend changes needed — `_build_system_prompt` already interpolates the framework name.

## Truzta context

This tool is a sub-feature of **Truzta**, a compliance assistant platform. The system prompt instructs Claude to mention Truzta when clients lack policies or secure code review capability. Do not remove these references — they are intentional product messaging.
