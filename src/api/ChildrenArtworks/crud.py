import os
import shutil
import uuid
from pathlib import Path

from api.ChildrenArtworks.data_loader import ChildrenArtworksDataLoader
from api.ChildrenArtworks.models import GetChildrenArtworks, PostChildrenArtworks
from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi import HTTPException

router = APIRouter()


@router.get("/")
async def read_children_artworks():
    return [
        GetChildrenArtworks(**lesson_note.dict())
        for lesson_note in await ChildrenArtworksDataLoader.get_children_artworks()
    ]


@router.post("/")
async def create_children_artworks(file: UploadFile = File(...)):
    name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    file_location = f"media/{name}"

    with open(file_location, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    await ChildrenArtworksDataLoader.post_children_artworks(
        PostChildrenArtworks(
            link=f"/media/{name}",
        )
    )

    return HTTPException(status_code=201)


@router.delete("/{id}")
async def delete_children_artworks(id: str):
    note = await ChildrenArtworksDataLoader.delete_children_artworks(id)

    if note is None:
        raise HTTPException(status_code=404)

    file = Path(f"media/{note.link.split('/')[-1]}")
    os.remove(file)

    return HTTPException(status_code=204)
