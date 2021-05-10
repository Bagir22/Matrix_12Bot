from pymongo import MongoClient
from config import MONGODB_URI


cluster = MongoClient(MONGODB_URI)

db = cluster["Matrix_12BotDB"]
collection = db["Matrix_12BotCollection"]
i = None
global fl_category, sl_category, fl_categories, sl_categories, tl_categories
items = None


def insert_data_into_db(id, fl_category=None, sl_category=None,
                        fl_categories=None, sl_categories=None,
                        tl_categories=None, i = None, items=None,
                        category=None, categories=None):
    collection.update({"id": id}, {"$set": {"fl_category": None, "sl_category": None,
                                            "fl_categories": None, "sl_categories": None,
                                            "tl_categories": None, "items": None,
                                            "i": None,
                                            "category": category,
                                            "categories": categories
                                            }}, upsert=True)



def insert_fl_categories(id, fl_categories, fl_category, sl_categories):
    collection.update_one(
        {"_id": id}, {"$set": {"fl_categories": fl_categories,
                               "fl_category": fl_category,
                               "sl_categories": sl_categories}})


def insert_tl_categories(id, sl_category, tl_categories):
    collection.update_one(
        {"_id": id}, {"$set": {"sl_category": sl_category,
                               "tl_categories": tl_categories}})


def get_sls_fl(id):
    sls = collection.find_one({"_id": id})["sl_categories"]
    fl = collection.find_one({"_id": id})["fl_category"]

    return sls, fl


def get_tls(id):
    tls = collection.find_one({"_id": id})["tl_categories"]

    return tls


def update_items(id, items=None, i=None):
    collection.update_one(
        {"_id": id}, {"$set": {"items": items, "i": i}})


def get_items(id):
    items = collection.find_one({"_id": id})["items"]
    i = collection.find_one({"_id": id})["i"]

    return items, i