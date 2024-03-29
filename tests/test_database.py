import psycopg2
import unittest

class TestDatabaseConnection(unittest.TestCase):
    def test_database(self):
        conn_params = {
            'host': 'Elocalhost',
            'database': 'postgres',
            'port':  5432,
            'user': 'postgres',
            'password': '123456aa'
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
