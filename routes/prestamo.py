from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.prestamo, config.db, schemas.prestamo, models.prestamo
from typing import List

prestamo = APIRouter()

models.prestamo.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@prestamo.get("/prestamos/", response_model=List[schemas.prestamo.Prestamo], tags=["Préstamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.prestamo.get_prestamos(db=db, skip=skip, limit=limit)

@prestamo.get("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Préstamos"])
async def read_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamo.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")
    return db_prestamo

@prestamo.post("/prestamos/", response_model=schemas.prestamo.Prestamo, tags=["Préstamos"])
async def create_prestamo(prestamo: schemas.prestamo.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamo.create_prestamo(db=db, prestamo=prestamo)

@prestamo.put("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Préstamos"])
async def update_prestamo(id: int, prestamo: schemas.prestamo.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamo.update_prestamo(db=db, id=id, prestamo=prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado, no actualizado")
    return db_prestamo

@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamo.Prestamo, tags=["Préstamos"])
async def delete_prestamo(id: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamo.delete_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado, no eliminado")
    return db_prestamo
