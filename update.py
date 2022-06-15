import sqlite3
conn=sqlite3.connect('bootcamp.db')

query='''
      update participants set name='Vinny' where gid=119
      '''
conn.execute(query)

print(conn.total_changes)
conn.commit()
conn.close()