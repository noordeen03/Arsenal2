import sqlite3
c = 'y'
conn = sqlite3.connect('test.db')
conn.execute("create table if not exists vnist1(id number primary key,Pname text,Admittedtime timestamp,wno number,room number,Docname text,primary key(id))")
while(c == 'y' or c=='Y' ) :
    conn.execute("insert into vnist1(id,Pname,Admittedtime,wno,room,Docname) values(?,?,?,?,?,?)",(input(),input(),input(),input(),input(),input()))
    conn.commit()
    print("Do you want continue:(y/n)")
    c=input()
data = conn.execute("select * from vnist1")
for row in data:
    print( row[1], row[2], row[3],row[0],row[4],row[5])

