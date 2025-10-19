from sqlalchemy.orm import Session
from models import Chambre
from schemas.chambre_schema import ChambreCreate, ChambreInDB

class ChambreService:
    def create_chambre(self, db: Session, chambre: ChambreCreate) -> ChambreInDB:
        new_chambre = Chambre(
            numero=chambre.numero,
            type=chambre.type,
            prix=chambre.prix,
            etat=chambre.etat,
            hotel_id=chambre.hotel_id,
        )
        db.add(new_chambre)
        db.commit()
        db.refresh(new_chambre)
        return new_chambre

    def list_rooms_by_hotel(self, db: Session, hotel_id: int):
            return (
                db.query(Chambre).filter(Chambre.hotel_id == hotel_id).all()
            )
    
