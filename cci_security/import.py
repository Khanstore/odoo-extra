#!/usr/bin/python
# -*- encoding: utf-8 -*-
import csv
import datetime
import time
from datetime import date, timedelta
import psycopg

map_sec = {
'model_id':  lambda x: '',
'group_id': lambda x:'', #should be the last day of x['YEAR,I,4']
'perm_read': lambda x: '',#should be the first day of x['YEAR,I,4']
'perm_create': lambda x: '',
'perm_unlink': lambda x:  '',
'perm_write': lambda x:  '',
'name':lambda x: '',
}
map_headers = {
'model_id': 'model_id',
'group_id': 'group_id', #should be the last day of x['YEAR,I,4']
'perm_read': 'perm_read',#should be the first day of x['YEAR,I,4']
'perm_create': 'perm_create',
'perm_unlink': 'perm_unlink',
'perm_write': 'perm_write',
'name':'name'
}

def import_csv(writer_security, map_sec, map_headers):
    print "creating csv"
    s = "host=localhost dbname=mra user='postgres' port=5432 password='postgres'"
    handle=psycopg.connect(s)
    cr = handle.cursor()
    cr.execute("select model as model_id,'1' as perm_read,  model as name,'1' as perm_create,'1' as perm_unlink,'1' as perm_write,res_groups.name as group_id from ir_model,res_groups where model like '%cci%' order by model")
    d=[]
    record = {}
#    for key, column_name in map_headers.items():
#        print key
#        record[key] = column_name
    #record1 = ['model_id', 'group_id', 'perm_read', 'perm_create', 'perm_unlink', 'perm_write']
#    print record
    record = {'model_id': 'model_id', 'group_id': 'group_id',  'perm_read': 'perm_read', 'perm_unlink': 'perm_unlink', 'perm_write': 'perm_write', 'perm_create': 'perm_create','name':'name'}
    writer_security.writerow(record)

    for i in cr.fetchall():
#        for j in range(len(i)):
 #           print j
        record = {}
        j=0
        for key,fnct in map_sec.items():
            record[key] =  i[j]
            j=j+1
        writer_security.writerow(record)
if __name__=='__main__':
    writer_security = csv.DictWriter(file('ir.model.access.csv', 'wb'),map_sec.keys())
    import_csv(writer_security, map_sec, map_headers)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
