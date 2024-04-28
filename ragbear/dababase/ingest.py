import torch
from .index.hnsw import Index


def vectorize(s: str) -> torch.Tensor:
    ...


def ingest(p: str, embedding_model: str = ""):
    index = Index()
    for doc in docs:
        index.add(doc)

