from fastapi import FastAPI
import uvicorn

from app.api.routers import main_router
from app.core.config import settings
from app.core.init_db import create_first_superuser

app = FastAPI(
    title=settings.app_title,
    description=settings.description,
    version=settings.version,
    docs_url="/api/swagger",
    redoc_url="/api/redoc",
)

app.include_router(main_router)


@app.on_event('startup')
async def startup():
    await create_first_superuser()


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
