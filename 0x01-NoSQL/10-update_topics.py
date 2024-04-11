#!/usr/bin/env python3
"""Change school topics"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """a Python function that changes all
        topics of a school document based on the name
    """
    return mongo_collection.update_mant(
        {"name": name},
        {"$set": {"topics": topics}}
    )
