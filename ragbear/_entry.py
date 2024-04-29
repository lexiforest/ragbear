from contextlib import suppress
from typing import List, Literal, Optional, TypedDict, Union
from .query.prompts import format_query
from .model import get_openai_client
from .database.remote.duckduckgo import get_duckduckgo_results


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
    *,
    model: str = "llama2",
    base_url: str = "http://localhost:11434/v1/",
    api_key: Optional[str] = "ollama",
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
        source: The data source for retrieval
    """
    # 1. find relevant docs
    docs = get_duckduckgo_results(prompt)
    docs = [d["body"] for d in docs]

    # 2. preprocess the query
    query = format_query(question=prompt, docs=docs)

    # 3. query the LLM
    client = get_openai_client(base_url, api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': query,
            }
        ],
        model=model,
    )
    # print(chat_completion)

    return chat_completion.choices[0].message.content
