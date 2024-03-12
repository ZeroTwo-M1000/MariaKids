import os
import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File, UploadFile
from fastapi import HTTPException

from api.ParentConsultations.data_loader import ParentConsultationsDataLoader
from api.ParentConsultations.models import (
    GetParentConsultations,
    PostParentConsultations,
)
from auth.auth import get_token

router = APIRouter()


@router.get("/")
async def read_parent_consultations():
    return [
        GetParentConsultations(**lesson_note.dict())
        for lesson_note in await ParentConsultationsDataLoader.get_parent_consultations()
    ]


@router.post("/")
async def create_parent_consultations(title: str, file: UploadFile = File(...), token: str = Depends(get_token)):
    name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    file_location = f"media/{name}"

    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await ParentConsultationsDataLoader.post_parent_consultations(
        PostParentConsultations(
            title=title,
            link=f"/media/{name}",
        )
    )

    return HTTPException(status_code=201)


@router.delete("/{id}")
async def delete_parent_consultations(id: str, token: str = Depends(get_token)):
    note = await ParentConsultationsDataLoader.delete_parent_consultations(id)

    if note is None:
        raise HTTPException(status_code=404)

    file = Path(f"media/{note.link.split('/')[-1]}")
    os.remove(file)

    return HTTPException(status_code=204)
