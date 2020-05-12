import paho.mqtt.client as mqtt
import Server


class MqttReceiver:
    broker = "DESKTOP-CM5F6LF"
    client = mqtt.Client("server")
    owner = {}
    simple_usage = "simple_usage"
    generate_rapport = "generate_rapport"
    remove_user = "remove_user"
    new_user = "new_user"
    connection = "connection"
    terminal_name = "terminal_name"

    def __init__(self, owner):
        self.client.tls_set("ca.crt")
        self.client.username_pw_set(username='server', password='P@ssw0rd')
        self.client.connect(self.broker, 8883)
        self.client.on_message = self.process_message
        self.client.subscribe(self.simple_usage)
        self.client.subscribe(self.generate_rapport)
        self.client.subscribe(self.remove_user)
        self.client.subscribe(self.new_user)
        self.client.subscribe(self.connection)
        assert isinstance(owner, Server.Server)
        self.owner = owner
        self.client.loop_start()

    def process_message(self, client, userdata, message):
        topic_as_string = message.topic
        splitted_message = (str(message.payload.decode("utf-8"))).split(".")
        if topic_as_string == self.simple_usage:
            self.owner.notify_card_usage(splitted_message[0], splitted_message[1])
        elif topic_as_string == self.generate_rapport:
            self.owner.generate_rapport(splitted_message[0])
        elif topic_as_string == self.remove_user:
            self.owner.remove_user(splitted_message[0])
        elif topic_as_string == self.new_user:
            self.owner.add_user(splitted_message[0], splitted_message[1])
        elif topic_as_string == self.connection:
            if splitted_message[0] == "Add":
                is_name_right = str(self.owner.try_to_add_terminal(splitted_message[1]))
                self.client.publish(self.terminal_name, is_name_right)
            elif splitted_message[0] == "Remove":
                self.owner.remove_terminal(splitted_message[1])
            else:
                print("error")

    def __del__(self):
        self.client.loop_stop()
        self.client.disconnect()
