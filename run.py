#!/usr/bin/env python3
from app import init_app
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
server = init_app()

server.mount("/assets", StaticFiles(directory="public/assets"), name="static")

@server.get("/favicon.png", response_class=FileResponse)
async def favicon_png():
    return FileResponse("public/favicon.png")

@server.get("/favicon.ico", response_class=FileResponse)
async def favicon_ico():
    return FileResponse("public/favicon.png")


server.mount('/', StaticFiles(directory='public', html=True))

