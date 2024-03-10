from api.ParentConsultations.models import PostParentConsultations
from config.connection import prisma_connection


class ParentConsultationsDataLoader:

    @staticmethod
    async def get_parent_consultations():
        return await prisma_connection.prisma.parentconsultations.find_many()

    @staticmethod
    async def get_parent_consultations_by_id(id: str):
        return await prisma_connection.prisma.parentconsultations.find_unique(
            where={"id": id},
        )

    @staticmethod
    async def post_parent_consultations(note: PostParentConsultations):
        return await prisma_connection.prisma.parentconsultations.create(
            data=note.model_dump()
        )

    @staticmethod
    async def delete_parent_consultations(id: str):
        return await prisma_connection.prisma.parentconsultations.delete(
            where={"id": id},
        )
