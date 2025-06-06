from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    name: str
    quantity: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None

class ItemOut(ItemBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True  # สำหรับ Pydantic v2