import json
from datetime import datetime
from pykafka import KafkaClient
import requests
#https://www.datasciencewiki.com/2019/08/apache-kafka-tutorial-for-beginners_22.html

r =requests.get('http://3.7.183.103:8080/metrics')
#r.status_cod
#r.headers
#r.headers['Content-Type']
dump = json.dumps(r.text)
val=[r.text]
print(dump)
print(r.text.find('slurm_cpus_alloc 0'))
#print(val[6321])
print(dump[6420:6460])


input_file= open("C:\learning\Tasks\data.json")
json_array=json.load(input_file)
metrics = json_array['data']['result']
data ={}
data['Timetame']= str(datetime.utcnow())
data['metrics'] = metrics
val = json.dumps(data)

def publish(topicname,messagecontent):
    client = KafkaClient(hosts="192.168.29.228:9092")
    print(client.topics)
    topic = client.topics[topicname]
    producer = topic.get_sync_producer()
    #message ="my first test  message"
    print(messagecontent)
    producer.produce(messagecontent.encode('ascii'))


publish('Shanthi',val)