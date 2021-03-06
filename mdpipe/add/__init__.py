# -*- coding:utf-8 -*-

import pymongo


def get_mongo():
    global db
    try:
        return db
    except:
        pass

    c = pymongo.MongoClient('127.0.0.1:27017')
    db = c['myndighetsdata']
    return db


def add_update_municipality(source):
    conn = get_mongo()
    conn.municipalitymap.update({'_id': source['id']}, source, upsert=True)


def add_update_source(source):
    conn = get_mongo()
    conn.source.update({'_id': source['id']}, source, upsert=True)


def insert_rawobjects(raw_obj):
    conn = get_mongo()
    conn.rawobjects.insert(raw_obj, upsert=True)