#!/usr/bin/env python3
"""
1. Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters."""
        return (page - 1) * page_size, page * page_size

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        total_items = len(self.dataset())
        total_pages = (total_items + page_size - 1) // page_size
        data = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
