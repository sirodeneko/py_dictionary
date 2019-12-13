import sqlite3

conn = sqlite3.connect('db/EDB.db')

cursor = conn.cursor()

cursor.execute('select * from Ewordmap limit 1')

values = cursor.fetchall()

for item in values:
    print(item)