from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    # title: str
    content: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    # email: str
    telegram_id: str


class UserCreate(UserBase):
    # password: str
    telegram_id: str


class User(UserBase):
    id: int
    telegram_id: str
    # is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True