import argparse

from influxdb import InfluxDBClient


host='15.206.2.79'
port=8086
user = 'admin'
password = '123'
dbname = 'example123'
dbuser = 'smly'
dbuser_password = 'my_secret_password'
retention_days = '3d'
#client = InfluxDBClient(host, port, user, password, dbname)
#client = InfluxDBClient(host='15.206.42.79', port=8086, username='admin', password='123', database=dbname)
print("Create database: " + dbname)
client.create_database(dbname)
print("Create user: " + dbuser)
###client.create_user(dbuser, dbuser_password, admin=False)
###client.grant_privilege('all', dbname, dbuser)
# grant_privilege(privilege, database, username)
print("Create a retention policy")
###client.create_retention_policy('awesome_policy', retention_days, 3, database=dbname, default=True)
# create_retention_policy(name, duration, replication, database=None, default=False, shard_duration=u'0s')

#url: "http://15.206.42.79:8086/api/v1/prom/write?db=prom1metrics&u=pr&p=111"

#form this url:


#drop_database(dbname)
#drop_user(username)
    #print("Drop database: " + dbname)
    #client.drop_database(dbname)


#https://influxdb-python.readthedocs.io/en/latest/api-documentation.html