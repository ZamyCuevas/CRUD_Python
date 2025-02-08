from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class EstadoMaterial(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    En_Mantenimiento = "En Mantenimiento"

class Material(Base):
    __tablename__ = "tbb_material"

    id = Column("ID_Material", Integer, primary_key=True, autoincrement=True)
    tipo_material = Column("Tipo_Material", String(100), nullable=False)
    marca = Column("Marca", String(100), nullable=True)
    modelo = Column("Modelo", String(100), nullable=True)
    estado = Column("Estado", Enum(EstadoMaterial), default=EstadoMaterial.Disponible, nullable=False)
