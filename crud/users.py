"""
Módulo que contiene las operaciones CRUD para manejar usuarios.
Este módulo interactúa con la base de datos para crear, obtener, 
actualizar y eliminar registros de usuarios.
"""

from sqlalchemy.orm import Session
import models.users
import schemas.users

def get_user(db: Session, user_id: int):
    """
    Obtiene un usuario por su ID.
    
    Args:
        db: La sesión de la base de datos.
        user_id: El ID del usuario a obtener.
        
    Returns:
        El usuario correspondiente al ID proporcionado, o None si no se encuentra.
    """
    return db.query(models.users.User).filter(models.users.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """
    Obtiene una lista de usuarios paginados.
    
    Args:
        db: La sesión de la base de datos.
        skip: El número de usuarios a omitir.
        limit: El número máximo de usuarios a obtener.
        
    Returns:
        Una lista de usuarios.
    """
    return db.query(models.users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.users.UserCreate):
    """
    Crea un nuevo usuario en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        user: Los datos del usuario a crear.
        
    Returns:
        El usuario creado.
    """
    db_user = models.users.User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        tipoUsuario=user.tipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        numeroTelefonico=user.numeroTelefonico,
        estatus=user.estatus,
        fechaRegistro=user.fechaRegistro,
        fechaActualizacion=user.fechaActualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.users.UserUpdate):
    """
    Actualiza un usuario existente en la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        user_id: El ID del usuario a actualizar.
        user: Los datos del usuario a actualizar.
        
    Returns:
        El usuario actualizado, o None si no se encuentra.
    """
    db_user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    if db_user:
        for var, value in vars(user).items():
            if value:
                setattr(db_user, var, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Elimina un usuario de la base de datos.
    
    Args:
        db: La sesión de la base de datos.
        user_id: El ID del usuario a eliminar.
        
    Returns:
        El usuario eliminado, o None si no se encuentra.
    """
    db_user = db.query(models.users.User).filter(models.users.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_user_by_usuario(db: Session, username: str):
    """
    Obtiene un usuario por su nombre de usuario.
    
    Args:
        db: La sesión de la base de datos.
        username: El nombre de usuario a buscar.
        
    Returns:
        El usuario correspondiente al nombre de usuario, o None si no se encuentra.
    """
    return db.query(models.users.User).filter(models.users.User.nombreUsuario == username).first()
