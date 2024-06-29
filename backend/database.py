import sqlite3

class Database():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_table()

    def create_table(self):
        self.conn = sqlite3.connect(self.db_file)
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS pantry (
                    num INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT NOT NULL,
                    product_name TEXT NOT NULL
                )
            """)

    def add_item(self, barcode, product_name):
        with self.conn:
            self.conn.execute("INSERT INTO pantry (barcode, product_name) VALUES (?, ?)", 
                              (barcode, product_name))

    def remove_item(self, id):
        with self.conn:
            self.conn.execute("DELETE FROM pantry WHERE num = ?", (id,))

    def get_item(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pantry WHERE num = ?", (id,))
        return cursor.fetchone()
    
    def get_inventory(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pantry")
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()

class GroceryListDatabase():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_table()

    def create_table(self):
        self.conn = sqlite3.connect(self.db_file)
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS grocery (
                    num INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT NOT NULL,
                    product_name TEXT NOT NULL
                )
            """)

    def add_item(self, barcode, product_name):
        with self.conn:
            self.conn.execute("INSERT INTO grocery (barcode, product_name) VALUES (?, ?)", 
                              (barcode, product_name))

    def remove_item(self, id):
        with self.conn:
            self.conn.execute("DELETE FROM grocery WHERE num = ?", (id,))

    def get_item(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM grocery WHERE num = ?", (id,))
        return cursor.fetchone()
    
    def get_grocery(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM grocery")
        return cursor.fetchall()
    
    def clear_grocery(self):
        with self.conn:
            self.conn.execute("DELETE FROM grocery")

    def close(self):
        if self.conn:
            self.conn.close()