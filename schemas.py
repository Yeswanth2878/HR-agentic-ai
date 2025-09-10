from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class RoleSpec(BaseModel):
    title: str
    level: Optional[str] = None                  # e.g., "Founding Engineer", "Intern"
    employment_type: Optional[str] = None        # FT/PT/Intern/C2C
    budget_range: Optional[str] = None           # "$160k-$220k" or "Hourly $25-$35"
    location: Optional[str] = None
    remote_policy: Optional[str] = None          # "Remote-first/Hybrid/Onsite"
    must_have_skills: List[str] = Field(default_factory=list)
    nice_to_have_skills: List[str] = Field(default_factory=list)
    timeline_weeks: Optional[int] = None

class JD(BaseModel):
    title: str
    markdown: str
    json: Dict[str, Any]

class ChecklistItem(BaseModel):
    week: int
    task: str
    owner: str = "Hiring Manager"
    status: str = "todo"

class HiringPlan(BaseModel):
    role_title: str
    interview_loop: List[Dict[str, str]]         # [{"round":"Tech Screen","panel":"Sr Eng","signal":"problem solving"}]
    sourcing_channels: List[str]
    success_metrics: List[str]                   # time to fill, quality of hire etc.

class ConversationState(BaseModel):
    session_id: str
    user_message: str = ""
    clarifying_needed: bool = True
    clarifying_questions: List[str] = Field(default_factory=list)
    answers: Dict[str, str] = Field(default_factory=dict)
    roles: List[RoleSpec] = Field(default_factory=list)
    jds: List[JD] = Field(default_factory=list)
    plans: List[HiringPlan] = Field(default_factory=list)
    checklist: List[ChecklistItem] = Field(default_factory=list)
    artifacts: Dict[str, Any] = Field(default_factory=dict)   # named markdown/JSON artifacts
    mode: str = "markdown"                                    # or "json"
