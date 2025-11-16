from pydantic import Field, BaseModel
from typing import List

class singleWhiskFormat(BaseModel):
    scene_id:int = Field(description="Unique scene identifier matching the original scene number (1-30)")
    prompt:str = Field(description="Main visual description and subject matter for image generation. Describe what should be in the image clearly and concisely.")
    style:str = Field(description="Art/animation style (e.g., 'Pixar 3D animation', 'Disney style', 'Studio Ghibli', '2D cartoon', 'watercolor illustration'")
    lighting:str = Field(description="Lighting setup and conditions (e.g., 'warm golden hour', 'soft morning light', 'dramatic shadows', 'bright daylight', 'moonlit night')")
    color_palette:str = Field(description="Color scheme and tones (e.g., 'vibrant and saturated', 'warm earth tones', 'cool blues and purples', 'pastel colors', 'high contrast')")
    composition:str = Field(description="Image composition and framing (e.g., 'centered subject', 'rule of thirds', 'foreground focus with blurred background', 'symmetrical layout')")
    mood:str = Field(description="Emotional tone and atmosphere (e.g., 'cheerful and uplifting', 'peaceful and calm', 'tense and dramatic', 'whimsical and playful')")
    quality:str = Field(description="Quality and detail level (e.g., 'highly detailed', '8K resolution', 'professional quality', 'sharp focus', 'crisp details')")
    shot:str = Field(description="Camera shot type and angle (e.g., 'wide shot', 'close-up', 'medium shot', 'bird's eye view', 'low angle', 'over-the-shoulder')")
    no_text:bool = Field(default=True, description="Whether to exclude text/letters from the generated image. True = no text in image, False = allow text")

class whiskPromptsCollection(BaseModel):
    prompts:List[singleWhiskFormat] = Field(description="Collection of image generation prompts for all 30 scenes, formatted for Whisker AI or similar image generation APIs")