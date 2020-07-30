import logging

from pykafka import KafkaClient
from pykafka.exceptions import SocketDisconnectedError
logging.basicConfig(level='DEBUG')
client = KafkaClient(hosts='192.168.29.228:9092')
topic = client.topics['1']

consumer = None
try:
    consumer =  topic.get_balanced_consumer(consumer_group='test-group',
                                            zookeeper_connect='zookeeper:2181',
                                            auto_commit_enable=True,
                                            auto_commit_interval_ms=1000)
    while True:
        message = consumer.consume()
        print (message.__dict__)
except SocketDisconnectedError:
    print ('handle error here')
finally:
    if consumer:
        consumer.stop()