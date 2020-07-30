import sqlite3

# moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com:5432
#somo, 1-8 dbname: moniter
#
#
#
connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (ip text PRIMARY KEY, servername text, password INTEGER)"
cursor.execute(create_table)
user = ('10.2', 'prom1', 5000)
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    ('10.3', 'prom2', 5000),
    ('10.4', 'prom3', 5000)
]

cursor.executemany(insert_query,users)


select_query = " SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()