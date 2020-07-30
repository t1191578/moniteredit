import psycopg2
#from dbconnection_to_postgre import Dbconnection_pg

class Db():
    #def __init__(self, host, user, passw, db):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(user="somo",
                                          password="12345678",
                                          host="moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com",
                                          port="5432",
                                          database="moniter")
            #self.con = psycopg2.connect(host, user, passw, db)

            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def version(self):
        pass

    def create_table(self):
        try:
            create_table_query = "CREATE TABLE IF NOT EXISTS Cluster (ip text PRIMARY KEY, servername text, password INTEGER);"
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while creating PostgreSQL table", error)
        finally:
            # closing database connection.
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")

    def insert_into_table(self,ip , servername , password ):
        cluster = (ip,servername,password)
        try:
            insert_query = "Insert into  Cluster values (%s ,%s,%s);"
            self.cursor.execute(insert_query,cluster)
            self.connection.commit()
            print("Table created successfully in PostgreSQL ")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while inserting data into  PostgreSQL table", error)
        finally:
            # closing database connection.
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")



if __name__ == '__main__':  # If it's executed like a script (not imported)
#    db = Db('moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com', 'somo', '12345678', 'moniter')

    db= Db()
    #db.create_table()
    db.insert_into_table('1','server1', 123)
  