from Helpers.agents import Agents
from Utils.state import AgentState
from Utils.image_inference.client import generate_image

agent_loader = Agents()

def image_regeneration_agent(state: AgentState):
    regen = state.get("images_to_regen")
    eval_images = state.get("eval_image")
    generation_count = state.get("image_generation_count")
    images_generated = []
    previous_images = state.get("images")

    for i in eval_images:
        if i["image_number"] in regen:
            file_name = f"image_number_{i['image_number']}.{generation_count+1}"
            image_prompt = f"{i['main_subject']}. {i['visual_style']}. {i['details']}. {i['character_consistency']}"
            niga = str(i["negative_prompts"])
            img = generate_image(prompt=image_prompt, negative_prompt=niga)

            print(f"Generated: {file_name}")
            img.save(rf"C:\Stack overflow\video_generation\Data\images\{file_name}.png", "PNG")

            previous_images[i["image_number"]-1] = img
            images_generated.append(img)
    
    
    return {"images": previous_images, "image_generation_count": state.get("image_generation_count")+1, "images_to_eval": images_generated}