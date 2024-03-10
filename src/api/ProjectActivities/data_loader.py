from api.ProjectActivities.models import PostProjectActivities
from config.connection import prisma_connection


class ProjectActivitiesDataLoader:

    @staticmethod
    async def get_project_activities():
        return await prisma_connection.prisma.projectactivities.find_many()

    @staticmethod
    async def get_project_activities_by_id(id: str):
        return await prisma_connection.prisma.projectactivities.find_unique(
            where={
                "id": id
            },
        )

    @staticmethod
    async def post_project_activities(note: PostProjectActivities):
        return await prisma_connection.prisma.projectactivities.create(
            data=note.model_dump()
        )

    @staticmethod
    async def delete_project_activities(id: str):
        return await prisma_connection.prisma.projectactivities.delete(
            where={
                "id": id
            },
        )
