import psycopg2

class Database:

    def __init__(self, dsn):
        self.conn = None
        self.cursor = None
        try:
            self.conn = psycopg2.connect(dsn)
            self.cursor = self.conn.cursor()
            print("Database connection was successful")
            
        except Exception as e:
            print(f"Failed to connect to the database: {e}")
        

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed")