from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from typing import List
import database
import schemas
import crud
import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="API Inventario")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crea tablas si no existen
models.Base.metadata.create_all(bind=database.engine)

# ---------------------- ENDPOINTS ----------------------
# Esto es lo que verás al entrar a http://www.api.pasa.ec/
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
    uvicorn.run(app, host="0.0.0.0", port=3000)
