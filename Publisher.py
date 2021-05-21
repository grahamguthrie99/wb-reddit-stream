import pika

class Publisher:
    def __init__(self, host, port, exchange, routing_key):
        self.host=host
        self.port=port
        self.exchange=exchange
        self.routing_key=routing_key

    def publish(self, message):       
        connection = self.create_connection()
        channel= connection.channel()
        channel.exchange_declare(
            exchange=self.exchange, 
            exchange_type='topic')
        channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key, 
            body=message)
        connection.close()
        print("Sent Message: {}".format(message))
 
    def create_connection(self):
        param = pika.ConnectionParameters(
            host=self.host,
            port=self.port) 
        return pika.BlockingConnection(param)