from Utils.state import AgentState
from Utils.prompt_templates import eval_scene_agent_template
from Helpers.agents import Agents

agent_loader = Agents()

def eval_scene_agent(state: AgentState):
    agent = agent_loader.get_eval_scene_agent()
    prompt = eval_scene_agent_template.get_template(state.get("scenes", []))

    response = agent.invoke({
    "messages": [{"role": "user", "content": prompt}]
    })

    return {
        "is_approved_scenes": response["structured_response"].is_approved_scenes,
        "eval_result_scenes": response["structured_response"].correction
    }