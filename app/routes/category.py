from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, models
from ..database import get_db

router = APIRouter(prefix="/category", tags=["category"])

@router.post("/", response_model=schemas.CategoryOut)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)

@router.get("/", response_model=list[schemas.CategoryOut])
def read_categories(skip: int = 0, limit: int = 10 ,db: Session = Depends(get_db)):
    return crud.get_category(db=db ,skip=skip ,limit=limit)

@router.get("/item", response_model=list[schemas.CategoryOutItem])
def read_categories(skip: int = 0, limit: int = 10 ,db: Session = Depends(get_db)):
    return crud.get_category(db=db ,skip=skip ,limit=limit)

@router.patch("/{category_id}", response_model=schemas.CategoryOut)
def patch_category(category_id: int, category: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category_id, category)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_id}")
def delete_category(category_id: int ,db: Session = Depends(get_db)):
    category_name = db.query(models.Category.name).filter(models.Category.id == category_id).scalar()
    db_category = crud.delete_category(db=db ,category_id=category_id)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"detail": f"Category {category_name} deleted"}
