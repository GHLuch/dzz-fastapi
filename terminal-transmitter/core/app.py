from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from core.settings import settings
from src.transport import rabbit_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with rabbit_router.lifespan_context(_app):
        yield

app = FastAPI(title="Terminal transmitter", version=settings.VERSION, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(rabbit_router)
