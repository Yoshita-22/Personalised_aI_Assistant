from pydantic import BaseModel
from datetime import datetime

class NetworkingSessionBase(BaseModel):
    user_id: int

class NetworkingSessionCreate(NetworkingSessionBase):
    pass

class NetworkingSession(NetworkingSessionBase):
    session_id: int
    session_timestamp: datetime

    class Config:
        from_attributes = True