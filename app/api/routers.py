from fastapi import APIRouter

from app.api.endpoints import (
    users_router, parser_router
)


main_router = APIRouter(prefix='/api')

main_router.include_router(
    parser_router,
    prefix='/parser_info',
    tags=['Parser Info'],
)


main_router.include_router(users_router)
