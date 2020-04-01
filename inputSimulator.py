from inputResolver import DataBase


def wait_for_input():
    database = DataBase()
    while True:
        try:
            key = int(input("Type key (negative to finish) "))
            if key < 0:
                break
            name = input("Type name to update (empty to skip) ")
            database.process_card(key, name)
            id_to_write = input("Type name to generate rapport (empty to skip) ")
            if id_to_write:
                database.generate_rapport(id_to_write)
        except ValueError:
            print("Incorrect input")
    del database
