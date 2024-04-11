#!/usr/bin/env python3
"""List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """List all documents Available"""
    return [] if not mongo_collection else list(mongo_collection.find())
