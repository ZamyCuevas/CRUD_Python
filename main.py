from fastapi import FastAPI
from routes.users import user
from routes.material import material
from routes.prestamo import prestamo

app = FastAPI(
    title="API",
    description="API con rutas de usuario, material y préstamo"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

# Incluir las rutas de usuario, material y préstamo
app.include_router(user)
app.include_router(material)
app.include_router(prestamo)
