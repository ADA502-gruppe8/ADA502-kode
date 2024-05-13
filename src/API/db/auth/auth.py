import jwt
from jwt.exceptions import InvalidKeyTypeError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from ..login.models import User
from fastapi import Header, HTTPException, Security
from API.db.auth import auth  # Adjust path as necessary
import psycopg2
from psycopg2 import OperationalError
from typing import Optional
from typing import Optional, Tuple
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi import Depends, HTTPException
from ..conDeconDb import Database

SECRET_KEY = "kosogkaker"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

security = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(username: str):
    expire = datetime.utcnow() + timedelta(minutes=15)  # Token expires in 15 minutes
    payload = {"sub": username, "exp": expire}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token, expire

def validate_token(db, token):
    sql = """
    SELECT username FROM user_tokens WHERE token = %s AND expires_at > CURRENT_TIMESTAMP
    """
    db.cursor.execute(sql, (token,))
    result = db.cursor.fetchone()
    if result:
        return result[0]  # Returns the username
    return None

# Dependency that creates and disposes of a database connection
async def get_database():
    db = Database("your connection string here")
    await db.connect()
    try:
        yield db
    finally:
        await db.close()

async def get_current_user(token: str = Depends(oauth2_scheme), db: Database = Depends(get_database)):
    username = await validate_token(db, token)
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return await get_user_by_username(db, username)

def authenticate_user(username: str, password: str, connection) -> Optional[str]:
    user = get_user_by_username(connection, username)
    if not user or not verify_password(password, user[1]):
        return None
    user_data = {"username": user[0], "permissions": "example_permission"}  # Customize as needed
    return create_access_token(user_data)

async def validate_token(db, token):
    # Assuming token validation includes checking the DB for revocation or expiry
    query = "SELECT username FROM user_tokens WHERE token = $1 AND expires_at > CURRENT_TIMESTAMP"
    result = await db.conn.fetch(query, token)
    if result:
        return result[0]["username"]
    else:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

async def get_user_by_username(db, username):
    query = "SELECT * FROM users WHERE username = $1"
    user = await db.conn.fetchrow(query, username)
    if user:
        return dict(user)
    else:
        raise HTTPException(status_code=404, detail="User not found")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)