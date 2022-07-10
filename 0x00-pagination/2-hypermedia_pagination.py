#!/usr/bin/env python3
"""Simple pagination."""
import csv
import math
from typing import List, Dict   


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple containing start index and an end index."""
    end = page_size * page
    start = end - page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset
        (the correct list of rows).
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)
        if start_idx >= len(dataset):
            return []

        return [row for row in dataset[start_idx:end_idx]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Hypermedia pagination."""
        dataset = self.dataset()
        idx_range = index_range(page, page_size)
        current_page = math.ceil(idx_range[1] / page_size)
        
        try:
            dataset[idx_range[1] + 1]
            next_page = current_page + page_size - 1
        except IndexError:
            next_page = None

        prev_page = current_page - page_size + 2
        if prev_page < 0:
            prev_page = None
        
        pagiation = {
            'page_size': len(self.get_page(page, page_size)),
            'page': current_page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(len(dataset) / page_size)
        }

        return pagiation