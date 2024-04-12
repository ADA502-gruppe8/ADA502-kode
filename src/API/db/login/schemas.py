from pydantic import BaseModel
from typing import List, Optional

class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class Role(RoleBase):
    id: int
    users: List['User'] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    role_id: int

class UserCreate(UserBase):
    password: str

class User(UserBase):
    role: Role

    class Config:
        orm_mode = True

# This is necessary to resolve the forward reference from Role
Role.update_forward_refs()