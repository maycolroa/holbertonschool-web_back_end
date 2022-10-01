#!/usr/bin/env python3
""""""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """"""
    upper_limit = (page * page_size) - page_size
    lower_limit = page * page_size
    indexes_range = (upper_limit, lower_limit)
    return indexes_range
