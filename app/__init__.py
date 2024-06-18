from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.config import config
from app.services.database import sessionmanager
from app.rabbit import rabbit_router



def init_app(init_db=True):
    lifespan = None

    if init_db:
        sessionmanager.init(config.DB_CONFIG)

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            async with rabbit_router.lifespan_context(app):
                yield
                if sessionmanager._engine is not None:
                    await sessionmanager.close()

    server = FastAPI(title="FastAPI server", lifespan=lifespan)

    from app.views.user import user_router
    from app.views.login import user_router
    from app.views.model import model_router
    from app.views.images import image_router

    server.include_router(rabbit_router)
    server.include_router(user_router, prefix="/api", tags=["user"])
    server.include_router(model_router, prefix="/api", tags=["model"])
    server.include_router(image_router, prefix="/api", tags=["image"])
    return server
