from sqlalchemy import Column, Integer, String, Float
from datetime import datetime
from database import Base

class InventarioPaso(Base):
    __tablename__ = "inventario_almacences" 
    __table_args__ = {"schema": "control_inventarios"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    cod_almacen = Column(String(255))
    num_linea = Column(Integer)
    bodega = Column(String(255))
    area = Column(String(255))
    codigo_barras = Column(String(255))
    cod_item = Column(String(255))
    descripcion = Column(String(255))
    stkumid = Column(String(255))
    uniddesp = Column(Float)
    cantidad = Column(Float)
    computador = Column(String(255))
    adduser = Column(String(255))
    adddate = Column(String(255), default=lambda: datetime.now().strftime("%Y-%m-%d"))
    addtime = Column(String(255), default=lambda: datetime.now().strftime("%H:%M:%S"))