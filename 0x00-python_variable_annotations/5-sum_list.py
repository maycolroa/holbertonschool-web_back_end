#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list input_list"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
