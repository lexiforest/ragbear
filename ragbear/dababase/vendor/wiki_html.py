import zhconv
from pathlib import Path

from ..index.hnsw import HnswIndex
from ..extract import extract_md_from_html


def import_all(p):
    index = HnswIndex()
    for file in Path().glob("**/*.html"):
        with open(file) as f:
            text = extract_md_from_html(f.read())
        text = text.replace("[编辑]", "")
        simplfied = zhconv.convert(text)
    index.add(simplfied)

