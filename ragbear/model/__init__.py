from openai import OpenAI


def get_openai_client(base_url, api_key) -> OpenAI:
    client = OpenAI(base_url=base_url, api_key=api_key)
    return client
