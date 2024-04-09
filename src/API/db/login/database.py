import psycopg2
from psycopg2 import OperationalError
from typing import Optional
from typing import Optional, Tuple

def open_connection(host: str = 'localhost', port: str = '5555', database: str = 'login') -> Optional[psycopg2.extensions.connection]:
    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            database=database
        )
        print("Connection to the database successful")
        return connection
    
    except OperationalError as e:
        print("The error occurred while connecting to the database:", e)
        return None

# Correct the close connection function for psycopg2
def close_connection(connection: psycopg2.extensions.connection):
    try:
        connection.close()
        print("Connection to the database closed")
    except Exception as error:  # Adjusted to catch a broader range of potential errors
        print("Error while closing the database connection", error)
        raise error