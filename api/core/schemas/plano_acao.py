from pydantic import BaseModel
from typing import Literal, Optional

class FinalidadePlanoAcao(BaseModel):
    """
    Model for Finalidade do Plano de Ação.
    """
    codigo: str
    descricao: str

class ValoresPlanoAcao(BaseModel):
    tipo: Literal['custeio', 'investimento']
    valor: Optional[float]

class PlanoAcaoBase(BaseModel):
    """
    Base model for Plano de Ação.
    """
    id: int
    codigo_do_programa: str
    situacao: str
    finalidades: list[FinalidadePlanoAcao]
    uf: str
