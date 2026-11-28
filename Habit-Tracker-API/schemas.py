from pydantic import BaseModel, ConfigDict
from pydantic import BaseModel
from typing import Optional
from datetime import datetime 

class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: str


class HabitResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    frequency: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
    