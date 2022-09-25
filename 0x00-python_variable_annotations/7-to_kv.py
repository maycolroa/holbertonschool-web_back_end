#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string k and an int OR float v"""
from typing import Tuple, Union

number = Union[int, float]


def to_kv(k: str, v: number) -> Tuple[str, float]:
    """sum_mixed_list"""
    return (k, v * v)
