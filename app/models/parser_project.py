from sqlalchemy import Column, String, Text

from app.models.base import ParserBase


class ParserProject(ParserBase):
    """Модель проектов для пожествований."""
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
