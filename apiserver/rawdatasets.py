
import os
import json

import mongodb

rawdatasets = [
  'hav-viss-grundvatten',
  'smhi-wetlands',
  'ivl-sot-statistik',
  'ivl-dvst_pah_gd',
  'ivl-dvslufar'
]

def makejson(o):
  def dthandler(obj):
    if hasattr(obj, 'isoformat'):
      return obj.isoformat()
    else:
      raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(o), repr(o))
  return json.dumps(o, default=dthandler)


def requestRawDataset (env, start_response):

  sourcename = os.path.basename(env['PATH_INFO'].lower())
  
  conn = mongodb.get_mongo()
      
  start_response('200 OK', [('Content-Type', 'application/json')])
  #return [sourcename]
  items = list( conn['rawobjects'].find({'source':sourcename}) )
      
  for i in range(0,len(items)):
    del items[i]['_id']

  result = { 'data': items }
  return [ makejson(result) ]


def init( resources ):
  for setname in rawdatasets:
    resources['/rawdatasets/'+setname] = requestRawDataset

  #resources['/rawdatasets'] = showRawDataSets
