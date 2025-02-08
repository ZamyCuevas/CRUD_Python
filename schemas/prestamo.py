from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EstadoPrestamo(str, Enum):
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class PrestamoBase(BaseModel):
    fecha_prestamo: Optional[datetime] = None
    fecha_devolucion: Optional[datetime] = None
    estado_prestamo: EstadoPrestamo

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id: int

    class Config:
        orm_mode = True
