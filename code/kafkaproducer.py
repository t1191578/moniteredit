import pykafka
import pykafka.exceptions
import pykafka.producer
import time
import logging
from kafka import KafkaProducer


logging.getLogger("pykafka").addHandler(logging.StreamHandler())
logging.getLogger("pykafka").setLevel(logging.DEBUG)
prod = KafkaProducer(bootstrap_servers='localhost:9092')
prod.send('test1',b'sdsad')


producer =KafkaProducer(bootstrap_server=['192.168.29.228:9092:9092'],api_version=(0,10,1))
producer.send('test1',b'some message')
kafka_client = pykafka.KafkaClient(hosts="192.168.29.228:9092")
# kafka_client = pykafka.KafkaClient(hosts="192.168.100.108:9092", socket_timeout_ms=3000)
# bin/kafka-topics.sh --list --bootstrap-server ec2-13-232-15-89.ap-south-1.compute.amazonaws.com:9092
# print(KafkaClient.topics)
topic = kafka_client.topics["tepic A"]

producer = topic.get_producer(delivery_reports=False,
                                                          min_queued_messages=100,
                                                           max_queued_messages=100000,
                                                         linger_ms=1000,
                                                         block_on_queue_full=False)


message="my  test  message"
print(message)

producer.produce('some test 123'.encode('ascii'))

consumer = topic.get_simple_consumer()
print('message from consumerr', consumer)
