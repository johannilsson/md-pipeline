import gevent
from gevent import monkey,sleep ; monkey.patch_all()
from gevent.pywsgi import WSGIServer, WSGIHandler
from gevent.server import StreamServer
from gevent.queue import Queue
from datetime import datetime
import urlparse

import rawdatasets
import tools

resources = {}

def newRequest(env, start_response):
  if env['PATH_INFO'].startswith('/datasets'):
    start_response('500 Not yet implemented', [('Content-type','text/plain')])
    return ['Hello there! The feature you are looking for has not yet been implemented']

  path = env['PATH_INFO'].lower()

  if resources.has_key(path):
    return resources[path](env,start_response)

  start_response('404 Not Found', [('Content-Type', 'text/plain')])
  return ['Not found']

rawdatasets.init( resources )
tools.init( resources )

a = gevent.pywsgi.WSGIServer(('127.0.0.1',3480), newRequest) #handler_class=CustomWSGI)
a.serve_forever()
