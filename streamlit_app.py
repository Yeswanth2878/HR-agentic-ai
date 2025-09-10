# streamlit_app.py
import streamlit as st
import uuid
from typing import Any, Dict

from schemas import ConversationState  # <-- ensure we can rehydrate the state
from memory import load_session, save_session, track
from graph.graph import build_graph

st.set_page_config(page_title="HR Hiring Planner", layout="wide")
st.title("🧭 Agentic HR Hiring Planner")

# ---- helpers ---------------------------------------------------------------
def ensure_state(x: Any) -> ConversationState:
    """LangGraph may return a dict; normalize to ConversationState."""
    if isinstance(x, ConversationState):
        return x
    if isinstance(x, dict):
        return ConversationState(**x)
    raise TypeError(f"Unexpected graph output type: {type(x)}")

def parse_kv_blob(blob: str) -> Dict[str, str]:
    """Parse 'k=v; k2=v2' into a dict, tolerant to spaces."""
    out: Dict[str, str] = {}
    if not blob:
        return out
    for pair in [p.strip() for p in blob.split(";") if p.strip()]:
        if "=" in pair:
            k, v = pair.split("=", 1)
            out[k.strip()] = v.strip()
    return out

# ---- session ---------------------------------------------------------------
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())[:8]
if "state" not in st.session_state:
    st.session_state.state = load_session(st.session_state.session_id)

# Build graph (optionally enforce types if your LangGraph version supports it)
graph = build_graph()
try:
    # If available, this guarantees type-stable I/O
    graph = graph.with_types(input_type=ConversationState, output_type=ConversationState)  # type: ignore[attr-defined]
except Exception:
    pass

# ---- UI --------------------------------------------------------------------
tab1, tab2 = st.tabs(["Chat", "Artifacts"])
with tab1:
    user_text = st.text_input(
        "Tell me what you need:",
        placeholder="I need to hire a founding engineer and a GenAI intern.",
    )
    out_mode = st.radio("Output format", ["markdown", "json"], horizontal=True)
    answers_blob = st.text_area(
        "Clarifications (key=value; ...)",
        placeholder="budget=$180k-$230k; timeline_weeks=6; location=Remote; employment_type=Full-time",
    )

    if st.button("Run Agent"):
        state = st.session_state.state
        # update mode & user message
        state.mode = out_mode
        if user_text:
            state.user_message = user_text

        # merge clarifications
        parsed = parse_kv_blob(answers_blob)
        state.answers.update(parsed)

        # propagate common fields to roles
        for r in state.roles:
            if "location" in state.answers:
                r.location = state.answers["location"]
            if "budget" in state.answers:
                r.budget_range = state.answers["budget"]
            if "employment_type" in state.answers:
                r.employment_type = state.answers["employment_type"]

        # run through the graph nodes
        try:
            for node in ["intake", "clarify", "plan_roles", "draft_jd", "checklist", "tools", "finalize"]:
                result = graph.invoke(state)  # some versions return dict
                state = ensure_state(result)
                track(state.session_id, node)
        except Exception as e:
            st.error(f"Agent run failed: {e}")
        else:
            save_session(state)
            st.session_state.state = state
            st.success("Agent run complete.")

    # Render final output
    if st.session_state.state.mode == "json":
        st.json(st.session_state.state.artifacts.get("final_json", {}))
    else:
        st.markdown(st.session_state.state.artifacts.get("final_markdown", ""))

    # Show clarifying questions (for convenience)
    if st.session_state.state.clarifying_questions:
        st.markdown("### Clarifying Questions")
        for q in st.session_state.state.clarifying_questions:
            st.markdown(f"- {q}")

with tab2:
    st.subheader("Artifacts")
    st.markdown("### Search Results")
    st.markdown(st.session_state.state.artifacts.get("search_results", ""))
    st.markdown("### Approval Email")
    st.code(st.session_state.state.artifacts.get("approval_email", ""))
