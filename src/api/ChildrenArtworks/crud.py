from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_children_artworks():
    return  # TODO


@router.post("/")
async def create_children_artworks():
    return  # TODO


@router.delete("/")
async def delete_children_artworks():
    return  # TODO
