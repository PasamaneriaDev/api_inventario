from pydantic import BaseModel
from typing import Optional

class Bodega(BaseModel):
    bodega: str
    descripcion: str

class Producto(BaseModel):
    codigo_barras_linea: Optional[str] = None
    codigo_barras_obsoleto: Optional[str] = None
    codigo_barras_paquete: Optional[str] = None
    item: str
    descripcion: str
    unidad_medida: Optional[str] = None
    unidad_despacho: Optional[float] = None


class Ubicacion(BaseModel):
    id_bodega: str
    id_ubicacion: str


class InventarioItemCreate(BaseModel):
    cod_almacen: str
    num_linea: int
    bodega: str
    area: str
    codigo_barras: str
    cod_item: str
    descripcion: str
    stkumid: Optional[str] = ""
    uniddesp: Optional[float] = 0.0
    cantidad: float
    computador: Optional[str] = "API"
    adduser: Optional[str] = "api_user"
    adddate: Optional[str] = None
    addtime: Optional[str] = None


class InventarioItem(InventarioItemCreate):
    id: int

    class Config:
        from_attributes = True
