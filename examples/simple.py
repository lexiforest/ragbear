import ragbear


ragbear.query("Did Steve Jobs receive a PhD degree?")
# -> No. He did not receive a PhD degree.


# Use duckduckgo as the data source
prompt = "Did Steve Jobs receive a PhD degree?"
ragbear.query(prompt, source="duckduckgo")


# Use another model, you can use any openai compatible API endpoints
ragbear.query(prompt, model="http://localhost:8964")
ragbear.query(prompt, model="http://localhost:8964", openai_token="xxxxxx")


# Use a local datasource, you need to ingest the data first, see ingest.md for details
ragbear.query(
    prompt,
    source=[
        {"data": "/tmp/data/wiki.hnsw", "type": "hnsw", "max_results": 10},  # query local hnsw indexed files
        {"data": "/tmp/data/wiki.bm25", "type": "bm25", "max_results": 10},  # query local bm25 indexed files
        {"data": "http://localhost:8888", "type": "meilisearch", "max_results": 10},  # query a meilisearch database
    ]
)


# Rerank the documents before generation
ragbear.query(prompt, rerank="similarity")
ragbear.query(prompt, rerank="oldest")
ragbear.query(prompt, rerank="newest")


# Rewrite the prompt before querying
ragbear.query(prompt, rewrite="query2doc")


# Use a different template for generation
template = """
You are a helpful assistant, answer the following question with the references:

Question: {question}
References: {refs}
"""
ragbear.query(prompt, template=template)


# Putting it all together
ragbear.query(
    "Who is the father of Luke Skywalker?",
    model="http://localhost:8964",
    source=[
        {"data": "http://localhost:8888", "type": "meilisearch", "max_results": 10},  # query a meilisearch database
    ],
    rerank="newest",
    rewrite="query2doc",
    template=template,
)
