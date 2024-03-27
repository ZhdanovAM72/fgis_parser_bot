from typing import Optional
from sqlalchemy import select, func, asc
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.parser_project import ParserProject


class CRUDParserProject(CRUDBase):
    """CRUD класс парсера."""
    async def get_charity_project_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        charity_project_id = await session.execute(
            select(ParserProject.id).where(
                ParserProject.name == project_name
            )
        )
        charity_project_id = charity_project_id.scalars().first()
        return charity_project_id

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[ParserProject]:
        parser_projects = await session.execute(
            select(ParserProject).where(
                ParserProject.fully_invested
            ).order_by(asc(func.julianday(ParserProject.close_date) -
                           func.julianday(ParserProject.create_date)))
        )
        parser_projects = parser_projects.scalars().all()
        print(parser_projects)
        return parser_projects


parser_project_crud = CRUDParserProject(ParserProject)
