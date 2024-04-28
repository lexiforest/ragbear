from contextlib import suppress
from typing import List, Literal, Optional, TypedDict, Union

with suppress(ImportError):
    pass


class SourceVendorType(TypedDict):
    data: str
    type: str
    max_results: Optional[int]


SourceType = Union[Literal["duckduckgo"], List[SourceVendorType]]
RerankType = Literal["similarity", "oldest", "newest"]
RewriteType = Literal["query2doc"]


def query(
    prompt: str,
    model: Optional[str] = None,
    *,
    openai_token: Optional[str] = None,
    source: Optional[SourceType] = None,
    rerank: Optional[RerankType] = None,
    rewrite: Optional[RewriteType] = None,
    template: Optional[str] = None,
    embedding_model: Optional[str] = None
):
    """Query the LLM, and return the summarized result.

    Args:
        prompt: the query string
        model: the model to use, by default use local ollama server.
        source: The data source for retrival

    """

    # 1. preprocess the query

    # 2. find relevant docs

    # 3. query the LLM

    return
