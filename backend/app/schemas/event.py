from pydantic import BaseModel

class EventContextBase(BaseModel):
    event_description: str
    user_interests: list[str]
    analyzed_themes: list[str] = []

class EventContextCreate(EventContextBase):
    session_id: int

class EventContext(EventContextCreate):
    event_id: int

    class Config:
        from_attributes = True