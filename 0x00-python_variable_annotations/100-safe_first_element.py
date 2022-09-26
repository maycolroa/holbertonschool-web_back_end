#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations"""
from typing import Iterable, List, Sequence, Tuple, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns"""
    if lst:
        return lst[0]
    else:
        return None
