import psycopg2

#conn
con = psycopg2.connect(
    host = "moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com",
    database = "moniter",
    user = "somo",
    password = "12345678")
cursor=con.cursor()
cursor.execute("select * from userdetails")
rows = cursor.fetchall()

print(rows)
#close conn
con.close()