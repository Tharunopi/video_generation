from Utils.state import AgentState
from Helpers.agents import Agents
from Utils.prompt_templates.generate_image_promt_template import get_template
from Utils.logger import get_logger, log_step

logger = get_logger(__name__)
agent_loader = Agents()

def image_prompt_agent(state: AgentState):
    log_step(logger, "Image Prompt Generation", "started")
    logger.info(f"Converting {len(state.get('scenes', []))} scenes to image prompts...")
    
    agent = agent_loader.get_image_prompt_agent()
    prompt = get_template(state.get("scenes", []))

    logger.info("Calling LLM to generate image prompts...")
    response = agent.invoke({
    "messages": [{"role": "user", "content": prompt}]
    })

    result = [{
    "image_number": i.image_number,
    "title": i.title,
    "main_subject": i.main_subject,
    "visual_style": i.visual_style,
    "details": i.details,
    "negative_prompts": i.negative_prompts,
    "character_consistency": {"identity_tags": i.character_consistency.identity_tags, "style_lock": i.character_consistency.style_lock}
    } for i in response["structured_response"].image_prompt]

    logger.info(f"Generated {len(result)} image prompts")
    for p in result[:3]:  # Show first 3 prompts
        logger.debug(f"  Image {p['image_number']}: {p['title']}")
    
    log_step(logger, "Image Prompt Generation", "completed")
    return {"image_prompt": result,
            "revision_count_image_prompt": state.get("revision_count_image_prompt", 0) + 1}