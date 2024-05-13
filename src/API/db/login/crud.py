from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import API.db.auth.auth as auth
from API.db.conDeconDb import open_connection, close_db_connection
from .models import User
from .schemas import UserCreate
import psycopg2
from fastapi import HTTPException

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(user: UserCreate, connection):
    hashed_password = pwd_context.hash(user.password)
    sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
    try:
        cur = connection.cursor()
        cur.execute(sql, (user.email, hashed_password, user.role))  # Assuming 'role' is part of UserCreate
        connection.commit()
        cur.close()
        user_data = {"username": user.email, "permissions": "example_permission"}
        token = auth.create_access_token(user_data)
        return token
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        close_db_connection(connection)

def store_token(db, username, token, expires_at):
    sql = """
    INSERT INTO user_tokens (username, token, expires_at) VALUES (%s, %s, %s)
    """
    db.cursor.execute(sql, (username, token, expires_at))
    db.conn.commit()

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
