from sqlalchemy import Column, Integer, String, Float
from database import Base

class InventarioPaso(Base):
    __tablename__ = "inventario_toma_paso"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bodega = Column(String(100))
    ubicacion = Column(String(100))
    codigo = Column(String(100))
    descripcion = Column(String(200))
    cantidad = Column(Float)
