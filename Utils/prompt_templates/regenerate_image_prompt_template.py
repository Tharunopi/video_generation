from langchain_core.prompts import PromptTemplate
from typing import List

def get_template(scenes:List, image_prompt:list, corrections:str) -> str:
    prompt = """Revise these image prompt based on the evaluation feedback:

    Original Scenes:
    {scenes}

    generated image prompt:
    {image_prompt}

    evaluation feedback:
    {corrections}

    Provide improved image prompt that address all issues.""" 

    template = PromptTemplate.from_template(prompt).format(scenes=scenes, image_prompt=image_prompt, corrections=corrections)

    return template