from fastapi import APIRouter
from fastapi import Depends

from auth.auth import encode_token
from auth.auth import get_token
from auth.model import User

router = APIRouter()


@router.post("/login")
async def get_users(user: User):
    return encode_token(user.username)


@router.get("/isadmin")
async def get_is_admin(token: str = Depends(get_token)):
    return {"admin": True}
