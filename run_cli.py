# run_cli.py
import uuid
from graph.graph import build_graph
from memory import load_session, save_session, track
from schemas import ConversationState
from config import DEFAULT_MODE

if __name__ == "__main__":
    session_id = str(uuid.uuid4())[:8]
    graph = build_graph()
    state = load_session(session_id)
    print(f"(session {session_id}) Type your need, or 'answers:' to provide clarifications.")
    while True:
        msg = input("> ").strip()
        if msg.lower().startswith("answers:"):
            # format: answers: budget=$200k; timeline_weeks=6; location=SF; ...
            pairs = [p.strip() for p in msg[8:].split(";") if p.strip()]
            for p in pairs:
                k,v = p.split("=",1)
                state.answers[k.strip()] = v.strip()
            # map common keys to roles
            for r in state.roles:
                if "location" in state.answers: r.location = state.answers["location"]
                if "budget" in state.answers: r.budget_range = state.answers["budget"]
                if "employment_type" in state.answers: r.employment_type = state.answers["employment_type"]
            state.mode = DEFAULT_MODE
        elif msg.lower() in ("quit","exit"):
            break
        else:
            state.user_message = msg

        for node in ["intake","clarify","plan_roles","draft_jd","checklist","tools","finalize"]:
            state = graph.invoke(state, config={})
            track(session_id, node)
        save_session(state)

        if state.mode == "json":
            print(state.artifacts.get("final_json"))
        else:
            print(state.artifacts.get("final_markdown"))
        print("\nClarifying Q’s (answer via `answers: key=value; ...`):")
        for q in state.clarifying_questions:
            print(f"- {q}")
