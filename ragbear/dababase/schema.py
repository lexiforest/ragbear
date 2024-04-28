from pydantic import BaseModel


class Chunk(BaseModel):
    id: int
    text: str
    article_id: int


class Article(BaseModel):
    id: int
    text: str
    url: str
