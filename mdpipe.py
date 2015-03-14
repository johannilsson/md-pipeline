# -*- coding:utf-8 -*-
from mdpipe.ivl import add_ivl_data

__author__ = 'johan'

from mdpipe.shapes import shape_to_feature
from mdpipe.lantmateriet import to_geojson_feature
from mdpipe.add import add_update_municipality

#for feature in shape_to_feature(
#        "./sve_1milj_sh_99TM/svk/riks/ak_riks.shp",
#        "./sve_1milj_sh_99TM/svk/riks/ak_riks.dbf",
#        to_geojson_feature):
#    add_update_municipality(feature)


add_ivl_data()

