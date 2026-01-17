from Helpers.agents import Agents
from Utils.state import AgentState
from Utils.prompt_templates.eval_image_template import get_template
from Utils.logger import get_logger, log_step
import base64, time
from io import BytesIO

logger = get_logger(__name__)
agent_loader = Agents()

def eval_generated_image(state: AgentState):
    log_step(logger, "Image Evaluation", "started")
    image_prompt = state.get("image_prompt")
    images = state.get("images_to_eval")
    agent = agent_loader.get_eval_image()
    
    logger.info(f"Evaluating {len(images)} generated images...")
    logger.info("Waiting 60s for rate limit cooldown...")
    time.sleep(60)

    eval_image = []

    for i, img in enumerate(images):
        image_prompt_single = image_prompt[i]
        prompt = get_template(image_prompt_single)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")   
        
        logger.info(f"  [{i+1}/{len(images)}] Evaluating image {image_prompt_single.get('image_number', i+1)}...")

        response = agent.invoke({
        "messages": [
            {"role": "user", 
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{img_str}"}
            ]
        }]}) 

        is_approved = response["structured_response"].is_approved_image
        result = {
            "image_number": image_prompt_single["image_number"],
            "is_approved": is_approved,
            "corrections": response["structured_response"].corrected_imageprompt
            }
        
        status = "PASS" if is_approved else "FAIL"
        logger.info(f"  [{i+1}/{len(images)}] {status}")
        eval_image.append(result)

    regen_images = [i["image_number"] for i in eval_image if i["is_approved"] is False]
    
    passed = len(eval_image) - len(regen_images)
    logger.info(f"Results: {passed}/{len(eval_image)} images passed")
    if regen_images:
        logger.warning(f"Images needing regeneration: {regen_images}")
    
    log_step(logger, "Image Evaluation", "completed")
    return {"eval_image": eval_image, "images_to_regen": regen_images}
