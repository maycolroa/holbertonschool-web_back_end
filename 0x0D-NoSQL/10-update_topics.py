#!/usr/bin/env python3
"""
Python function
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    function that changes all topics
    """
    return mongo_collection.update_many({"name": name}, {'$set': {"topics": topics}})
