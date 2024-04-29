from duckduckgo_search import DDGS





def get_duckduckgo_results(query: str, max_results: int = 10):
    results = DDGS().text(query, max_results=max_results)
    return results

