#!/usr/bin/env python3
"""index_range function and Server class"""
import math
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns a tuple"""
    upper_limit = (page * page_size) - page_size
    lower_limit = page * page_size
    indexes_range = (upper_limit, lower_limit)
    return indexes_range


class Server:
    """Server class"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        upper_limit, lower_limit = index_range(page, page_size)
        return self.dataset()[upper_limit:lower_limit]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_hyper method"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        total_pages = math.floor(len(self.dataset()) / page_size)
        data_dict = {'page_size': len(self.get_page(page, page_size)),
                     'page': page,
                     'data': self.get_page(page, page_size),
                     'next_page': page + 1 if page + 1 < total_pages else None,
                     'prev_page': page - 1 if page > 1 else None,
                     'total_pages': total_pages
                     }
        return data_dict
