import argparse
from uuid import uuid4
from six.moves import input
from confluent_kafka import SerializingProducer
from confluent_kafka.serialization import StringSerializer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer


class User(object):
    
    def __init__(self, name, address, favorite_number, favorite_color):
        self.name = name
        self.favorite_number = favorite_number
        self.favorite_color = favorite_color
        # address should not be serialized, see user_to_dict()
        self._address = address


def user_to_dict(user, ctx):
    r = requests.get('http://3.7.183.103:8080/metrics')
    val = (json.dumps(r.text)).split('\\n')
    messagecontent = val[121:145:3]
    d = dict(x.split(" ") for x in messagecontent)
      # User._address must not be serialized; omit from dict
    return d


def delivery_report(err, msg):

    if err is not None:
        print("Delivery failed for User record {}: {}".format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


def main(bootstrap_servers,schema_registry,topic):
    topic = topic
    schema_str = {
      "title": "User",
      "required": [ "name" ]
    }
    schema_registry_conf = {'url': schema_registry}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    json_serializer = JSONSerializer(schema_str, schema_registry_client, user_to_dict)

    producer_conf = {'bootstrap.servers': bootstrap_servers,
                     'key.serializer': StringSerializer('utf_8'),
                     'value.serializer': json_serializer}

    producer = SerializingProducer(producer_conf)

    print("Producing user records to topic {}. ^C to exit.".format(topic))
    while True:
        # Serve on_delivery callbacks from previous calls to produce()
        producer.poll(0.0)
        try:
            r = requests.get('http://3.7.183.103:8080/metrics')
            messagecontent = json.dumps(r.text)
            producer.produce(topic=topic, key=str(uuid4()), value=messagecontent,
                             on_delivery=delivery_report)
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid input, discarding record...")
            continue

    print("\nFlushing records...")
    producer.flush()


if __name__ == '__main__':
    bootstrap_servers = '192.168.29.228:9092'
    schema_registry = 'http://3.7.183.103:8080/metrics'
    topic = '20A3'
    main(bootstrap_servers,schema_registry,topic)
