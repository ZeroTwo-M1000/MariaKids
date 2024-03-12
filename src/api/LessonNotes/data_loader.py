from api.LessonNotes.models import PostLessonNotes
from config.connection import prisma_connection


class LessonNotesDataLoader:

    @staticmethod
    async def get_lesson_notes():
        return await prisma_connection.prisma.lessonnotes.find_many(
            order={"date": "desc"},
        )

    @staticmethod
    async def get_lesson_notes_by_id(id: str):
        return await prisma_connection.prisma.lessonnotes.find_unique(
            where={"id": id},
        )

    @staticmethod
    async def post_lesson_notes(note: PostLessonNotes):
        return await prisma_connection.prisma.lessonnotes.create(data=note.model_dump())

    @staticmethod
    async def delete_lesson_notes(id: str):
        return await prisma_connection.prisma.lessonnotes.delete(
            where={"id": id},
        )
