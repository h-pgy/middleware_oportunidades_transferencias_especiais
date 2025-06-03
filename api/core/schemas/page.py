from pydantic import BaseModel
from .plano_acao import PlanoAcaoBase

class BasePage(BaseModel):
    """
    Model for paginated responses.
    """
    total: int
    skip: int
    limit: int
    data: list[BaseModel]

class PlanoBasePage(BasePage):
    """
    Model for paginated response of action plans.
    """
    data: list[PlanoAcaoBase]
    