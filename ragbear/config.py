import yaml
from pathlib import Path
from typing import Literal, List


from pydantic import BaseModel


class Config(BaseModel):
    index_engine: Literal["hnswlib", "faiss", "annoy"]
    embedding_model: str
    query_rewrite: List[Literal["expand"]]


def read_config(p: str | Path):
    with open(p) as f:
        return yaml.safe_load(f)


