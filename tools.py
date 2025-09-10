# tools.py
from typing import List, Dict
import textwrap

def google_search_sim(query: str) -> List[Dict]:
    # Simulated results (swap with real Google SerpAPI, Tavily, etc.)
    return [
        {"title":"Startup Interview Loop Best Practices","url":"https://example.com/loop"},
        {"title":"Founding Engineer JD Examples","url":"https://example.com/jd"},
        {"title":"GenAI Intern Screening Guide","url":"https://example.com/genai-intern"}
    ]

def write_email(to:str, subject:str, body_points:List[str]) -> str:
    body = "\n\n".join(f"• {p}" for p in body_points)
    return textwrap.dedent(f"""\
    To: {to}
    Subject: {subject}

    Hi {to.split('@')[0].title()},

    {body}

    Best,
    HR Hiring Planner Agent
    """)

def build_checklist(weeks:int, role_titles:List[str]) -> List[Dict]:
    # Simple, opinionated plan
    tasks = []
    base = [
      "Kickoff & define success metrics",
      "Finalize JD & approve budget",
      "Open roles on ATS & sourcing plan",
      "Begin outreach & screening",
      "Tech screens & take-home (if any)",
      "Onsite/Panel interviews",
      "Debriefs & decision",
      "Offer & closing",
      "Pre-onboarding"
    ]
    for r in role_titles:
        for i, t in enumerate(base[:weeks] if weeks < len(base) else base, start=1):
            tasks.append({"week": i, "task": f"{r}: {t}", "owner":"Hiring Manager","status":"todo"})
    return tasks
