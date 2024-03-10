from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_project_activities():
    return  # TODO


@router.post("/")
async def create_project_activities():
    return  # TODO


@router.delete("/")
async def delete_project_activities():
    return  # TODO
