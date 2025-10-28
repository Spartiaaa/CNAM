from fastapi import APIRouter, Depends, HTTPException, status

routeur = APIRouter(
    prefix="/"
)

@routeur.get("/")
def read_root():
    return {"message": "Bienvenue sur mon API FastAPI ! Aller sur '/docs' pour avoir accès à l'interface."}
