from fastapi import FastAPI
from .routes import items ,category
# from .database import Base, engine
from .database import engine
from . import models

# สร้าง table ใน DB
# Base.metadata.create_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)
app.include_router(category.router)
