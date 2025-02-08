from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EstadoMaterial(str, Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    En_Mantenimiento = "En Mantenimiento"

class MaterialBase(BaseModel):
    tipo_material: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    estado: EstadoMaterial

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int

    class Config:
        orm_mode = True
