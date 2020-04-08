import paho.mqtt.client as mqtt


class MqttSender:
    client = {}
    broker = "localhost"

    def __init__(self, terminal_name):
        self.client = mqtt.Client(terminal_name)
        self.client.connect(self.broker)
        self.send_message("Connected")

    def __del__(self):
        self.client.disconnect()

    def send_message(self, message):
        self.client.publish("card_used", message)


def generate_message(self, info_list):
    message = ""
    for element in info_list:
        message = message + "." + element
    return message[1:]
