from typing import Optional

from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Title'
    description: str = 'Description'
    version: str = '0.1.0'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    token_lifetime: int = 3600

    class Config:
        env_file = '.env'


settings = Settings()
