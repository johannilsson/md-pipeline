# -*- coding:utf-8 -*-

def as_utf8(s):
    """ Ensure utf-8 for the provided s """
    try:
        return str(s)
    except UnicodeEncodeError:
        return unicode(s).encode('utf-8')
