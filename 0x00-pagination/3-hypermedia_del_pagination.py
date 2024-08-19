#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position,
         starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia pagination information.

        Args:
            index (int): The start index of the current page (default: None).
            page_size (int): The size of the page (default: 10).

        Returns:
            Dict: A dictionary containing pagination information and data.
        """
        dataset = self.indexed_dataset()

        # Handle the case where index is None
        if index is None:
            index = 0

        # Assert that index is in a valid range
        assert 0 <= index < len(dataset), "Index out of range"

        data = []
        next_index = index
        current_size = 0

        while current_size < page_size and next_index < len(dataset):
            if next_index in dataset:
                data.append(dataset[next_index])
                current_size += 1
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
