#!/usr/bin/env python3
"""Copy index_range from the previous task"""
import math
import csv
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function index"""
    upper_limit = (page * page_size) - page_size
    lower_limit = page * page_size
    indexes_range = (upper_limit, lower_limit)
    return indexes_range


class Server:
    """class server"""
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
        """get_page"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        upper_limit, lower_limit = index_range(page, page_size)
        return self.dataset()[upper_limit:lower_limit]
