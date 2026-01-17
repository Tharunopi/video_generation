from Utils.state import AgentState
from Utils.prompt_templates.scene_creator_agent_template import get_scene_creator_prompt
from Helpers.agents import Agents
from Utils.logger import get_logger, log_step

logger = get_logger(__name__)
agent_loader = Agents()

def scene_creater_agent(state: AgentState):
    log_step(logger, "Scene Creation", "started")
    logger.info("Reading script and generating scenes...")
    
    agent = agent_loader.get_scene_agent()
    prompt = get_scene_creator_prompt(script=state.get("script", ""))

    logger.info("Calling LLM to break down script into scenes...")
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

    logger.info(f"Generated {len(list_of_scenes)} scenes")
    for scene in list_of_scenes[:3]:  # Show first 3 scenes
        logger.debug(f"  Scene {scene['scene_number']}: {scene['location']} - {scene['brief_description'][:50]}...")
    
    log_step(logger, "Scene Creation", "completed")
    return {
        "scenes": list_of_scenes,
        "revision_count_scenes": state.get("revision_count_scenes", 0) + 1
    }