from api.LessonNotes.crud import router as lesson_notes_router
from api.ParentConsultations.crud import router as parent_consultations_router
from api.ProjectActivities.crud import router as project_activities_router
from config.connection import prisma_connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
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

    app.include_router(lesson_notes_router, tags=["Lesson Notes"], prefix="/api/lesson-notes")
    app.include_router(parent_consultations_router, tags=["Parent Consultations"], prefix="/api/parent-consultations")
    app.include_router(project_activities_router, tags=["Project Activities"], prefix="/api/project-activities")
    app.include_router(web_routes.router, tags=["Web"])

    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    return app


app = init_app()
