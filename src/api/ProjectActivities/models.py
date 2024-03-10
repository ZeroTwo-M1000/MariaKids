from datetime import datetime

from pydantic import BaseModel


class GetProjectActivities(BaseModel):
    id: str
    title: str
    date: datetime
    link: str


class PostProjectActivities(BaseModel):
    title: str
    link: str
