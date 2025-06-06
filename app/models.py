from sqlalchemy import Column, Integer, String
from .database import Base

class Item(Base):
    __tablename__ = "items"
    __table_args__ = {"schema": "dcp_api"} 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)

class Category(Base):
    __tablename__ = "categories"
    __table_args__ = {"schema": "dcp_api"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

