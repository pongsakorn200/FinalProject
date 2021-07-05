import sqlite3

class SqliteHelper:
    def __init__(self,name=None):
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()

        except sqlite3.Error:
            print("Failed connecting to database...")


    def create_table_device(self):
        c = self.cursor
        c.execute('''CREATE TABLE devices(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    port TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    notify VARCHAR(10) NOT NULL,
                    status VARCHAR(10) NOT NULL)''')

    def create_table_token(self):
        c = self.cursor
        c.execute('''CREATE TABLE tokens(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address VARCHAR(255) NOT NULL)''')
    
    def create_table_device_has_token(self):
        c = self.cursor
        c.execute('''CREATE TABLE device_has_token(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_name TEXT NOT NULL,
                    token_name TEXT NOT NULL)''')
        
    def create_table_position(self):
        c = self.cursor
        c.execute('''CREATE TABLE position(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_name TEXT NOT NULL,
                    position VARCHAR(20),
                    address VARCHAR(255),
                    ip TEXT NOT NULL,
                    status VARCHAR(10) NOT NULL)''')

    def edit(self,query,updates):#UPDATE
        c = self.cursor
        c.execute(query, updates)
        self.conn.commit()

    def delete(self,query): #DELETE
        c = self.cursor
        c.execute(query)
        self.conn.commit()

    def insert(self,query): #,inserts):#INSERT
        c = self.cursor
        c.execute(query) #,inserts)
        self.conn.commit()

    def select(self,query): #SELECT
        c = self.cursor
        c.execute(query)
        return c.fetchall()
