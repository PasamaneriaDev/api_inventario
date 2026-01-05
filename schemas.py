from unicodedata import numeric
from pydantic import BaseModel
from typing import List, Optional

class Bodega(BaseModel):
    bodega: str
    descripcion: str


class Producto(BaseModel):
    codigo_barras: str
    item: str
    descripcion: str
    unidad_medida: Optional[str] = None
    unidad_despacho: Optional[float] = None


class Ubicacion(BaseModel):
    id_bodega: str
    id_ubicacion: str

class InventarioItem(BaseModel):
    bodega: str
    ubicacion: str
    codigo: str
    descripcion: str
    cantidad: str

class InventarioItemCreate(InventarioItem):
    pass
