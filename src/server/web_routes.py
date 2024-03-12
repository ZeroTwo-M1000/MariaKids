import os

from fastapi import HTTPException
from fastapi.responses import FileResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/media/{file_name:path}")
async def media(file_name: str):
    if file_name != "" and os.path.exists(f"media/{file_name}"):
        return FileResponse(
            f"media/{file_name}",
            media_type="application/octet-stream",
            filename=file_name,
        )
    raise HTTPException(status_code=404)


@router.get("/{full_path:path}")
async def other(full_path: str):
    if not full_path.startswith("api") and not full_path.startswith("media"):
        return FileResponse("build/index.html")
    raise HTTPException(status_code=404)
