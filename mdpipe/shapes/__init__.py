# -*- coding:utf-8 -*-

import shapefile


def shape_to_feature(shp, dbf, parser):
    myshp = open(shp, "rb")
    mydbf = open(dbf, "rb")
    r = shapefile.Reader(shp=myshp, dbf=mydbf)
    for shape in r.shapeRecords():
        yield parser(shape.shape, shape.record)







