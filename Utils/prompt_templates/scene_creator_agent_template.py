from langchain_core.prompts import PromptTemplate

def get_scene_creator_prompt(script:str) -> str:
    prompt = """You are a script breakdown specialist. Convert the following script into scenes and give json prompt.
    
        For each scene, provide:
        - Scene number
        - Location
        - Time of day
        - Characters present
        - Brief description
        - Dialogue summary

        Script:
        {script}

        Format as a structured list of json prompts and give 30 scenes."""
    
    template = PromptTemplate.from_template(prompt).format(script=script)

    return template