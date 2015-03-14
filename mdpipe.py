# -*- coding:utf-8 -*-

__author__ = 'johan'

from mdpipe.shapes import shape_to_feature_collection
from mdpipe.lantmateriet import to_geojson_feature
import json

s = shape_to_feature_collection(
    "./sve_1milj_sh_99TM/svk/riks/ak_riks.shp",
    "./sve_1milj_sh_99TM/svk/riks/ak_riks.dbf",
    to_geojson_feature
)


print json.dumps(s)
