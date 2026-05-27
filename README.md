# Risk Assessment Tool

An AI-powered compliance risk assessment chatbot built with Claude and Flask. It conducts structured, conversational audits of security controls across compliance frameworks and produces a downloadable risk register — the kind of document that normally takes days to produce manually.

Built as part of [Truzta](https://truzta.com), a compliance assistant platform.

---

## What It Does

Most compliance audits are painful — long spreadsheets, vague questions, and hours of back-and-forth. This tool replaces that process with a natural conversation.

You select a compliance framework, answer Claude's questions about your security controls, and walk away with a structured risk register you can hand to an auditor.

**Supported frameworks:**
- SOC 2 (Trust Service Criteria)
- ISO 27001 (Information Security Management)

---

## Features

- **Conversational auditing** — Claude interviews you like a real auditor, asking intelligent follow-up questions based on your answers
- **Calibrated to your organisation** — tool recommendations adjust based on your headcount (startup vs. enterprise)
- **Structured risk output** — every control produces a risk record with likelihood score, impact score, residual risk, recommended tool, and treatment action
- **CSV export** — download your full risk register with one click, ready to share with auditors or import into a GRC platform
- **Progress tracking** — real-time progress bar so you always know where you are in the assessment
- **Framework-specific guidance** — tool recommendations are tailored per framework (e.g. Okta for access control under SOC 2, ISO-aligned controls for 27001)

---

## How It Works

1. Select your compliance framework and enter your organisation name
2. Tell Claude your headcount — this calibrates the recommendations
3. Claude assesses each control one at a time, asking up to 3 follow-up questions before producing a finding
4. Each completed control generates a risk record automatically
5. When all controls are done, download your risk register as a CSV

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI | Claude Haiku via Anthropic SDK |
| Frontend | Vanilla JavaScript, HTML, CSS |
| Export | CSV (Python's csv module) |
| Config | python-dotenv |

No database — all session state lives in the browser, making the backend completely stateless.

---

## Getting Started

**Requirements:** Python 3.x, an Anthropic API key

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-USERNAME/risk-assessment-tool.git
cd risk-assessment-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key
cp .env.example .env
# Open .env and add your key:
# ANTHROPIC_API_KEY=your_key_here

# 4. Run the app
python app.py

# 5. Open http://localhost:5000 in your browser
```

---

## Project Structure

```
risk-assessment-tool/
├── app.py              # Flask backend, Claude API calls, CSV export logic
├── questions.py        # Control questions for each framework
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── static/
│   ├── script.js       # Frontend logic and state management
│   └── style.css       # Chat interface styling
└── templates/
    └── index.html      # Main UI template
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Serve the main UI |
| GET | `/api/questions/<framework>` | Return control questions for a framework |
| POST | `/api/chat` | Send a message and get Claude's assessment response |
| POST | `/api/export` | Generate and download the risk register CSV |

---

## Adding a New Framework

1. Add a new entry to the `QUESTIONS` dict in `questions.py`
2. Add a framework card in `templates/index.html`
3. Optionally add tool guidance to `FRAMEWORK_TOOLS` in `app.py`

No other changes needed.

---

## Limitations

**Usability**
- Runs locally — there is no hosted version, so users must set up Python and an API key themselves
- No user accounts or login — anyone with the link (if deployed) can access it
- Session data is lost on page refresh — if you close the browser mid-assessment, you start over
- No way to pause and resume an assessment across sessions
- Assessment flow is linear — you cannot skip a control and come back to it

**Product**
- No persistent storage — completed risk registers only exist as downloaded CSV files, not in a database
- Single user at a time per session — not built for team collaboration or multi-reviewer workflows
- No audit trail — there is no record of who ran the assessment, when, or what answers were given
- Control questions are hardcoded — updating the question bank requires editing `questions.py` directly
- Completely dependent on the Anthropic API — no offline fallback if the API is unavailable
- Claude's assessments are probabilistic — findings should always be reviewed by a qualified professional before being used in a real audit

---

## Next Steps — Making This a Real Product

**Step 1 — Add a database**
Replace browser-state with a proper database (PostgreSQL via SQLAlchemy). This enables saved sessions, audit history, and the ability to pause and resume assessments. Every risk register gets stored, not just downloaded once.

**Step 2 — User authentication**
Add login with email/password or Google OAuth (using Flask-Login or Supabase Auth). This unlocks multi-user support and personal assessment history.

**Step 3 — Deploy it**
Host on [Railway](https://railway.app) or [Render](https://render.com) — both support Flask apps with a free tier. Once deployed, you have a real shareable URL. Add a custom domain and it's a product.

**Step 4 — Team collaboration**
Allow multiple reviewers to work on the same assessment — one person answers, another reviews and approves findings. Add commenting and status tracking per control.

**Step 5 — Richer exports**
Beyond CSV, export to PDF (for auditors), Excel (for GRC teams), or push directly into platforms like Vanta, Drata, or Notion via their APIs.

**Step 6 — Expand framework coverage**
Add HIPAA, PCI-DSS, NIST CSF, and CIS Controls. The architecture already supports new frameworks with minimal code changes.

---

## Author

Built by Fahad — a beginner developer learning AI engineering by building real things.
