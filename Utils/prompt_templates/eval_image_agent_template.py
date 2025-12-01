from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List, image_prompt: list) -> str:
    prompt = """You are evaluating structured image generation prompts against original scenes.

    Original Scenes:
    {scenes}

    Generated image prompt:
    {image_prompt}

    Evaluate EACH image prompt based on these criteria:

    **STRUCTURE VALIDATION:**
    1. ✓ All required fields present? (image_number, title, main_subject, visual_style, details, negative_prompts, character_consistency)
    2. ✓ Title <= 60 characters?
    3. ✓ details list has 5-10 items?
    4. ✓ negative_prompts list has 5-10 items?
    5. ✓ identity_tags has 3-7 items?
    6. ✓ style_lock is a single clear instruction?

    **CONTENT ACCURACY:**
    7. ✓ image_number sequential and correct?
    8. ✓ main_subject matches scene action and characters?
    9. ✓ visual_style includes time of day from scene?
    10. ✓ details include all key characters mentioned in scene?
    11. ✓ details include location-specific elements (INT/EXT)?

    **QUALITY CHECKS:**
    12. ✓ main_subject is factual and action-focused (not style-focused)?
    13. ✓ visual_style is comprehensive (medium, camera, lighting, mood)?
    14. ✓ details are concise noun-phrases?
    15. ✓ identity_tags are consistent and repeatable?
    16. ✓ negative_prompts target common AI issues?
    17. ✓ character_consistency preserves character across scenes?

    **CONSISTENCY CHECKS:**
    18. ✓ visual_style consistent across all scenes?
    19. ✓ style_lock same for all scenes in project?
    20. ✓ identity_tags for same character consistent across scenes?
    
    Provide:
    1. PASS or FAIL for each rule
    2. Specific issues found
    3. Overall recommendation: APPROVED or NEEDS_REVISION
    4. Suggestions for improvement if needed"""

    template = PromptTemplate.from_template(prompt).format(scenes=scenes, image_prompt=image_prompt)

    return template