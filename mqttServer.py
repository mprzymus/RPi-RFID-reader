from MqttReceiver import MqttReceiver
from Server import Server


def main():
    server = Server()
    mqtt = MqttReceiver(server)
    command = ""
    while command != "exit":
        command = input()


if __name__ == '__main__':
    main()
