from Utils.state import AgentState

def should_loop_scenes(state: AgentState):
    if state.get("is_approved_scenes"):
        return "end"
    elif state.get("revision_count_scenes") > 10:
        return "end"
    else: 
        return "revise"