# prompts.py
SYSTEM_PROMPT = """You are an HR Hiring Planner Agent for startups.
Goal: Clarify needs, propose role specs, draft job descriptions, and build a hiring plan/checklist.
Output must be concise, structured, and actionable."""

CLARIFYING_QUESTIONS = [
  "What is the total budget and comp bands per role (base/equity/bonus/intern stipend)?",
  "What timeline are you targeting (weeks to first hire)?",
  "Location & remote policy?",
  "Required vs nice-to-have skills per role?",
  "Employment type (FT/Intern/Contract)?",
  "Team context (stage, product, tech stack), manager, interviewers?",
  "Must-have hiring constraints (visa, time-zone overlap)?",
  "Preferred sourcing channels (LinkedIn, GitHub, referrals, universities)?",
  "Decision-making process (who signs off) and offer process?"
]
