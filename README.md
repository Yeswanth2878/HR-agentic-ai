🧭 Agentic HR Hiring Planner

An agentic AI application that helps HR professionals plan a startup hiring process.
Simply type something like:

I need to hire a founding engineer and a GenAI intern. Can you help?


The agent will then:

Ask clarifying questions (budget, skills, timeline, location, etc.)

Suggest job description (JD) drafts

Create a hiring checklist / plan

Present results in structured Markdown or JSON

Provide supporting artifacts like a draft approval email and simulated search results

✨ Features

Multi-step reasoning via LangGraph

intake → clarify → plan_roles → draft_jd → checklist → tools → finalize

Clarifying Q&A to collect missing information

Job Descriptions in Markdown + JSON

Hiring Checklists with week-by-week tasks

Tool integrations (simulated Google search, email writer, checklist builder)

Memory: file-based session persistence

Analytics: CSV log of session runs

Frontends:

CLI (terminal runner)

Streamlit app with a clean, interactive UI

User Input (need + clarifications)
        │
        ▼
 ┌──────────────┐
 │   Intake     │   → parse request
 └──────────────┘
        ▼
 ┌──────────────┐
 │  Clarify     │   → ask budget, skills, location, etc.
 └──────────────┘
        ▼
 ┌──────────────┐
 │  Plan Roles  │   → build RoleSpec objects
 └──────────────┘
        ▼
 ┌──────────────┐
 │  Draft JD    │   → generate job descriptions
 └──────────────┘
        ▼
 ┌──────────────┐
 │  Checklist   │   → week-by-week hiring plan
 └──────────────┘
        ▼
 ┌──────────────┐
 │   Tools      │   → search results + approval email
 └──────────────┘
        ▼
 ┌──────────────┐
 │  Finalize    │   → artifacts: final_markdown + final_json
 └──────────────┘


📂 Project Structure
.
.
├── config.py          # Model & default config
├── memory.py          # Session persistence + analytics logging
├── prompts.py         # System prompt + clarifying questions
├── run_cli.py         # CLI entrypoint
├── schemas.py         # Pydantic models (RoleSpec, JD, Checklist, State)
├── streamlit_app.py   # Streamlit frontend
├── tools.py           # Simulated tools (search, email, checklist)
├── requirements.txt   # Dependencies
└── graph/graph.py     # (not shown here) defines LangGraph pipeline


🚀 Getting Started
1. Install dependencies
pip install -r requirements.txt

2. Run in CLI mode
python run_cli.py


Example:

(session ab12cd) Type your need, or 'answers:' to provide clarifications.
> I need to hire a founding engineer and a GenAI intern
... agent runs ...
Clarifying Q’s (answer via `answers: key=value; ...`):
- What is the total budget and comp bands per role (base/equity/bonus/intern stipend)?
- What timeline are you targeting (weeks to first hire)?
...


Provide clarifications inline:

> answers: budget=$200k; timeline_weeks=6; location=Remote

3. Run in Streamlit
streamlit run streamlit_app.py


Chat Tab: enter need, clarifications, output format → click Run Agent

Artifacts Tab: view simulated search results + draft approval email

Choose Markdown for human-readable planning or JSON for structured outputs.

📊 Example Outputs
Markdown Output
# Hiring Results

## Job Descriptions
### Founding Engineer
...

## Checklist
- [ ] (Week 1) Founding Engineer: Kickoff & define success metrics
- [ ] (Week 2) Founding Engineer: Finalize JD & approve budget
...

JSON Output
{
  "roles": [
    {
      "title": "Founding Engineer",
      "budget_range": "$200k",
      "location": "Remote"
    }
  ],
  "jds": [...],
  "checklist": [...]
}

⚙️ Tech Specs

LangGraph ≥ 0.2.0 for multi-step reasoning

Pydantic v2 for strict state modeling

Streamlit ≥ 1.36 for frontend

File-based sessions (.sessions/{id}.json)

Analytics CSV (usage.csv) with timestamp, session id, node, tokens

🔮 Roadmap

 Add real Google Search / Tavily integration

 Support sending actual emails

 Extend checklist with owners/due dates from answers

 Deploy Streamlit app for remote teams



MIT License – free to use and modify.

Would you like me to also add example screenshots (mockups of the Streamlit UI + CLI run) into the README for clarity, or keep it text-only?
