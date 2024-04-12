from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import API.db.auth.auth as auth
from API.db.conDeconDb import open_connection, close_db_connection
from .models import User
from .schemas import UserCreate
import psycopg2

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate):
    # Hash the user's password
    hashed_password = pwd_context.hash(user.password)
    
    # SQL statement for inserting a new user
    sql = """
    INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)
    """
    
    # Open a database connection
    conn = open_connection("login")
    if conn is not None:
        try:
            # Create a new cursor
            cur = conn.cursor()
            # Execute the insert statement
            cur.execute(sql, (user.email, hashed_password, 2))
            # Commit the transaction
            conn.commit()
            # Close the cursor
            cur.close()
        finally:
            # Close the database connection
            close_db_connection(conn)

def delete_user(user_email: str):
    # SQL statement for deleting a user
    sql = "DELETE FROM users WHERE username = %s"
    
    # Open a database connection
    conn = open_connection("login")
    if conn is not None:
        try:
            # Create a new cursor
            cur = conn.cursor()
            # Execute the delete statement
            cur.execute(sql, (user_email,))
            # Commit the transaction
            conn.commit()
            # Close the cursor
            cur.close()
            print(f"User {user_email} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")
            # Optionally, you might want to roll back if there's an error
            conn.rollback()
        finally:
            # Close the database connection
            close_db_connection(conn)
