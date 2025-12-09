from pydantic import BaseModel, Field
from typing import List

class Scenes(BaseModel):
    scene_number: int = Field(description="A simple numeric label used to keep the sequence organized.")
    location: str = Field(description="A short note describing where the scene takes place — could be indoor, outdoor, real place, fictional place, or a general setting.Example: “Inside a small office,” “Busy marketplace,” “Temple courtyard,” “Rural farmland,” etc.")
    time_of_the_day: str = Field(description="Specifies the lighting and mood. Example: “Early morning,” “Sunset,” “Nighttime,” “Midday,” etc.")
    characters_present: str = Field(description="A list of all people (or entities) appearing in the scene. Example: “Main character only,” “Thiruvalluvar,” “Two farmers,” “Student and teacher,” etc.")
    brief_description: str = Field(description="A 1–2 sentence overview of what’s visually happening. Example: “The character walks into the room, observing the surroundings,” or “A peaceful sunrise washes over the village.”")
    dialogue_summary:str = Field(description="A quick line describing what is spoken or conveyed. Example: “The character explains the core idea,” or “Thiruvalluvar delivers a short line about wisdom.”")

class listScenes(BaseModel):
    scenes:List[Scenes] = Field(description="A collection of scene objects, each containing structured details such as scene number, location, time of day, characters, brief description, and dialogue summary. This list represents the full storyboard or sequence of scenes for the video or narrative.")

class evalReportScenes(BaseModel):
    is_approved_scenes: bool = Field(description="Boolean value used to define whether the scenes are approved or not")
    correction: str = Field(description="Contains the feedback to improve scenes.")

class evalReportImagePrompt(BaseModel):
    is_approved_image_prompt: bool = Field(description="Boolean value used to define whether the scenes are approved or not")
    correction: str = Field(description="Contains the feedback to improve scenes.")

class evalReportImage(BaseModel):
    is_approved_image: bool = Field(description="Boolean value used to define whether the image are approved or not")
    corrected_imageprompt: str = Field(description="Contains corrected image prompt if image is not approved.")

class characterConsistenyModel(BaseModel):
    identity_tags: List[str] = Field(description="Short factual phrases that describe persistent character attributes (face marks, hair style, clothing details). Use concise, repeatable tags.")
    style_lock: str = Field(description="Short instruction to lock or strongly prefer the same overall art style across outputs (e.g., painterly warm-tone).")

class imagePrompts(BaseModel):
    image_number: int = Field(description="A simple numeric label used to keep the sequence organized.")
    title: str = Field(description="Short human-readable title for quick identification in UIs and logs. Keep it concise (<= 60 chars).")
    main_subject: str = Field(description="Clear, factual one-line description of the primary subject (who/what). Focus on identity and action rather than style.")
    visual_style: str = Field(description="High-level art direction: medium, camera lens, lighting, mood, and stylistic adjectives. Keeps the overall look consistent across generations.")
    details: List[str] = Field(description="List of short, specific attributes to enforce appearance and environment (appearance, clothing, props, background constraints). Each item should be a concise noun-phrase.")
    negative_prompts: List[str] = Field(description="List of terms/concepts to avoid (artifacts, unwanted objects, quality issues). Use specific items such as 'text', 'watermark', 'extra limbs', 'deformed hands'.")
    character_consistency: characterConsistenyModel = Field(description="hints to preserve the same character across multiple generations")

class imagePromptList(BaseModel):
    image_prompt: List[imagePrompts] = Field(description="List of all image prompts for the scenes")