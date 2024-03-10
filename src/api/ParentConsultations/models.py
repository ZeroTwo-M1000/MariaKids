from datetime import datetime

from pydantic import BaseModel


class GetParentConsultations(BaseModel):
    id: str
    title: str
    date: datetime
    link: str


class PostParentConsultations(BaseModel):
    title: str
    link: str
