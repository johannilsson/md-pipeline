# -*- coding: utf-8
import myndighetsdata as md

from StringIO import StringIO

source = {  "_id": "hav-viss-grundvatten", "description": "Beslutadeklassningar 20091222 statussammanställning grundvattenförekomster hela Sverige 2015-03-13 18.09", "license": "CC-0", "licensetext": "Så långt det är möjligt ska VISS anges som källa, med länk och datum för nedladdning." }
md.addUpdateSource(source)

input = open('grundvatten-latest.csv')

keynames = {}

for line in (input.readline(),input.readline()):
  line = line.rstrip()
  items = line.split(';')
  for i in range(0,len(items)):
    if not items[i]: continue
    keynames[i] = md.makeKey( items[i] )

print keynames    

conn = md.get_mongo()

for line in input.readlines():
  line = line.rstrip()

  i = 0
  insert = {'source':source['_id']}
  for item in line.split(';'):
    if item:
      insert[keynames[i]] = item
      i += 1

  conn.rawobjects.insert(insert)
  #print insert