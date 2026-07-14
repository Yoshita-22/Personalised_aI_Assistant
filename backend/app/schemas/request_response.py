from pydantic import BaseModel
from typing import Optional

class ConversationRequest(BaseModel):
    event_description: str
    user_interests: list[str]


class ConversationResponse(BaseModel):
    themes: list[str]
    conversation_starters: list[str]


class FactCheckRequest(BaseModel):
    input_text: str


class FactCheckResponse(BaseModel):
    verification_status: str
    summary: Optional[str] = None
class FeedbackRequest(BaseModel):
    suggestion:str
    action:str