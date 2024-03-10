from datetime import datetime

from pydantic import BaseModel


class GetChildrenArtworks(BaseModel):
    id: str
    date: datetime
    link: str


class PostChildrenArtworks(BaseModel):
    link: str
