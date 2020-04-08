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
                client.send_message(MqttSender.generate_message([key]))
            elif command == 2:
                key = get_key()
                client.generate_rapport(key)
            elif command == 3:
                key = get_key()
                client.remove_user(key)
            elif command == 4:
                key = get_key()
                name = input("type user name ")
                client.add_user(key, name)
            elif command == 5:
                break
            else:
                print("wrong input %s" % command)
        except ValueError:
            print("Incorrect input")
    del client


if __name__ == '__main__':
    wait_for_input()
