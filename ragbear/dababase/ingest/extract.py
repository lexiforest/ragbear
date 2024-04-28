from readability import Document
from markdownify import markdownify as md


def extract_md_from_html(s):
    doc = Document(s)
    html = doc.summary()
    plain_text = md(html, default_title=True)
    return plain_text


def chunked(s: str) -> list[str]:
    return s.split("\n\n")
