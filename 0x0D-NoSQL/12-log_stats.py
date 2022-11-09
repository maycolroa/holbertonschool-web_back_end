#!/usr/bin/env python3
"""
Python script
"""
from pymongo import MongoClient


def method_requester(method_dict: dict) -> int:
    """
    database
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    return logs.count_documents(method_dict)


def printer():
    """
    Print MongoDB
    """
    print(f"{method_requester({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {method_requester({'method': 'GET'})}")
    print(f"\tmethod POST: {method_requester({'method': 'POST'})}")
    print(f"\tmethod PUT: {method_requester({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {method_requester({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {method_requester({'method': 'DELETE'})}")
    print(f"{method_requester({'method': 'GET', 'path': '/status'})} status check")


if __name__ == "__main__":
    printer()
