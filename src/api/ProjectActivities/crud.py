import os
import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File, UploadFile
from fastapi import HTTPException

from api.ProjectActivities.data_loader import ProjectActivitiesDataLoader
from api.ProjectActivities.models import GetProjectActivities, PostProjectActivities
from auth.auth import get_token

router = APIRouter()


@router.get("/")
async def read_project_activities():
    return [
        GetProjectActivities(**lesson_note.dict())
        for lesson_note in await ProjectActivitiesDataLoader.get_project_activities()
    ]


@router.post("/")
async def create_project_activities(title: str, file: UploadFile = File(...), token: str = Depends(get_token)):
    name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    file_location = f"media/{name}"

    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await ProjectActivitiesDataLoader.post_project_activities(
        PostProjectActivities(
            title=title,
            link=f"/media/{name}",
        )
    )

    return HTTPException(status_code=201)


@router.delete("/{id}")
async def delete_project_activities(id: str, token: str = Depends(get_token)):
    note = await ProjectActivitiesDataLoader.delete_project_activities(id)

    if note is None:
        raise HTTPException(status_code=404)

    file = Path(f"media/{note.link.split('/')[-1]}")
    os.remove(file)

    return HTTPException(status_code=204)
