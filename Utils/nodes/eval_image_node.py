from Helpers.agents import Agents
from Utils.state import AgentState
from Utils.prompt_templates.eval_image_template import get_template
import base64, time
from io import BytesIO

agent_loader = Agents()
time.sleep(60)

def eval_generated_image(state: AgentState):
    image_prompt = state.get("image_prompt")
    images = state.get("images_to_eval")
    agent = agent_loader.get_eval_image()

    eval_image = []

    for i, img in enumerate(images):
        image_prompt_single = image_prompt[i]
        prompt = get_template(image_prompt_single)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")   

        response = agent.invoke({
        "messages": [
            {"role": "user", 
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": f"data:image/png;base64,{img_str}"}
            ]
        }]}) 

        result = {
            "image_number": image_prompt_single["image_number"],
            "is_approved": response["structured_response"].is_approved_image,
            "corrections": response["structured_response"].corrected_imageprompt
            }
        eval_image.append(result)

    regen_images = [i["image_number"] for i in eval_image if i["is_approved"] is False]

    return {"eval_image": eval_image, "images_to_regen": regen_images}
