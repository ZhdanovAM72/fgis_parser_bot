from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class ParserProjectBase(BaseModel):
    """Базовый класс парсера."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)


class ParserProjectCreate(ParserProjectBase):
    """Класс создания."""
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    applicability: bool = Field(...)

    @validator('name')
    def name_cant_be_null(cls, value: str):
        if value is None:
            raise ValueError('Имя СИ не может быть пустым!')
        return value


class ParserProjectUpdate(ParserProjectBase):
    """Класс обновления."""
    class Config:
        extra = 'allow'


class ParserProjectDB(ParserProjectBase):
    """Класс парсера в БД."""
    id: int
    applicability: bool = Field(False)
    parser_date: datetime = Field(
        # ..., example=datetime.now().isoformat(timespec='seconds')
        None, example=datetime.now()
    )

    class Config:
        orm_mode = True
        extra = 'allow'
