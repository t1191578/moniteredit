from kafka import KafkaProducer
from datetime import datetime
import time
from json import dumps
import json ,requests, logging, time

KAFKA_TOPIC_NAME = "20A1"
KAFKA_BOOTSTRAP_SERVERS_CONS = '192.168.29.228:9092'
def success(metadata):
    print(metadata.topic)
def error(exception):
    print(exception)

if __name__ == "__main__":
    print("Kafka Producer Application Started ... ")

    kafka_producer_obj = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS_CONS,
                             value_serializer=lambda x: dumps(x).encode('utf-8'))
    try:
        while True:
            r = requests.get('http://3.7.183.103:8080/metrics')
            messagecontent = json.dumps(r.text)
            val = messagecontent.split('\\n')
            messagecontent = val[121:145:3]
            kafka_producer_obj.send(KAFKA_TOPIC_NAME, messagecontent).add_callback(success).add_errback(error)
            time.sleep(1)
            #producer.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))