from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List) -> str:
    prompt = """You are an expert AI Art Director. Your goal is to translate a storyboard into a set of highly detailed, production-ready image generation prompts.
    
                **Input Scenes:**
                {scenes}

                **Task:**
                Create a detailed `ImagePromptModel` for EACH scene. The prompts must be optimized for high-quality diffusion models (like Midjourney, Stable Diffusion, or Flux).

                **Required Fields for Each Image:**

                1. **image_number**: (Integer) Matching the scene number.
                2. **title**: (String) Short, unique file name/title.
                3. **main_subject**: (String) The core subject + action.
                   - *Rule*: Start with the subject. Use active verbs.
                   - *Example*: "A weary firefighter resting on the bumper of the truck."

                4. **visual_style**: (String) The global art direction.
                   - *Critical*: This string MUST be consistent across ALL images to ensure the video looks cohesive.
                   - Define: Medium (e.g., "Cinematic 3D Render"), Lighting (e.g., "Volumetric morning light"), and Color Palette.
                   - *Example*: "Pixar-style 3D animation, vibrant colors, soft global illumination, high fidelity, 8k resolution."

                5. **details**: (List[str]) Specific visual elements to populate the frame.
                   - Include: Background elements, props, textures, weather effects.
                   - *Example*: ["puddles on the ground", "neon sign reflecting in water", "rust texture on metal", "dense fog"]

                6. **negative_prompts**: (List[str]) What to avoid.
                   - *Example*: ["blur", "distortion", "watermark", "text", "low resolution", "extra fingers", "mutated"]

                7. **character_consistency**: (Object)
                   - **identity_tags**: (List[str]) Physical traits that NEVER change (e.g., "red scarf", "scar on left cheek", "blue robot").
                   - **style_lock**: (String) A short trigger phrase to enforce style (e.g., "in the style of Anime").

                **Pro Tips for Better Images:**
                - Use camera terminology (e.g., "Low angle shot," "Close-up," "Wide establishing shot", "Depth of field").
                - Describe lighting explicitly (e.g., "Rim lighting," "Softbox lighting," "Sunset golden hour").
                - Keep the `visual_style` identical for every single prompt unless the scene dictates a flashback/dream.

                Return the output as a JSON array."""
    
    template = PromptTemplate.from_template(prompt).format(scenes=scenes)

    return template