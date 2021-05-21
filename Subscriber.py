#subscriber.py
import pika
import sys
class Subscriber:
    def __init__(self, queueName, bindingKey, host, port, exchange):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.host = host
        self.port = port
        self.exchange = exchange
        self.connection = self._create_connection()
    
    def __del__(self):
        self.connection.close()
    
    def _create_connection(self):
        parameters=pika.ConnectionParameters(
            host=self.host,
            port = self.port
        )
        return pika.BlockingConnection(parameters)
    
    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print(body)
    
    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='topic'
        )
        channel.queue_declare(queue=self.queueName)
        channel.queue_bind(
            queue=self.queueName,
            exchange=self.exchange,
            routing_key=self.bindingKey
        )
        channel.basic_consume(
            queue=self.queueName,
            on_message_callback=self.on_message_callback, 
            auto_ack=True
        )
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()