import psycopg2

class Dbconnection_pg:
        # moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com:5432
    #somo, 1-8 dbname: moniter
    try:
        connection = psycopg2.connect(user = "somo",
                                      password = "12345678",
                                      host = "moniterdbprom.crnro4ewkaoo.ap-south-1.rds.amazonaws.com",
                                      port = "5432",
                                      database = "moniter")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record,"\n")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        '''
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")'''