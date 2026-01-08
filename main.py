from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.responses import HTMLResponse
from typing import List
import database
import schemas
import crud
import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI(title="API Inventario")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

models.Base.metadata.create_all(bind=database.engine)

# ---------------------- ENDPOINTS ----------------------

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>API PASA</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding-top: 50px; }
                h1 { color: #2c3e50; }
            </style>
        </head>
        <body>
            <h1>API de la Aplicación PASA - Python Version</h1>
            <p>El servicio se encuentra activo y funcionando correctamente.</p>
            <a href="/docs" style="color: #3498db;">Ver Documentación Interactiva (Swagger)</a>
        </body>
    </html>
    """

@app.get("/api/bodegas", response_model=List[schemas.Bodega])
def obtener_bodegas(db: Session = Depends(database.get_db)):
    data = crud.obtener_bodegas(db)
    return [dict(row._mapping) for row in data]

@app.get("/api/productos", response_model=List[schemas.Producto])
def obtener_productos(skip: int = 0, limit: int = 10000, db: Session = Depends(database.get_db)):
    data = crud.obtener_productos_paginado(db, skip=skip, limit=limit)
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

@app.get("/api/productos/total")
def contar_productos(db: Session = Depends(database.get_db)):
    # CORRECCIÓN: Envolver el string en text()
    query = text("SELECT COUNT(*) as total FROM control_inventarios.w_productos")
    result = db.execute(query).first()
    return {"total": result[0]}


# ---------------------- SERVIDOR ----------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)