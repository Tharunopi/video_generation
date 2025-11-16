from pydantic import Field, BaseModel
from typing import List, Optional

class scene(BaseModel):
    scene_id:int = Field(description="Unique identifier for the scene")
    title:str = Field(description="Brief title of the scene")
    summary:str = Field(description="Short summary of what happens")
    visual_description:str = Field(description="Detailed visual description")
    emotion:str = Field(description="Primary emotion of the scene")
    camera_direction:str = Field(description="Camera angle and movement")
    dialogue:Optional[str] = Field(default=None, description="Dialogue or narration in the scene")
    duration_seconds:int = Field(default=5, description="Duration in seconds")

class sceneCollection(BaseModel):
    scenes:List[scene] = Field(description="List of exactly 30 cinematic scenes")