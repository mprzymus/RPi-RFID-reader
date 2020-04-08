from Server import Server


def get_key():
    return input("type card id ")


def wait_for_input():
    server = Server()
    while True:
        try:
            command = int(input("1 - card use, 2 - generate rapport, 3 - remove user, 4 - add card user, 5 - exit "))
            if command == 1:
                key = get_key()
                server.notify_card_usage(key)
            elif command == 2:
                key = get_key()
                server.generate_rapport(key)
            elif command == 3:
                key = get_key()
                server.remove_user(key)
            elif command == 4:
                key = get_key()
                name = input("type user name ")
                server.add_user(key, name)
            elif command == 5:
                break
            else:
                print("wrong input %s" % command)
        except ValueError:
            print("Incorrect input")
    del server
