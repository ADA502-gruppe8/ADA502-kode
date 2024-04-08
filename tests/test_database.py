import psycopg2
import unittest
from decouple import config

class TestDatabaseConnection(unittest.TestCase):
    def test_database(self):
        conn_params = {
            'host': 'localhost',
            'database': 'postgres',
            'port':  5432,
            'user': config('DATABASE_USERNAME'),
            'password': config('DATABASE_PASSWORD')
        }
        
        try:
            conn = psycopg2.connect(**conn_params)
            conn.close()
            self.assertTrue(True)  # Test passes if connection is successful
        except Exception as e:
            print("Error:", e)
            self.fail(f"Failed to connect to the database: {str(e)}")  # Use self.fail() to indicate a test failure


if __name__ == '__main__':
    unittest.main()
