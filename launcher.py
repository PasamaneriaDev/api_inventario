# launcher.py
import os
import sys

# Importa tu app desde main.py
from main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 3000))  # Puedes cambiar el puerto si quieres
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info",
        reload=False  # reload debe ser False para exe
    )
