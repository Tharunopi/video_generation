from Helpers.agents import Agents
from Utils.state import AgentState
from Utils.image_inference.client import generate_image
from Utils.logger import get_logger, log_step

logger = get_logger(__name__)
agent_loader = Agents()

def image_generation_agent(state: AgentState):
    log_step(logger, "Image Generation", "started")
    prompts = state.get("image_prompt")
    generation_count = state.get("image_generation_count")
    images_generated = []
    
    logger.info(f"Generating {len(prompts)} images (attempt #{generation_count + 1})...")

    for idx, i in enumerate(prompts, 1):
        file_name = f"image_number_{i['image_number']}.{generation_count+1}"
        image_prompt = f"{i['main_subject']}. {i['visual_style']}. {i['details']}. {i['character_consistency']}"
        negative_prompt = str(i["negative_prompts"])
        
        logger.info(f"  [{idx}/{len(prompts)}] Generating: {i.get('title', file_name)[:50]}...")
        img = generate_image(prompt=image_prompt, negative_prompt=negative_prompt)

        img.save(rf"C:\Stack overflow\video_generation\Data\images\{file_name}.png", "PNG")
        logger.info(f"  [{idx}/{len(prompts)}] Saved: {file_name}.png")

        images_generated.append(img)

    logger.info(f"Generated {len(images_generated)} images total")
    log_step(logger, "Image Generation", "completed")
    return {
        "images": images_generated, 
        "image_generation_count": state.get("image_generation_count")+1,
        "images_to_eval": images_generated}