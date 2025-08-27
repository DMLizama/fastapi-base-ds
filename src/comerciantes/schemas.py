from pydantic import BaseModel, field_validator
from src.comerciantes.exceptions import TipoComercianteInvalido #únicamente importo la excepción para "laburar lo más atómico posible, porque hay archivos que son muy grandes como para andar trayendolos todos"
from src.comerciantes.models import TipoComerciante

class ComercianteBase (BaseModel):
    nombre: str
    tipo: TipoComerciante

    @field_validator("tipo", mode="before") #validar tipoComerciante antes para que no venga cualquier cosa
    @classmethod
    def is_valid_tipo_comerciante(cls, v: str) -> str:
        if v.lower() not in TipoComerciante:
            raise TipoComercianteInvalido(list(TipoComerciante))
        return v.lower()

    
class ComercianteCreate(ComercianteBase):
    pass

class ComercianteUpdate(ComercianteBase):
    id: int

class ComercianteDelete(ComercianteBase):
    id: int

class Comerciante(ComercianteBase):
    pass
