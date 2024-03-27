from datetime import datetime

from sqlalchemy import Column, DateTime, Boolean

from app.core.db import Base


class ParserBase(Base):
    __abstract__ = True

    applicability = Column(Boolean, default=False)
    parse_date = Column(DateTime, default=datetime.now)
