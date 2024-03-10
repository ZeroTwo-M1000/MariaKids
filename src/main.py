from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config.connection import prisma_connection


def init_app():
    app = FastAPI(title="Inventix API")

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

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    return app
