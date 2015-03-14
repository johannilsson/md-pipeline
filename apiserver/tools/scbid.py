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
  return makejson(scbid(float(getdata['wgs84lon'][0]),float(getdata['wgs84lat'][0])))

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
    })
  try:
    del data['_id']
  except KeyError:
    pass
  return data
