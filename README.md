# 🐻 Ragbear

`ragbear`, short for RAG Bear, is an academic oriented RAG framework for building retrieval
enhanced applications.

## Why

[existing solutions are too heavy](link to reddit).

But RAG should be simple, as simple as the following lines of code:

```py
DEFAULT_PROMPT = """Please answer the question according to the references.

Question: {question}

References: {docs}
"""

question = "Has tiktok been banned in the US?"

docs = get_docs(question)

prompt = DEFAULT_PROMPT.format(question=question, "\n".join(docs))

completion = openai.chat.completion.create({..., prompt, ...})

print(completion.choices[0].message.content)
```

With `ragbear`, it's **even simpler**:

```py
ragbear.query("Has tiktok been banned in the US?")
```

But a lot fancier, too:

```py
ragbear.query(
    "Who is the father of Luke Skywalker?",
    model="http://localhost:8964",
    source=[
        {"data": "http://localhost:8888", "type": "meilisearch"},  # query a meilisearch database
    ],
    rerank="newest",
    rewrite="query2doc",
    template=template,
)
```

But you will need to optimize towards your academic or commercial goals, you need a framework.

Enter Ragbear, we follow the above pattern closely, but give you options to swap each parts
of the pipeline. The code is concise and straightforward, no useless wrappers around wrappers.
Just read it.

Unlike LangChain, we do not try to encapsulate every solution out there, because there is
actually not too much to wrap at all. We would like to call ragbear a patter, rather than
a framework.

## Implemented algorithms

With ragbear, we want to incorporate the latest research ideas and put it into production.
We have implemented the following algorithms, which you can easily apply in your app.

- HyDE
- REPLUG
- Query2Doc

For example, to use the REPLUG method, it's as easy as:

```py
import ragbear

ans = ragbear.query("Where was Steve Jobs born?", rewrite="replug")
```

## Data

We support the following data query backend

- DuckDuckGo, via python package `duckduckgo_search`
- Local Dataset, via ANN engines, aks vector databases
    - hnswlib + sqlite
    - faiss + sqlite
    - pg_vector

## Dependencies

- An LLM API endpoint, you can use OpenAI API or local models with Ollama.
- An data backend, use `duckduckgo_search` or local dataset.

## Citation

If you find this project useful, please cite it as below:

```
@software{Lyonnet2024,
  author = {Alex Lyonnet, Shang Yu},
  title = {RAGBear - various RAG methods implemented in one package},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/oysteroil/ragbear}},
}
```
