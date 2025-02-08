from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base
import enum
from sqlalchemy.sql import func

class MyEstatus(str,enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class TipoUsuario(str,enum.Enum):
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Directivo = "Directivo"
    Administrativo = "Administrativo"

class User(Base):
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    tipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(40))
    numeroTelefonico = Column(String(20))
    estatus = Column(Enum(MyEstatus))
    fechaRegistro = Column(DateTime, default=func.now())
    fechaActualizacion = Column(DateTime, default=func.now(), onupdate=func.now())
   
