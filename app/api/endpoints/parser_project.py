from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
# from app.core.user import current_superuser
from app.schemas.parser_project import (
    ParserProjectDB,
)
from app.crud.charity_project import parser_project_crud

router = APIRouter()


@router.get(
    '/',
    response_model_exclude_none=True,
    response_model=list[ParserProjectDB],
)
async def get_charity_projects(
    session: AsyncSession = Depends(get_async_session),
):
    return await parser_project_crud.get_multi(session)
