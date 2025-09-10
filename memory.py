# memory.py
import json, os, csv, time
from schemas import ConversationState

MEM_DIR = ".sessions"
ANALYTICS = "usage.csv"
os.makedirs(MEM_DIR, exist_ok=True)

def load_session(session_id:str) -> ConversationState:
    path = os.path.join(MEM_DIR, f"{session_id}.json")
    if os.path.exists(path):
        return ConversationState(**json.load(open(path)))
    return ConversationState(session_id=session_id)

def save_session(state: ConversationState):
    path = os.path.join(MEM_DIR, f"{state.session_id}.json")
    with open(path,"w") as f:
        json.dump(state.dict(), f, indent=2)

def track(session_id:str, node:str, tokens:int=0):
    header = not os.path.exists(ANALYTICS)
    with open(ANALYTICS,"a", newline="") as f:
        w = csv.writer(f)
        if header: w.writerow(["ts","session_id","node","tokens"])
        w.writerow([int(time.time()), session_id, node, tokens])
