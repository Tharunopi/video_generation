from langchain_core.prompts import PromptTemplate

def get_scene_creator_prompt(script:str) -> str:
    prompt = """You are an expert Script-to-Storyboard Specialist. Your task is to break down the provided text script into a sequence of distinct, visually descriptive scenes suitable for video generation.

    Input Script:
    {script}

    Instructions:
    1. **Analyze the Script**: Understand the flow, characters, and key message.
    2. **Break into Scenes**: Divide the script into logical visual segments. Create as many scenes as necessary to tell the story smoothly (typically 1 scene per 1-2 sentences of narration).
    3. **Visual Focus**: For each scene, focus heavily on *what we see*. Describe the action, setting, and character emotions vividly.
    4. **Consistency**: Ensure character names and locations remain consistent throughout.

    For each scene, you must provide:
    - **Scene Number**: Sequential integer.
    - **Location**: Specific setting (e.g., "Kitchen - Morning", "Park - Sunny").
    - **Time of Day**: "Morning", "Afternoon", "Night", etc.
    - **Characters Present**: List of characters in this specific shot.
    - **Brief Description**: 1-2 sentences describing the visual action. *Critical for image generation.*
    - **Dialogue Summary**: What is being said (or "Narration" if voiceover).

    Output the result as a structured list of JSON objects matching the required schema."""
    
    template = PromptTemplate.from_template(prompt).format(script=script)

    return template