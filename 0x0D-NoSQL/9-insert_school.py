#!/usr/bin/env python3
"""
Python function
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
