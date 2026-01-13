from sqlalchemy import Column, Integer, String, Float, Date, Time
from datetime import datetime, date
from database import Base

class InventarioPaso(Base):
    __tablename__ = "inventario_almacences"  # verifica que coincida con la tabla real
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
    # TIPOS ALINEADOS CON LA BD
    adddate = Column(Date, default=date.today)
    addtime = Column(Time, default=lambda: datetime.now().time())