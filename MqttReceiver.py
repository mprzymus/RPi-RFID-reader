import paho.mqtt.client as mqtt
import Server


class MqttReceiver:
    broker = "localhost"
    client = mqtt.Client("server")
    owner = {}
    simple_usage = "simple_usage"
    generate_rapport = "generate_rapport"
    remove_user = "remove_user"
    new_user = "new_user"

    def __init__(self, owner):
        self.client.connect(self.broker)
        self.client.on_message = self.process_message
        self.client.subscribe(self.simple_usage)
        self.client.subscribe(self.generate_rapport)
        self.client.subscribe(self.remove_user)
        self.client.subscribe(self.new_user)
        assert isinstance(owner, Server.Server)
        self.owner = owner

    def process_message(self, client, userdata, message):
        print("nice")
        topic_as_string = message.topic
        splitted_message = (str(message.payload.decode("utf-8"))).split(".")
        if topic_as_string == self.simple_usage:
            self.owner.notify_card_usage(splitted_message[0])
        elif topic_as_string == self.generate_rapport:
            self.owner.generate_rapport(splitted_message[0])
        elif topic_as_string == self.remove_user:
            self.owner.remove_user(splitted_message[0])
        elif topic_as_string == self.new_user:
            self.owner.add_user(splitted_message[0], splitted_message[1])

    def loop(self):
        self.client.loop_forever()

    def __del__(self):
        self.client.disconnect()
