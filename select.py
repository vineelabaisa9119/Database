import sqlite3
conn=sqlite3.connect('bootcamp.db')

res=conn.execute("select * from participants")
for i in  res:
    print(i)