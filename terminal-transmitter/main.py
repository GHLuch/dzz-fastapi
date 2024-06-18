import uvicorn

from core.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "core.app:app",
        host=settings.SERVER_HOST if settings.SERVER_HOST else "localhost",
        port=int(settings.SERVER_PORT) if settings.SERVER_PORT else 5321,
        root_path=settings.ROOT_PATH if settings.ROOT_PATH else '',
        reload=True,
    )
