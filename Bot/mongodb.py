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
                        category=None, categories=None,
                        kb_index=None):
    collection.update({"id": id}, {"$set": {"fl_category": None, "sl_category": None,
                                            "fl_categories": None, "sl_categories": None,
                                            "tl_categories": None, "items": None,
                                            "i": None, "kb_index": None,
                                            "category": category,
                                            "categories": categories
                                            }}, upsert=True)



def insert_fl_categories(id, fl_categories, fl_category, sl_categories):
    collection.update_one(
        {"id": id}, {"$set": {"fl_categories": fl_categories,
                               "fl_category": fl_category,
                               "sl_categories": sl_categories}})


def insert_tl_categories(id, sl_category, tl_categories):
    collection.update_one(
        {"id": id}, {"$set": {"sl_category": sl_category,
                               "tl_categories": tl_categories}})


def get_sls_fl(id):
    sls = collection.find_one({"id": id})["sl_categories"]
    fl = collection.find_one({"id": id})["fl_category"]

    return sls, fl


def get_tls(id):
    tls = collection.find_one({"id": id})["tl_categories"]

    return tls


def update_items(id, items=None, i=None, category = None):
    collection.update_one(
        {"id": id}, {"$set": {"items": items,
                               "i": i,
                               "category": category}})


def update_i(id, i):
    collection.update_one(
        {"id": id}, {"$set": {"i": i}})


def update_keyboard_index(id, kb_index):
    collection.update_one(
        {"id": id}, {"$set": {"kb_index": kb_index}})



def get_items(id):
    items = collection.find_one({"id": id})["items"]
    i = collection.find_one({"id": id})["i"]
    category = collection.find_one({"id": id})["category"]

    return items, i, category


def get_categories(id):
    fl_categories = collection.find_one({"id": id})["fl_categories"]
    sl_categories = collection.find_one({"id": id})["sl_categories"]
    tl_categories = collection.find_one({"id": id})["tl_categories"]
    kb_index = collection.find_one({"id": id})["kb_index"]

    return fl_categories, sl_categories, tl_categories, kb_index