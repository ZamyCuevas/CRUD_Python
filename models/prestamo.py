from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.sql import func
from config.db import Base
import enum

class EstadoPrestamo(str, enum.Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    __tablename__ = "tbb_prestamos"

    id = Column("ID_Prestamo", Integer, primary_key=True, autoincrement=True)
    fecha_prestamo = Column("Fecha_Prestamo", DateTime, default=func.now(), nullable=False)
    fecha_devolucion = Column("Fecha_Devolucion", DateTime, nullable=True)
    estado_prestamo = Column("Estado_Prestamo", Enum(EstadoPrestamo), default=EstadoPrestamo.Activo, nullable=False)
