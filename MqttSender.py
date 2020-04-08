import paho.mqtt.client as mqtt


class MqttSender:
    client = {}
    broker = {}

    def __init__(self, terminal_name, broker="localhost"):
        self.broker = broker
        self.client = mqtt.Client(terminal_name)
        self.client.connect(self.broker)
        self.send_message("Connected", terminal_name)

    def __del__(self):
        self.client.disconnect()

    def send_message(self, subject, message):
        self.client.publish(subject, message)


def generate_message(info_list):
    message = ""
    for element in info_list:
        message = message + "." + element
    return message[1:]
