#!/usr/bin/env python3
"""
Write a Python function that lists all documents in a collection
"""
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    List all documents in a MongoDB collection
    """
    documents = list(mongo_collection.find())
    return documents if documents else []
