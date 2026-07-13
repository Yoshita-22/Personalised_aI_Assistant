from pydantic import BaseModel
from datetime import datetime

class FactCheckBase(BaseModel):
    input_text: str

class FactCheckCreate(FactCheckBase):
    session_id: int

class FactCheck(FactCheckCreate):
    fact_check_id: int
    checked_at: datetime

    class Config:
        from_attributes = True