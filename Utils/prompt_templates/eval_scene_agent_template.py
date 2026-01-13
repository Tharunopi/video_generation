from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List) -> str:
    rules = """
    Rules to check:
    1. **Visual Clarity**: Is the scene physically possible to draw/film? (Avoid abstract emotions like "He felt sad" without a visual cue).
    2. **Locations**: Are locations consistent? (e.g., if Scene 1 is "Kitchen", Scene 2 shouldn't randomly be "Mars" without transition).
    3. **Pacing**: Is the scene length appropriate? (Not too crammed, not too empty).
    4. **Character Continuity**: Are characters introduced before they appear?
    5. **Descriptions**: Are descriptions concise (under 2 sentences) and focus on action?
    """
    prompt = """You are a Storyboard Supervisor. Your job is to reject scenes that will fail in image generation.
    
    {rules}

    Scenes to evaluate:
    {scenes}

    Provide:
    1. PASS or FAIL for each rule.
    2. Specific scenes that violate the rules (quote them).
    3. Fix Suggestions: How to rewrite the description to be more visual.
    4. Overall recommendation: APPROVED or NEEDS_REVISION."""

    template = PromptTemplate.from_template(prompt).format(rules=rules, scenes=scenes)

    return template