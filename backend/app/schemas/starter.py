from pydantic import BaseModel
from datetime import datetime

class GeneratedStarterBase(BaseModel):
    starter_text: str
    prompt_used: str

class GeneratedStarterCreate(GeneratedStarterBase):
    session_id: int

class GeneratedStarter(GeneratedStarterCreate):
    starter_id: int
    generated_at: datetime

    class Config:
        from_attributes = True