#!/usr/bin/env python3
"""
Hypermedia pagination module for a database of popular baby names.
This module provides a Server class with methods for paginating data.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    This class provides methods to access and paginate the dataset.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset of popular baby names.

        Returns:
            List[List]: The dataset as a list of lists.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.

        Args:
            page (int): The page number (default: 1).
            page_size (int): The number of items per page (default: 10).

        Returns:
            List[List]: The requested page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = self.index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Calculate the start and end indices for a given page and page size.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            Tuple[int, int]: A tuple containing the start and end indices.
        """
        return index_range(page, page_size)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Retrieve a page of data along with pagination information.

        Args:
            page (int): The page number (default: 1).
            page_size (int): The number of items per page (default: 10).

        Returns:
            Dict[str, Any]: A dictionary containing
            pagination information and data.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
        }
