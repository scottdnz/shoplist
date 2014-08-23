#!/usr/bin/env python


"""
"""

import csv
import MySQLdb as mdb


def get_categories_sql():
    ''' '''
    sql = 'insert into category ( name, general_category) values {};';
    categories = []
    #Read CSV file
    f_name = 'categories.csv'
    f = open(f_name, 'rb')
    rows = csv.DictReader(f)
    #Build list of values to insert
    for row in rows:
        categories.append('(\'{}\', \'{}\')'.format(row['name'], 
                                                    row['general_category']))
    f.close()
    return sql.format(','.join(categories))


def get_categories_ids_dic(con):
    ''' '''
    categories_names_dic = {}
    sql = 'select name, id from category;'
    dict_cur = con.cursor(mdb.cursors.DictCursor)
    dict_cur.execute(sql)
    rows = dict_cur.fetchall()
    for row in rows:
        categories_names_dic[row['name']] = row['id']
    return categories_names_dic 


def get_items_sql(categories_names_dic):
    ''' '''
    sql = '''insert into item (label, brand, amount, units, category_id, 
description) values {};'''
    items = []
    f_name = 'items.csv'
    f = open(f_name, 'rb')
    rows = csv.DictReader(f)
    #Build list of values to insert
    for row in rows:
#         print(row)
        if not row['amount']:
            row['amount'] = 0
        cat_id = categories_names_dic[row['category_name']]
        items.append('(\'{}\', \'{}\', {}, \'{}\', {}, \'{}\')'.format(
               row['label'], row['brand'], row['amount'], row['units'], 
               cat_id, row['description']))
                                                    
    f.close()
    return sql.format(','.join(items))
    

if __name__ == "__main__":
    try:
        con = mdb.connect('localhost', 'marlena', 'youareasnoop', 'shoplist');
        cur = con.cursor()
        # Insert categories
        sql_cmd = get_categories_sql()
        cur.execute(sql_cmd)
        con.commit()
    
        categories_names_dic = get_categories_ids_dic(con)
        #for k, v in categories_names_dic.items():
        #    print('{}: {}'.format(k, v))
        
        #Insert items
        sql_cmd = get_items_sql(categories_names_dic) 
        print(sql_cmd)
        cur.execute(sql_cmd)
        con.commit()
    
    except mdb.Error, e:
        print "Error {0}: {1}".format(e.args[0], e.args[1])
        sys.exit(1)
        
    finally:    
        if con:    
            con.close()