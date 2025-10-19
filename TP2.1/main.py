from fastapi import FastAPI
from database.session import Base, engine
from api.v1.chambre_routeur import routeur as chambre_routeur
from api.v1.hotel_routeur import routeur as hotel_router

# Crée les tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hotel API")

# Inclut le router
app.include_router(hotel_router)
app.include_router(chambre_routeur)