from pykafka import KafkaClient
import pykafka.exceptions
import pykafka.producer
import json ,requests, logging, time
from kafka import KafkaProducer
from datetime import datetime
from datetime import datetime
#r =requests.get('http://3.7.183.103:8080/metrics')

topic = '20A1'

def create_topic(topic):
    prod = KafkaProducer(bootstrap_servers='192.168.29.228:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    prod.send(topic,'wherw')
    return topic

def connect_kafka_producer():
    _client = None
    try:
        _client = KafkaClient(hosts="192.168.29.228:9092")
        print('connection is established')
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _client
#logger.info('Sending events...')
def publish(broker_instance,topicname):
    try:
        #client = KafkaClient(hosts="192.168.29.228:9092")
        print(broker_instance.topics)
        topic = broker_instance.topics[topicname]
        producer = topic.get_sync_producer()
        # message ="my first test  message"
        #print(messagecontent)
        while True:

            #r = requests.get('http://15.206.250.89:9090/api/v1/query?query=slurm_nodes_idle')
            r = requests.get('http://3.7.183.103:8080/metrics')
            #messagecontent = json.dumps(r.text)
            #messagecontent = messagecontent[6420:6460]
            messagecontent = json.dumps(r.text)
            #messagecontent = messagecontent["data"]
            producer.produce(messagecontent.encode('ascii'))
            time.sleep(5)
            # producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


def recip(topicname):
    client = KafkaClient(hosts="192.168.29.228:9092")
    print(client.topics)
    topic = client.topics[topicname]
    consumer = topic.get_simple_consumer()
    print('message from consumerr', consumer)
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

connect_kafka_producer()
publish(connect_kafka_producer(),topic)
# recip(topic)
