# -*- coding:utf-8 -*-
from geojson import Feature
from mdpipe.add import add_update_municipality
from mdpipe.shapes import shape_to_feature
from mdpipe.utils import as_utf8
from mdpipe.geo import sweref99tm_to_wgs84

__author__ = 'johan'


def to_geojson_feature(shape, record):
    f = Feature(
        id=record[2],
        geometry=geo_interface_sweref_to_wgs84(shape.__geo_interface__),
        properties={
            'Municipality': as_utf8(record[3].decode('latin-1')),
            'County': as_utf8(record[5].decode('latin-1'))
        }
    )
    return f


def geo_interface_sweref_to_wgs84(geo_interface):
    coordinates = geo_interface['coordinates'][0]
    coords = []
    for row in range(0, len(coordinates)):
        e, n = coordinates[row]
        lat, lon = sweref99tm_to_wgs84(n=n, e=e)
        coords.append((lon, lat))

    n_coords = [coords]

    geo_interface['coordinates'] = tuple(n_coords)
    return geo_interface


def process():
    for feature in shape_to_feature(
            "./sve_1milj_sh_99TM/svk/riks/ak_riks.shp",
            "./sve_1milj_sh_99TM/svk/riks/ak_riks.dbf",
            to_geojson_feature):
        add_update_municipality(feature)
