from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LogEntryBase(BaseModel):
    action_type: str
    payload_json: Optional[dict] = None

class LogEntryCreate(LogEntryBase):
    session_id: int

class LogEntry(LogEntryCreate):
    log_id: int
    timestamp: datetime

    class Config:
        from_attributes = True