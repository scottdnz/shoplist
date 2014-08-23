#!/usr/bin/env python

"""
"""

import MySQLdb as mdb
from django.conf import settings


def fetch_items():
    """ """
    db = settings.DATABASES['default']
    items = [] 
    con = mdb.connect(db['HOST'], db['USER'], db['PASSWORD'], db['NAME']);

    sql_cmd = 'select * from item order by label;'
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute(sql_cmd)
    rows = cur.fetchall()
    for row in rows:
        items.append({'id': row['id'],
                      'label': row['label'],
                      'brand': row['brand'],
                      'amount': row['amount'],
                      'units': row['units'],
                      'category_id': row['category_id'],
                      'description': row['description']} )
    return items