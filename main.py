from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import database
import schemas
import crud
import models

app = FastAPI(title="API Inventario")

# Crea tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

# ---------------------- ENDPOINTS ----------------------

@app.get("/api/bodegas", response_model=List[schemas.Bodega])
def obtener_bodegas(db: Session = Depends(database.get_db)):
    data = crud.obtener_bodegas(db)
    return [dict(row._mapping) for row in data]

@app.get("/api/productos", response_model=List[schemas.Producto])
def obtener_productos(db: Session = Depends(database.get_db)):
    data = crud.obtener_productos(db)
    return [dict(row._mapping) for row in data]

@app.get("/api/ubicaciones", response_model=List[schemas.Ubicacion])
def obtener_ubicaciones(db: Session = Depends(database.get_db)):
    data = crud.obtener_ubicaciones(db)
    return [dict(row._mapping) for row in data]

@app.post("/api/inventario")
def recibir_inventario(items: List[schemas.InventarioItemCreate], db: Session = Depends(database.get_db)):
    if not items:
        raise HTTPException(status_code=400, detail="Lista vacía")
    crud.insertar_inventario(db, [item.dict() for item in items])
    return {"status": "ok", "recibidos": len(items)}

# ---------------------- SERVIDOR ----------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
