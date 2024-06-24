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
                    barcode TEXT PRIMARY KEY,
                    product_name TEXT NOT NULL
                )
            """)

    def add_item(self, barcode, product_name):
        with self.conn:
            self.conn.execute("INSERT INTO pantry (barcode, product_name) VALUES (?, ?)", 
                              (barcode, product_name))
            
    def remove_item(self, barcode):
        with self.conn:
            self.conn.execute("DELETE FROM pantry WHERE barcode = ?", (barcode,))

    def get_item(self, barcode):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM pantry WHERE barcode = ?", (barcode,))
        return cursor.fetchone()

    def close(self):
        if self.conn:
            self.conn.close()