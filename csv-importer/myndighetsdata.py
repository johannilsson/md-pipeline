#
#  myndighetsdata.py - Tools for importing data into api.myndighetsdata.se
#

import pymongo

def get_mongo():
  global db
  try:
    return db
  except:
    pass
  
  mongoclient = pymongo.MongoClient('127.0.0.1')
  db = mongoclient['myndighetsdata']
  return db


def addUpdateSource(source):

  conn = get_mongo()
  conn.sources.update({'_id':source['_id']},source,upsert=True)

  print conn.sources.find_one({'_id':source['_id']})

def makeKey(s):
  s = s.replace('.','_')
  return s