from typing import List

DEFAULT_PROMPT_ZH = """请根据用户提问和参考资料进行回复，回复的内容控制在100字左右。

用户提问：{}

参考材料：
{}"""

DEFAULT_PROMPT = """Please answer the question according to the references.

Question: {question}

References: {docs}
"""


def format_query(question: str, docs: List[str]):
    return DEFAULT_PROMPT.format(question=question, docs="\n\n".join(docs))
