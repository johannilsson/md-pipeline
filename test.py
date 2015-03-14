import shapefile
import json

myshp = open("./sve_1milj_sh_99TM/svk/riks/ak_riks.shp", "rb")
mydbf = open("./sve_1milj_sh_99TM/svk/riks/ak_riks.dbf", "rb")

r = shapefile.Reader(shp=myshp, dbf=mydbf)

print r.fields


#for rec in r.records():
#    print rec

for shape in r.shapeRecords():
    #print json.dumps(shape.shape.__geo_interface__)
    print shape.record
