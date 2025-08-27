from sqlalchemy import Integer, String#, ForeignKey no llevan en este caso porque no tienen foránea de otro model
from sqlalchemy.orm import Mapped, mapped_column#, relationship
from enum import auto, StrEnum
from src.models import ModeloBase

class TipoComerciante(StrEnum):
    ROTISERIA = auto()
    PIZZERIA = auto()
    RESTAURANT = auto()

class Comerciante(ModeloBase):
    __tablename__ = "comerciantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String, index=True)
    tipo: Mapped[TipoComerciante] = mapped_column(String)
