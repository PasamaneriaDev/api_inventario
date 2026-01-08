from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from datetime import datetime
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
            cod_almacen=item["cod_almacen"],
            num_linea=item["num_linea"],
            bodega=item["bodega"],
            area=item["area"],
            codigo_barras=item["codigo_barras"],
            cod_item=item["cod_item"],
            descripcion=item["descripcion"],
            stkumid=item.get("stkumid", ""),
            uniddesp=float(item.get("uniddesp", 0)),
            cantidad=float(item["cantidad"]),
            computador=item.get("computador", "API"),
            adduser=item.get("adduser", "api_user"),
            adddate=item.get("adddate", datetime.now().strftime("%Y-%m-%d")),
            addtime=item.get("addtime", datetime.now().strftime("%H:%M:%S"))
        ))
    db.commit()

def obtener_productos_paginado(db: Session, skip: int = 0, limit: int = 10000):
    query = """
        SELECT codigo_barras_linea, codigo_barras_obsoleto, codigo_barras_paquete, item, descripcion, unidad_medida, unidad_despacho
        FROM control_inventarios.w_productos
        ORDER BY item
        LIMIT :limit OFFSET :skip
    """
    # CORRECCIÓN: Se agrega text(query) para que SQLAlchemy 2.0 lo acepte
    return db.execute(text(query), {"skip": skip, "limit": limit}).fetchall()