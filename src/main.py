from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config.connection import prisma_connection
from server import web_routes


def init_app():
    app = FastAPI(title="MariaSite")

    app.mount("/assets", StaticFiles(directory="build/assets"), name="static")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    async def on_startup():
        await prisma_connection.connect()

    async def on_shutdown():
        await prisma_connection.disconnect()

    app.include_router(web_routes.router, tags=["Web"])

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    return app


app = init_app()
