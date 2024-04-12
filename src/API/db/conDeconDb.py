import psycopg2

class Database:

    def __init__(self, db_type):
        self.conn = None
        self.cursor = None
        # Define connection strings for different database types
        dsn_config = {
            "firerisk": "dbname=firerisk user=postgres password=123456aa host=host.docker.internal port=5555",
            "login": "dbname=login user=postgres password=123456aa host=host.docker.internal port=5555"
        }
        try:
            self.conn = psycopg2.connect(dsn_config[db_type])
            self.cursor = self.conn.cursor()
            print(f"Database connection to {db_type} was successful")
            
        except Exception as e:
            print(f"Failed to connect to the {db_type} database: {e}")
        

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed")
