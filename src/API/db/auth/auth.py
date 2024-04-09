import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from ..login.models import User

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

import psycopg2
from psycopg2 import OperationalError
from typing import Optional
from typing import Optional, Tuple

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str) -> User:
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Adjust the get user by username function for psycopg2 and PostgreSQL syntax
def get_user_by_username(connection: psycopg2.extensions.connection, username: str) -> Optional[Tuple[str, str]]:
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT username, password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        return user
    finally:
        cursor.close()  # Ensure the cursor is closed after operation

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)