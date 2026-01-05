from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
import models

def obtener_bodegas(db: Session):
    return db.execute(text("SELECT bodega, descripcion FROM control_inventarios.id_bodegas Order By bodega ")).fetchall()

def obtener_productos(db: Session):
    return db.execute(text("SELECT codigo_barras_linea AS codigo_barras, item, descripcion, unidad_medida, unidad_despacho " \
    "FROM control_inventarios.w_productos")).fetchall()

def obtener_ubicaciones(db: Session):
    return db.execute(text("SELECT bodega as id_bodega, ubicacion as id_ubicacion FROM control_inventarios.id_ubicaciones")).fetchall()

def insertar_inventario(db: Session, items: List[dict]):
    for item in items:
        db.add(models.InventarioPaso(
            bodega=item["bodega"],
            ubicacion=item["ubicacion"],
            codigo=item["codigo"],
            descripcion=item["descripcion"],
            cantidad=float(item["cantidad"]),
        ))
    db.commit()
