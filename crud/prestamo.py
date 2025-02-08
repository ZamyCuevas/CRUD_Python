"""
Módulo que contiene las operaciones CRUD para manejar préstamos.
Este módulo interactúa con la base de datos para crear, obtener, actualizar y eliminar
registros de préstamos.
"""

from sqlalchemy.orm import Session
import models.prestamo
import schemas.prestamo

# Módulo que contiene funciones CRUD para manejar los préstamos.

def get_prestamo(db: Session, prestamo_id: int):
    """
    Obtiene un préstamo por su ID.
    
    Args:
        db: La sesión de la base de datos.
        prestamo_id: El ID del préstamo a obtener.
        
    Returns:
        El préstamo correspondiente al ID proporcionado, o None si no se encuentra.
    """
    return db.query(models.prestamo.Prestamo).filter(
        models.prestamo.Prestamo.id == prestamo_id
    ).first()

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de préstamos paginados.
    
    Args:
        db: La sesión de la base de datos.
        skip: El número de préstamos a omitir.
        limit: El número máximo de préstamos a obtener.
        
    Returns:
        Una lista de préstamos.
    """
    return db.query(models.prestamo.Prestamo).offset(skip).limit(limit).all()

def create_prestamo(
    db: Session, prestamo: schemas.prestamo.PrestamoCreate
):
    """
    Crea un nuevo préstamo en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        prestamo: Los datos del préstamo a crear.
        
    Returns:
        El préstamo creado.
    """
    db_prestamo = models.prestamo.Prestamo(
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=prestamo.fecha_devolucion,
        estado_prestamo=prestamo.estado_prestamo
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(
    db: Session, prestamo_id: int, prestamo: schemas.prestamo.PrestamoUpdate
):
    """
    Actualiza un préstamo existente en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        prestamo_id: El ID del préstamo a actualizar.
        prestamo: Los datos del préstamo a actualizar.
        
    Returns:
        El préstamo actualizado, o None si no se encuentra.
    """
    db_prestamo = db.query(models.prestamo.Prestamo).filter(
        models.prestamo.Prestamo.id == prestamo_id
    ).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            if value:
                setattr(db_prestamo, var, value)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, prestamo_id: int):
    """
    Elimina un préstamo de la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        prestamo_id: El ID del préstamo a eliminar.
        
    Returns:
        El préstamo eliminado, o None si no se encuentra.
    """
    db_prestamo = db.query(models.prestamo.Prestamo).filter(
        models.prestamo.Prestamo.id == prestamo_id
    ).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
