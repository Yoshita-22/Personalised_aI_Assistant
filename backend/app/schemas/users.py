from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserProfileBase(BaseModel):
    name: str
    bio: str

class UserProfileCreate(UserProfileBase):
    pass

class UserProfile(UserProfileBase):
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True