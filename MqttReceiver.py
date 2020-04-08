import paho.mqtt.client as mqtt


class MqttReceiver:
    broker = "localhost"
    client = mqtt.Client()
    owner = {}

    def __init__(self, owner):
        self.client.connect(self.broker)
        self.client.on_message = self.process_message
        self.client.loop_start()
        self.client.subscribe("card_used")
        self.owner = owner

    def process_message(self, client, userdata, message):
        splitted_message = (str(message.payload.decode("utf-8"))).split(".")
        self.owner.process_card(splitted_message[0])

    def __del__(self):
        self.client.disconnect()