import hnswlib
import numpy as np

DIM = 128
num_elements = 10_000


class HnswIndex:

    def __init__(self, dim: int, max_elements, num_threads: int=4, ef_construction: int = 200,):
        """
        Args:
            max_elements, the maximum number of elements (capacity). Will throw an exception if exceeded


        """
        self.dim = dim
        self.max_elements = max_elements
        self.num_threads = num_threads
        self.ef_construction = ef_construction
        self._index = None

    def create(self):
        index = hnswlib.Index(space="cosine", dim=self.dim)
        index.init_index(max_elements=self.max_elements, ef_construction=200, M=16)
        return index

    def load(self):
        ...

    def save(self):
        ...

    def add_items(self, items: list):
        ...

    def query(self, q: str, k: int = 1):
        labels, distance = self._index.knn_query(data=q, k=k)
        labels = [[self.dict]]
        ...



