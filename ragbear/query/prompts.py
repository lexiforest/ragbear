from typing import List

RAG_PROMPT = """请根据用户提问和参考资料进行回复，回复的内容控制在100字左右。

用户提问：{}

参考材料：
{}"""



def format(p: str, question: str, docs: List[str]):
    return RAG_PROMPT.format(query, docs)
