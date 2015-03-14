# -*- coding:utf-8 -*-

from mdpipe.add import insert_rawobjects
from mdpipe.pgsql import query_pgsql_web
import json


datasets = [
    {
        'name': 'Sot statistik',
        'source': 'ivl-sot-statistik',
        'url': 'http://www3.ivl.se/db/plsql/dvst_sot_st$b1.querylist'
    },
    {
        'name': 'Bensen statistik',
        'source': 'ivl-bensen-statistik',
        'url': 'http://www3.ivl.se/db/plsql/dvst_bensen_st$b1.querylist'
    },
    {
        'name': 'Miljöövervakning av flyktiga organiska ämnen samt polyaromatiska kolväten i tätortsmiljö',
        'source': 'ivl-dvst_pah_gd',
        'url': 'http://www3.ivl.se/db/plsql/dvst_pah_gd$b1.querylist'
    },
    {
        'name': 'Årsmedelhalter i luft',
        'source': 'ivl-dvslufar',
        'url': 'http://www3.ivl.se/db/plsql/dvslufar$b1.querylist'
    },
]


def _process(dataset, page):
    data, next_page = query_pgsql_web(dataset['url'], page)
    if len(data) > 0:
        for d in data:
            d.update({'source': dataset['source']})
            insert_rawobjects(d)
        _process(dataset, next_page)
        print next_page


def add_ivl_data():
    for dataset in datasets:
        _process(dataset, -100)

