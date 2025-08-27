from typing import List
from src.comerciantes.constants import ErrorCode
from src.exceptions import NotFound, BadRequest

class ComercianteNoEncontrado(NotFound):
    DETAIL = ErrorCode.COMERCIANTE_NO_ENCONTRADO

class NombreDuplicado(BadRequest):
    DETAIL = ErrorCode.NOMBRE_DUPLICADO

class TipoComercianteInvalido(ValueError):
    def __init__(self, posibles_tipos: List[str]): #constructor que recibe una lista de posible tipos de comerciante
        posibles_tipos = ", ".join(posibles_tipos)
        message = f"{ErrorCode.TIPO_COMERCIANTE_INVALIDO} {posibles_tipos}"
        super().__init__(message)
