import mongodb
import urlparse
import json

def makejson(o):
  def dthandler(obj):
    if hasattr(obj, 'isoformat'):
      return obj.isoformat()
    else:
      raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(o), repr(o))
  return json.dumps(o, default=dthandler)


def request(env, start_response):
  getdata = urlparse.parse_qs(env['QUERY_STRING'])
  start_response('200 OK', [('Content-Type', 'application/json')])
  try:
    return makejson(fromid(int(getdata['id'][0])))
  except:
    pass
    
  try:
    return makejson(scbid(float(getdata['wgs84lon'][0]),float(getdata['wgs84lat'][0])))
  except:
    pass

  try:
    return makejson(getall(getdata['all'][0]))
  except:
    pass
    
  return "no data found"
  
def getdata():
  conn = mongodb.get_mongo()
  data = conn.municipalitymap.find({},{ '_id': 0 })
  ut = []
  for muni in data:
    ut.append(muni)
  data = {"municipalities":ut}
  return data

def getall(id):
  conn = mongodb.get_mongo()
  data = conn.municipalitymap.find({},{ '_id': 0, "geometry":0, "type":0 })
  ut = []
  for muni in data:
    ut.append(muni)
  
  data = {"municipalities":ut}
  return data
  
def fromid(id):
  conn = mongodb.get_mongo()
  data =  conn.municipalitymap.find_one({ "id":id},{ '_id': 0 })
  return data

def scbid(lon, lat):
  conn = mongodb.get_mongo()
  data =  conn.municipalitymap.find_one(
    { "geometry": 
       {"$geoIntersects": 
          {"$geometry": 
             {"type": "Point",
             "coordinates": [lon, lat]
             }
          }
        }
    },{ '_id': 0 })
  return data
