from pydantic import BaseModel, Field
from typing import Optional

class sceneContext(BaseModel):
    script:str = Field(description="The input script to convert into scenes")
    target_audience_age:Optional[str] = Field(default="5-9", description="Target age group (e.g., '5-8', '9-12')")
    # theme:Optional[str] = Field(default="space", description="Primary theme (Unicorns, Circus, Superheroes, Mermaids, etc..)")
    # tone:Optional[str] = Field(default="warm and uplifting", description="Overall tone of the scenes")
    # total_duration_minutes:Optional[int] = Field(default=5, description="Target total duration in minutes")
    # visual_style:Optional[str] = Field(default="colourfull and bright", description="Visual style preference")