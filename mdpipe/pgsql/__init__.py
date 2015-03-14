# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import json
import requests


def _parse_row(cols):
    if cols is None or len(cols) == 0:
        return None
    cols = [elem.text.strip() for elem in cols]
    return cols


def parse(html):
    soap = BeautifulSoup(html)
    tables = soap.find_all('table')

    table = tables[2]

    rows = table.find_all('tr')
    headings = None
    data = []
    for row in rows:
        if headings is None:
            headings = _parse_row(row.find_all('th'))
        values = _parse_row(row.find_all('td'))
        if values is not None and headings is not None:
            data.append(dict(zip(headings, values)))

    form = soap.find('form')
    inputs = form.find_all('input')
    next_page = None
    for input_ele in inputs:
        if input_ele['name'] == 'Z_START':
            next_page = input_ele['value']

    return data, next_page


def query_pgsql_web(url, page):
    r = requests.get(url, params={
        'Z_ACTION': 'NEXT',
        'Z_START': page
    })
    if r.status_code != 200:
        return None, page
    data, next_page = parse(r.text)
    return data, next_page
