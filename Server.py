from database import DataBase


class Server:
    database = DataBase()
    clients_list = []

    def notify_card_usage(self, key, terminal, name=None):
        self.database.process_card(key, terminal, name)

    def generate_rapport(self, key):
        self.database.generate_rapport(key)

    def print_user_info(self, key):
        user = self.database.get_user(key)
        visits = self.database.get_card_uses(key)
        print(user)
        print(visits)

    def add_user(self, card_id, name):
        self.database.update_user(card_id, name)

    def remove_user(self, key):
        self.database.remove_card_user(key)

    def remove_terminal(self, terminal):
        self.clients_list.remove(terminal)

    def try_to_add_terminal(self, terminal):
        if terminal in self.clients_list:
            return False
        self.clients_list.append(terminal)
        return True

    def __del__(self):
        del self.database
