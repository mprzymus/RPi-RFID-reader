import sqlite3
import CsvWriter
from operator import itemgetter


class DataBase:
    base = None
    default_date_out_value = "so far in"
    empty_string = ""

    def __init__(self):
        database_path = r"rfi_card.db"
        self.base = sqlite3.connect(database_path)
        cards = '''CREATE TABLE IF NOT EXISTS users (
                    card_number integer PRIMARY KEY,
                    user_name text
                )'''
        card_uses = '''CREATE TABLE IF NOT EXISTS visits (
                        card_used_id integer, 
                        time_in text DEFAULT CURRENT_TIMESTAMP,
                        time_out text,
                        FOREIGN KEY(card_used_id) REFERENCES users (card_number)
                )'''
        c = self.base.cursor()
        c.execute(cards)
        c.execute(card_uses)

    def process_card(self, card_id, users_name):
        self.update_user(card_id, users_name)
        try:
            users_visits = self.get_card_uses(card_id)
            users_last_visit = users_visits[0]
            if users_last_visit[2] == self.default_date_out_value:
                self.set_uses_out(users_last_visit)
            else:
                self.add_visit_record(card_id)
        except IndexError:
            self.add_visit_record(card_id)

    def update_user(self, key, name=None):
        already_in_database = self.get_user(key)
        c = self.base.cursor()
        if not already_in_database:
            users_table = ''' INSERT INTO users(card_number, user_name)
                                    VALUES(?, ?)'''
            if name == self.empty_string:
                name = None
            c.execute(users_table, (key, name))
        elif name and name != self.empty_string and already_in_database[1] != name:
            sql_update_name = ''' UPDATE users
                      SET user_name = ?
                      WHERE card_number = ?'''
            c.execute(sql_update_name, (name, key))

    def get_user(self, key):
        cur = self.base.cursor()
        cur.execute("SELECT * FROM users WHERE card_number=?", (key,))
        return cur.fetchone()

    def get_card_uses(self, key):
        cur = self.base.cursor()
        cur.execute("SELECT * FROM visits WHERE card_used_id=?", (key,))
        uses = cur.fetchall()
        uses.sort(key=itemgetter(1))
        uses.reverse()
        return uses

    def add_visit_record(self, visitor_id):
        visit_table = '''INSERT INTO visits(card_used_id, time_in, time_out) 
                                    VALUES(?, datetime('now', 'localtime'),?)'''
        c = self.base.cursor()
        c.execute(visit_table, (visitor_id, self.default_date_out_value))

    def set_uses_out(self, record):
        sql = ''' UPDATE visits
                      SET time_out = datetime('now', 'localtime')
                      WHERE card_used_id = ? AND
                            time_in = ?'''
        self.base.cursor().execute(sql, (record[0], record[1]))

    def generate_rapport(self, key):
        user = self.get_user(key)
        visits = self.get_card_uses(key)
        CsvWriter.write_data(user, visits)

    def remove_card_user(self, user_name):
        sql_command = ''''''

    def __del__(self):
        self.base.commit() # to save changes
        self.base.close()
