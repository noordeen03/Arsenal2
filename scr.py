import sqlite3
conn = sqlite3.connect('test.db')
data = conn.execute("select * from vnist1")
for row in data:
    print(row[0], row[1], row[2], row[3],row[4],row[5])
