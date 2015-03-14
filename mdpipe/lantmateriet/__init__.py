# -*- coding:utf-8 -*-
from geojson import Feature, Polygon
from mdpipe.utils import as_utf8
from mdpipe.geo import sweref99tm_to_wgs84, rt90_to_wgs84


def to_geojson_feature(shape, record):
    f = Feature(
        id=record[2],
        geometry=geo_interface_sweref_to_wgs84(shape.__geo_interface__),
        properties={
            'Municipality': as_utf8(record[3].decode('latin-1')),
            'Area': as_utf8(record[5].decode('latin-1'))
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