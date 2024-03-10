from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_parent_consultations():
    return  # TODO


@router.post("/")
async def create_parent_consultations():
    return  # TODO


@router.delete("/")
async def delete_parent_consultations():
    return  # TODO
