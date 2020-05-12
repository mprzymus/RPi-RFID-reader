import paho.mqtt.client as mqtt


class MqttSender:
    client = mqtt.Client()
    broker = {}
    is_name_accepted = False
    terminal_name = {}
    terminal_name_topic = "terminal_name"
    connection_topic = "connection"

    def __init__(self, terminal_name, broker="localhost", port=8883):
        self.terminal_name = terminal_name
        self.broker = broker
        self.connect(port)
        self.client.on_message = self.process_message
        self.client.subscribe(self.terminal_name_topic)
        self.send_message(self.connection_topic, self.generate_message(["Add"]))
        self.client.loop_start()

    def connect(self, port):
        self.client.tls_set("ca.crt")
        self.client.username_pw_set(username='client', password='password')
        self.client.connect(self.broker, port)

    def process_message(self, client, userdata, message):
        topic = message.topic
        message_as_string = str(message.payload.decode("utf-8"))
        if topic == "terminal_name":
            if message_as_string == str(True):
                self.is_name_accepted = True
                self.client.unsubscribe("terminal_name")
            else:
                self.terminal_name = input("Please type correct terminal name: ")
                self.send_message(self.connection_topic, self.generate_message(["Add"]))

    def disconnect(self):
        self.send_message(self.connection_topic, self.generate_message(["Remove"]))
        self.client.loop_stop()
        self.client.disconnect()

    def send_message(self, subject, message):
        self.client.publish(subject, message)

    def generate_message(self, info_list):
        message = ""
        for element in info_list:
            message = message + "." + element
        message = message + "." + self.terminal_name
        return message[1:]
