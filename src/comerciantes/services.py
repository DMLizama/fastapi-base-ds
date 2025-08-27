from typing import List
from sqlalchemy import select#, update, delete DESCOMENTAR PARA IMPLEMENTAR
from sqlalchemy.orm import Session
from src.comerciantes import schemas
from src.comerciantes.models import Comerciante
#crear funciones de servicios para crear comerciantes, y otro para listar todos los comerciantes creados.
#seguir con routers

def crear_comerciante(db: Session, comerciante: schemas.ComercianteCreate) -> schemas.Comerciante:
    _comerciante = Comerciante(**comerciante.model_dump())
    db.add(_comerciante)
    db.commit()
    db.refresh(_comerciante)
    return _comerciante

def listar_comerciantes(db: Session) -> List[schemas.Comerciante]:
    return db.scalars(select(Comerciante)).all()

