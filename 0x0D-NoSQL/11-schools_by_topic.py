#!/usr/bin/env python3
"""
Python function
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    function that returns the list
    """
    return mongo_collection.find({"topics": topic})
