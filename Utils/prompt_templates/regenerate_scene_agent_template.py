from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes: List, correction: str) -> str:
    prompt = """Revise these scenes based on the evaluation feedback:

    Original Scenes:
    {scenes}

    Evaluation Feedback:
    {correction}

    Provide improved scenes that address all issues."""

    template = PromptTemplate.from_template(prompt).format(scenes=scenes, correction=correction)

    return template