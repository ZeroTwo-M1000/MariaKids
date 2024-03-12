import os
import shutil
import uuid
from pathlib import Path

from fastapi import APIRouter
from fastapi import Depends
from fastapi import File, UploadFile
from fastapi import HTTPException

from api.LessonNotes.data_loader import LessonNotesDataLoader
from api.LessonNotes.models import GetLessonNotes, PostLessonNotes
from auth.auth import get_token

router = APIRouter()


@router.get("/")
async def read_lesson_notes():
    return [
        GetLessonNotes(**lesson_note.dict())
        for lesson_note in await LessonNotesDataLoader.get_lesson_notes()
    ]


@router.post("/")
async def create_lesson_notes(title: str, file: UploadFile = File(...), token: str = Depends(get_token)):
    name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    file_location = f"media/{name}"

    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await LessonNotesDataLoader.post_lesson_notes(
        PostLessonNotes(
            title=title,
            link=f"/media/{name}",
        )
    )

    return HTTPException(status_code=201)


@router.delete("/{id}")
async def delete_lesson_notes(id: str, token: str = Depends(get_token)):
    note = await LessonNotesDataLoader.delete_lesson_notes(id)

    if note is None:
        raise HTTPException(status_code=404)

    file = Path(f"media/{note.link.split('/')[-1]}")
    os.remove(file)

    return HTTPException(status_code=204)
