from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    email: EmailStr
    password_hash: Optional[str] = None
    provider: str = "local"
    social_id: Optional[str] = None
    nickname: str
    profile_image_url: Optional[str] = None
    bio: Optional[str] = None


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    email: EmailStr
    provider: str
    social_id: Optional[str]
    nickname: str
    profile_image_url: Optional[str]
    bio: Optional[str]
    is_portfolio_public: bool
    is_2fa_enabled: bool
    is_active: bool
    last_login_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    subscription_tier: str
    subscription_expires_at: Optional[datetime]
    theme_preference: str
    timezone: str
