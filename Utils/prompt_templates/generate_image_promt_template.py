from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List) -> str:
    prompt = """You are an expert at creating structured image generation prompts for AI image models.

                Given the following scene breakdown, create a detailed image prompt for EACH scene following this exact structure:

                Scenes:
                {scenes}

                For each scene, you must create an ImagePromptModel with these fields:

                1. **image_number**: Sequential number (1, 2, 3...)

                2. **title**: Short descriptive title (<= 60 chars)
                - Example: "Sarah Working Alone at Coffee Shop"

                3. **main_subject**: One clear sentence describing who/what and their action
                - Focus on IDENTITY and ACTION, not style
                - Example: "Young woman typing intensely on laptop at corner table"

                4. **visual_style**: Art direction combining medium, camera, lighting, mood
                - Include: medium type (photo-realistic, cinematic, etc.)
                - Camera details: lens type, angle, shot composition
                - Lighting: quality, direction, time of day
                - Mood: emotional tone, color palette
                - Example: "Cinematic photo-realistic, 35mm film, medium shot from slight overhead angle, soft morning sunlight streaming through windows, warm golden hour lighting, amber and cream color palette, shallow depth of field, moody and tense atmosphere"

                5. **details**: List of specific visual attributes (5-10 items)
                - Character appearance details
                - Clothing descriptions
                - Props and objects
                - Environment/background specifics
                - Spatial relationships
                - Example: ["casual business attire", "laptop with glowing screen", "wooden table surface", "coffee cup nearby", "large windows in background", "urban coffee shop interior", "morning sunlight rays", "blurred background with cafe customers"]

                6. **negative_prompts**: List of things to avoid (5-10 items)
                - Common AI artifacts
                - Quality issues
                - Unwanted elements
                - Example: ["text", "watermark", "blurry", "low quality", "deformed hands", "extra limbs", "distorted face", "unrealistic proportions", "oversaturated", "anime style"]

                7. **character_consistency**: Object with two sub-fields:
                
                a. **identity_tags**: List of persistent character attributes (3-7 tags)
                    - Physical features that stay consistent
                    - Clothing style markers
                    - Distinctive characteristics
                    - Example: ["shoulder-length brown hair", "green eyes", "slim build", "navy blazer", "silver necklace", "focused expression"]
                
                b. **style_lock**: One instruction for consistent art style
                    - Locks the overall visual treatment
                    - Example: "cinematic photo-realistic with warm natural lighting and film grain"

                IMPORTANT GUIDELINES:
                - Keep identity_tags factual and repeatable across scenes
                - Make main_subject action-focused, not style-focused
                - visual_style should be consistent across all scenes for the same project
                - details should be specific noun-phrases, not full sentences
                - negative_prompts should target common AI generation issues
                - character_consistency helps maintain same character appearance across multiple images

                Return the data as a JSON array of image prompt objects."""
    
    template = PromptTemplate.from_template(prompt).format(scenes=scenes)

    return template