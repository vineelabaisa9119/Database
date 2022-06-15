'''
import
crete db
connect db
create a table
execte query
'''
import sqlite3
conn=sqlite3.connect('bootcamp.db')

'''
create table name(cname dt(size))
'''
query='''
     create table participants(gid int primary key,name text not null,branch text not null)
      '''
conn.execute(query)

