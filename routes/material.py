from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.material, config.db, schemas.material, models.material
from typing import List

material = APIRouter()

models.material.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materiales/", response_model=List[schemas.material.Material], tags=["Materiales"])
async def read_materiales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.material.get_materiales(db=db, skip=skip, limit=limit)

@material.get("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return db_material

@material.post("/materiales/", response_model=schemas.material.Material, tags=["Materiales"])
async def create_material(material: schemas.material.MaterialCreate, db: Session = Depends(get_db)):
    return crud.material.create_material(db=db, material=material)

@material.put("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def update_material(id: int, material: schemas.material.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.material.update_material(db=db, id=id, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado, no actualizado")
    return db_material

@material.delete("/material/{id}", response_model=schemas.material.Material, tags=["Materiales"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.material.delete_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado, no eliminado")
    return db_material
