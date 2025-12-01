from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List) -> str:
    rules = """
    Rules to check:
    1. Each scene must have a clear location
    2. Each scene must specify time of day
    3. Characters must be clearly identified
    4. Scene transitions must be logical
    5. Each scene should have a clear purpose
    """
    prompt = """You are a script supervisor. Evaluate these scenes against the rules.
    
    {rules}

    Scenes to evaluate:
    {scenes}

    Provide:
    1. PASS or FAIL for each rule
    2. Specific issues found
    3. Overall recommendation: APPROVED or NEEDS_REVISION
    4. Suggestions for improvement if needed"""

    template = PromptTemplate.from_template(prompt).format(rules=rules, scenes=scenes)

    return template