import sqlite3
conn=sqlite3.connect('bootcamp.db')

conn.execute("insert into participants values(119,'vinny','CSAI','Btech')")
conn.execute("insert into participants values(101,'snehi','CSI','Btech')")
conn.execute("insert into participants values(102,'ruchi','CS','Btech')")
conn.execute("insert into participants values(103,'anjana','CAI','Btech')")

conn.commit()
conn.close()