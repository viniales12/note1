import sqlite3

from config import *


class Database:

    def __init__(self, user):
        self.name = user.name
        self.email = user.email
        self.phone = user.phone
        self.address = user.address
        self.country = user.country

    def connect_db(self):
        self.conn = sqlite3.connect(db_address)
        return self.conn

    def create_db(self):
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()
        self.cur.execute(''' CREATE TABLE users ( user_id INTEGER PRIMARY KEY NOT NULL,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        phone TEXT NOT NULL,
                        address TEXT NOT NULL,
                        country TEXT NOT NULL)
                    ''')
        self.conn.commit()
        self.conn.close()

    def add_user(self):
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('''
            INSERT INTO users (name, email, phone, address,       
                           country) VALUES (?, ?, ?, ?, ?)
            ''', (self.name, self.email, self.phone, self.address, self.country))

            self.conn.commit()
            self.conn.close()
        except:
            self.create_db()
            self.cur.execute('''
                    INSERT INTO users (name, email, phone, address,       
                                   country) VALUES (?, ?, ?, ?, ?)
                    ''', (self.name, self.email, self.phone, self.address, self.country))

            self.conn.commit()
            self.conn.close()
        finally:
            return f"New User {self.name} Successfully added"

    def show_db(self):
        self.users = []

        self.conn = self.connect_db()
        self.conn.row_factory = sqlite3.Row
        #  ^^^^^  umożliwia dostęp do kolumn za pomocą nazw, podczas gdy zwykła krotka wymagałaby użycia indeksów numerowanych
        self.cur = self.conn.cursor()

        try:
            for i in self.cur.execute('''SELECT * FROM users'''):
                user = {}
                user["user_id"] = i["user_id"]
                user["name"] = i["name"]
                user["email"] = i["email"]
                user["phone"] = i["phone"]
                user["address"] = i["address"]
                user["country"] = i["country"]
                self.users.append(user)
        except:
            self.create_db()
            for i in self.cur.execute('''SELECT * FROM users'''):
                user = {}
                user["user_id"] = i["user_id"]
                user["name"] = i["name"]
                user["email"] = i["email"]
                user["phone"] = i["phone"]
                user["address"] = i["address"]
                user["country"] = i["country"]
                self.users.append(user)
        finally:
            return self.users

    def show_db_id(self, id):
        self.users = []

        self.conn = self.connect_db()
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

        try:
            for i in self.cur.execute('''SELECT * FROM users WHERE user_id == ?''', (id,)):
                # przecinek w (id ,) bardzo ważny, inaczej błąd przy wprowadzeniu liczby dwucyfrowej
                user = {}
                user["user_id"] = i["user_id"]
                user["name"] = i["name"]
                user["email"] = i["email"]
                user["phone"] = i["phone"]
                user["address"] = i["address"]
                user["country"] = i["country"]
                self.users.append(user)
        except:
            self.create_db()
            for i in self.cur.execute('''SELECT * FROM users WHERE user_id == ?''', (id,)):
                # przecinek w (id ,) bardzo ważny, inaczej błąd przy wprowadzeniu liczby dwucyfrowej
                user = {}
                user["user_id"] = i["user_id"]
                user["name"] = i["name"]
                user["email"] = i["email"]
                user["phone"] = i["phone"]
                user["address"] = i["address"]
                user["country"] = i["country"]
                self.users.append(user)
        finally:
            return self.users

    def delete(self, id):
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('''DELETE FROM users WHERE user_id == ?''', (id,))

            self.conn.commit()
            self.conn.close()
            return f'User id:{id} Successfully deleted'
        except:
            return "Error. Table or user not exist"

    def update(self, id):
        self.conn = self.connect_db()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(
                "UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?",
                (self.name, self.email, self.phone, self.address, self.country, id))

            self.conn.commit()
            self.conn.close()

            return f"User {self.name} Successfully updated"
        except:
            return "Error. Table or user not exist"
