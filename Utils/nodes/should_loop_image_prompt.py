from Utils.state import AgentState

def should_loop_image_prompt(state: AgentState):
    if state.get("is_approved_image_prompt"):
        return "end"
    elif state.get("revision_count_image_prompt") > 10:
        return "end"
    else:
        return "revise"