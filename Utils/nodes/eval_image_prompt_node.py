from Utils.state import AgentState
from Helpers.agents import Agents
from Utils.prompt_templates.eval_image_agent_template import get_template

agent_loader = Agents()

def eval_image_prompt_node(state: AgentState):
    agent = agent_loader.get_eval_image_prompt_agent()
    prompt = get_template(state.get("scenes", []), state.get("image_prompt", []))

    response = agent.invoke({
    "messages": [{"role": "user", "content": prompt}]
    })

    return {
        "is_approved_image_prompt": response["structured_response"].is_approved_image_prompt,
        "eval_result_image_prompt": response["structured_response"].correction
    }