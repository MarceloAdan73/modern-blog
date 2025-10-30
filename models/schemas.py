from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    profile_picture: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None

class UserResponse(UserBase):
    id: int
    profile_picture: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    website: Optional[str]
    created_at: Optional[datetime]
    
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    excerpt: Optional[str] = None

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author_id: int
    author_name: str
    created_at: datetime
    updated_at: Optional[datetime]
    is_owner: bool = False
    
    class Config:
        from_attributes = True
