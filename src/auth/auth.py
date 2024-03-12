from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from starlette import status

get_bearer_token = HTTPBearer(auto_error=False)

user_admin = {
    "name": "maria",
    "password": "mariaadmin",
}


def decode_token(token: str) -> dict:
    return jwt.decode(token, key="hfgkkfjgjhfg4356grthnyge5", algorithms=["HS256"])


async def get_token(auth: Optional[HTTPAuthorizationCredentials] = Depends(get_bearer_token)):
    if auth is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    try:
        name = decode_token(auth.credentials)["name"]

        if name != user_admin["name"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )

    return auth.credentials


def encode_token(name: str):
    if name != user_admin["name"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
    return jwt.encode({"name": name}, key="hfgkkfjgjhfg4356grthnyge5", algorithm="HS256")
