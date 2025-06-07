from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Item(Base):
    __tablename__ = "items"
    __table_args__ = {"schema": "dcp_api"} 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)

    category_id = Column(Integer, ForeignKey("dcp_api.categories.id"))
    category = relationship("Category", back_populates="items")

class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "dcp_api"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    items = relationship("Item", back_populates="category")
