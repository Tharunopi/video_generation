from Utils.state import AgentState
from Utils.prompt_templates import eval_scene_agent_template
from Helpers.agents import Agents
from Utils.logger import get_logger, log_step

logger = get_logger(__name__)
agent_loader = Agents()

def eval_scene_agent(state: AgentState):
    log_step(logger, "Scene Evaluation", "started")
    logger.info(f"Evaluating {len(state.get('scenes', []))} scenes...")
    
    agent = agent_loader.get_eval_scene_agent()
    prompt = eval_scene_agent_template.get_template(state.get("scenes", []))

    logger.info("Calling LLM to evaluate scenes...")
    response = agent.invoke({
    "messages": [{"role": "user", "content": prompt}]
    })

    is_approved = response["structured_response"].is_approved_scenes
    correction = response["structured_response"].correction
    
    if is_approved:
        logger.info("Scenes APPROVED!")
    else:
        logger.warning(f"Scenes NEED REVISION: {correction[:100]}...")
    
    log_step(logger, "Scene Evaluation", "completed")
    return {
        "is_approved_scenes": is_approved,
        "eval_result_scenes": correction
    }