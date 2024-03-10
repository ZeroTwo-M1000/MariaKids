from datetime import datetime

from pydantic import BaseModel


class GetLessonNotes(BaseModel):
    id: str
    title: str
    date: datetime
    link: str


class PostLessonNotes(BaseModel):
    title: str
    link: str
