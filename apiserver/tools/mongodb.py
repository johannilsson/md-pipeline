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
