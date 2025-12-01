from Utils.state import AgentState
from Utils.prompt_templates.regenerate_scene_agent_template import get_template
from Helpers.agents import Agents

agent_loader = Agents()

def regenerate_scene_agent(state: AgentState):
    agent = agent_loader.get_scene_agent()
    prompt = get_template(state.get("scenes", []), state.get("eval_result_scenes", ""))

    response = agent.invoke({
    "messages": [{"role": "user", "content": prompt}]
    })

    list_of_scenes = [{
        "scene_number": i.scene_number,
        "location": i.location,
        "time_of_day": i.time_of_the_day,
        "characters_present": i.characters_present,
        "brief_description": i.brief_description,
        "dialogue_summary": i.dialogue_summary
    } for i in response["structured_response"].scenes]

    return {
        "scenes": list_of_scenes,
        "revision_count_scenes": state.get("revision_count_scenes") + 1
    }