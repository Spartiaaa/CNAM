# api/v1/hotel_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from schemas.chambre_schema import ChambreCreate, ChambreInDB
from services.chambre_service import ChambreService

# Un seul router
routeur = APIRouter(
    prefix="/chambres",
    tags=["Chambres"]
)
chambre_service = ChambreService()

@routeur.post("/", response_model=ChambreInDB)  # "/" car le prefix est déjà "/chambres"
def create_chambre(chambre: ChambreCreate, db: Session = Depends(get_db)):
    new_chambre = chambre_service.create_chambre(db=db, chambre=chambre)
    return new_chambre

@routeur.get("/{hotel_id}/chambre", response_model=List[ChambreInDB])
def list_rooms_by_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return chambre_service.list_rooms_by_hotel(db=db, hotel_id=hotel_id)

