from api.ChildrenArtworks.models import PostChildrenArtworks
from config.connection import prisma_connection


class ChildrenArtworksDataLoader:

    @staticmethod
    async def get_children_artworks():
        return await prisma_connection.prisma.childrenartworks.find_many()

    @staticmethod
    async def get_children_artworks_by_id(id: str):
        return await prisma_connection.prisma.childrenartworks.find_unique(
            where={
                "id": id
            },
        )

    @staticmethod
    async def post_children_artworks(note: PostChildrenArtworks):
        return await prisma_connection.prisma.childrenartworks.create(
            data=note.model_dump()
        )

    @staticmethod
    async def delete_children_artworks(id: str):
        return await prisma_connection.prisma.childrenartworks.delete(
            where={
                "id": id
            },
        )
