#!/usr/bin/env python3
"""nsert a document in Python"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """a Python function that inserts a new
        document in a collection based on kwargs
    """
    return mongo_collection.insert_one(kwargs).inserted_id
