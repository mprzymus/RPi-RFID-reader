from inputResolver import DataBase


class Server:
    database = DataBase()
    clients_list = []

    def notify_card_usage(self, key):
        self.database.process_card(key)

    def generate_rapport(self, key):
        self.database.generate_rapport(key)

    def print_user_info(self, key):
        user = self.database.get_user(key)
        visits = self.database.get_card_uses(key)
        print(user)
        print(visits)

    def add_user(self, card_id, name):
        self.database.update_user(card_id, name)

    def remove_user(self, name):
        self.database.remove_card_user(name)