"""
Módulo que contiene las operaciones CRUD para manejar materiales.
Este módulo interactúa con la base de datos para crear, obtener, 
actualizar y eliminar registros de materiales.
"""

from sqlalchemy.orm import Session
import models.material
import schemas.material

def get_material(db: Session, material_id: int):
    """
    Obtiene un material por su ID.
    
    Args:
        db: La sesión de la base de datos.
        material_id: El ID del material a obtener.
        
    Returns:
        El material correspondiente al ID proporcionado, o None si no se encuentra.
    """
    return db.query(models.material.Material).filter(
        models.material.Material.id == material_id
    ).first()

def get_materiales(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de materiales paginados.
    
    Args:
        db: La sesión de la base de datos.
        skip: El número de materiales a omitir.
        limit: El número máximo de materiales a obtener.
        
    Returns:
        Una lista de materiales.
    """
    return db.query(models.material.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.material.MaterialCreate):
    """
    Crea un nuevo material en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        material: Los datos del material a crear.
        
    Returns:
        El material creado.
    """
    db_material = models.material.Material(
        tipo_material=material.tipo_material,
        marca=material.marca,
        modelo=material.modelo,
        estado=material.estado
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material_id: int, material: schemas.material.MaterialUpdate):
    """
    Actualiza un material existente en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        material_id: El ID del material a actualizar.
        material: Los datos del material a actualizar.
        
    Returns:
        El material actualizado, o None si no se encuentra.
    """
    db_material = db.query(models.material.Material).filter(
        models.material.Material.id == material_id
    ).first()
    if db_material:
        for var, value in vars(material).items():
            if value:
                setattr(db_material, var, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, material_id: int):
    """
    Elimina un material de la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        material_id: El ID del material a eliminar.
        
    Returns:
        El material eliminado, o None si no se encuentra.
    """
    db_material = db.query(models.material.Material).filter(
        models.material.Material.id == material_id
    ).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
