# -*- coding:utf-8 -*-

import shapefile
from geojson import FeatureCollection


def shape_to_feature_collection(shp, dbf, parser):
    myshp = open(shp, "rb")
    mydbf = open(dbf, "rb")

    r = shapefile.Reader(shp=myshp, dbf=mydbf)

    results = []
    for shape in r.shapeRecords():
        results.append(parser(shape.shape, shape.record))

    return FeatureCollection(results)







