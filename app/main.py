from fastapi import FastAPI
from .routes import items
from .database import Base, engine
from . import models

# สร้าง table ใน DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router)
