from pydantic import BaseModel

class ChambreBase(BaseModel):
    numero: int
    type: str
    prix : float
    etat : str
    hotel_id : int

class ChambreCreate(ChambreBase):
    pass

class ChambreInDB(ChambreBase):
    id : int
    model_config = {
        "from_attributes": True
    }