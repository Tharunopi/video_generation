from pydantic import BaseModel, Field
from typing import Optional

class whiskContext(BaseModel):
    script:str = Field(description="The input script to convert into scenes")
    target_audience_age:Optional[str] = Field(default="5-9", description="Target age group (e.g., '5-8', '9-12')")