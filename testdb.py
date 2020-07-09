import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()


create_table = "CREATE TABLE IF NOT EXISTS users (ip text PRIMARY KEY, servername text, password INTEGER)"
cursor.execute(create_table)
user =('10.2', 'prom1', 5000)
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)



select_query = " SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)




connection.commit()

connection.close()