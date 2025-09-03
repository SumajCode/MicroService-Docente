import pika
from config.conf import BaseConf

parameters = pika.URLParameters(BaseConf.HOST_MQ)
publisher = pika.BlockingConnection(parameters)
channelPublisher = publisher.channel()

def publish():
    channelPublisher.basic_publish(
        exchange=BaseConf.EXCHANGE,
        routing_key=BaseConf.NAME_QUEUE,
        body='Create and compile file')