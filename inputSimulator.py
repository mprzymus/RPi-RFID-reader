import MqttSender


def get_key():
    return input("type card id ")


def wait_for_input():
    client = MqttSender.MqttSender("T1")
    while True:
        try:
            command = int(input("1 - card use, 2 - generate rapport, 3 - remove user, 4 - add card user, 5 - exit "))
            if command == 1:
                key = get_key()
                client.send_message("simple_usage", MqttSender.generate_message([key]))
            elif command == 2:
                key = get_key()
                client.send_message("generate_rapport", MqttSender.generate_message([key]))
            elif command == 3:
                key = get_key()
                client.send_message("remove_user", MqttSender.generate_message([key]))
            elif command == 4:
                key = get_key()
                name = input("type user name ")
                client.send_message("new_user", MqttSender.generate_message([key, name]))
            elif command == 5:
                break
            else:
                print("wrong input %s" % command)
        except ValueError:
            print("Incorrect input")
    del client


if __name__ == '__main__':
    wait_for_input()
