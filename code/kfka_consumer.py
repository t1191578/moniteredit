from pykafka import KafkaClient
import pykafka
import pykafka.exceptions
import pykafka.producer
import json
from kafka import KafkaProducer
import logging
from datetime import datetime

topic ='22A1'

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

def recip(client,topicname):
    #client = KafkaClient(hosts="192.168.29.228:9092")
    topic = client.topics[topicname]
    consumer = topic.get_simple_consumer()
    print('message from consumerr', consumer)
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)

#connect_kafka_producer()
#publish(connect_kafka_producer(),topic)
recip(connect_kafka_producer(),topic)