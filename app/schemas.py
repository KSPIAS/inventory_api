from pydantic import BaseModel
from typing import Optional

# Category
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = None

class CategoryOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # สำหรับ Pydantic v2

# Item
class ItemBase(BaseModel):
    name: str
    quantity: int
    category_id: int

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    quantity: Optional[int] = None

class ItemOut(ItemBase):
    id: int
    category: CategoryOut

    class Config:
        from_attributes = True

#############################################
class ItemOutCate(BaseModel):
    name: str
    quantity: int

    class Config:
        from_attributes = True

class CategoryOutItem(BaseModel):
    id: int
    name: str
    items: list[ItemOutCate]

    class Config:
        from_attributes = True
