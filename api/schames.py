from pydantic import BaseModel
from typing import List, Optional, Any


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_staff: bool

    class Config:
        orm_mode = True


class CategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductSchema(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    count: int
    category_id: Optional[int]

    class Config:
        orm_mode = True


class OrderSchema(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int
    count: int
    order_status: str

    class Config:
        orm_mode = True


class RegisterModel(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_staff: bool
    is_active: bool

    class Config:
        orm_mode = True
        schemas_extra = {
            "example": {
                "first_name": "Diyorbek",
                "last_name": "Axmadjonov",
                "username": "Dior",
                "email": "dior@gmail.com",
                "password": "2004",
                "is_staff": True,
                "is_active": True
            }
        }


class LoginModel(BaseModel):
    username: str
    password: str


class Settings(BaseModel):
    authjwt_secret_key: str = "be3edb546db38da200931a851ff405db0f85a21b8b8571007628a44b565a91ac"
