import uuid

from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, String, UniqueConstraint
from sqlalchemy.sql import func

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=True)

    provider = Column(String(20), default="local", nullable=False)
    social_id = Column(String(255), nullable=True)

    nickname = Column(String(50), unique=True, nullable=False)
    profile_image_url = Column(String(255), nullable=True)
    bio = Column(String(150), nullable=True)
    is_portfolio_public = Column(Boolean, default=True, nullable=False)

    is_2fa_enabled = Column(Boolean, default=False, nullable=False)
    two_factor_secret = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    last_login_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    subscription_tier = Column(String(20), default="FREE", nullable=False)
    subscription_expires_at = Column(DateTime, nullable=True)
    theme_preference = Column(String(10), default="DARK", nullable=False)
    timezone = Column(String(50), default="Asia/Seoul", nullable=False)

    __table_args__ = (
        UniqueConstraint("provider", "social_id", name="uq_users_provider_social_id"),
        CheckConstraint(
            "provider != 'local' OR password_hash IS NOT NULL",
            name="ck_users_local_requires_password",
        ),
    )
