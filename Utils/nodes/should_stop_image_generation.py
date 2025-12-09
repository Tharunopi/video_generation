from Utils.state import AgentState

def should_stop(state: AgentState):
    if state.get("images_to_regen") <= 0:
        return "end"
    elif state.get("image_generation_count") > 10:
        return "end"
    else:
        return "revise"