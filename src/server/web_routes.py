from fastapi.responses import FileResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/", response_class=FileResponse)
async def root():
    return FileResponse("build/index.html")


@router.get("/{full_path:path}", response_class=FileResponse)
async def other(full_path: str):
    if not full_path.startswith('api'):
        return FileResponse('build/index.html')
