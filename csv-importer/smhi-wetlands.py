# -*- coding: utf-8
import myndighetsdata as md

from StringIO import StringIO

source = {  "_id": "smhi-wetlands", "description": "SMHI lagrar här information om våtmarker från Jordbruksverket och länsstyrelserna i en Våtmarksdatabas. Syftet är att samla och förvalta en nationell databas för anlagda våtmarker i Sverige samt erbjuda information om anlagda våtmarker för nedladdning. Våtmarker som ska lagras i databasen är våtmarker för närsaltsreduktion som tar emot vatten från definierade tillrinningsområden. Det utesluter dock inte att även andra våtmarker rapporteras in. Rapportering från Jordbruksverket och respektive Länsstyrelsen till SMHI kommer att göras löpande, dock minst en gång per år.", "license": "CC-0", "licensetext": "Så långt det är möjligt ska SMHI anges som källa, med länk och datum för nedladdning." }
md.addUpdateSource(source)

input = open('smhi-wetlands.csv')

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