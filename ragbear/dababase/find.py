from typing import List, Optional
from pydantic import BaseModel, AnyUrl, Url
from sentence_transformers import SentenceTransformer
from duckduckgo_search import DDGS

from ragbear.rank import noop_rank


model = SentenceTransformer("cyclone/simcse-chinese-roberta-wwm-ext")

model.encode(["hehe", ""])


class Doc(BaseModel):
    title: str = ""
    text: str = ""
    full_text: str = ""
    url: Optional[AnyUrl]= None
    source: str = ""
    source_type: str = ""
    time_used: int


def find(query: str, recall="bm25"):

    # 1. vectorize the query string
    vec = model.encode(str)

    # 2. find docs in the index
    docs = index.search(vec)

    return docs


def find_bm25(query: str):
    ...


def find_duckduckgo(query: str, max_results: int = 10) -> List[Doc]:
    results = DDGS().text(query, max_results=max_results)
    return docs

