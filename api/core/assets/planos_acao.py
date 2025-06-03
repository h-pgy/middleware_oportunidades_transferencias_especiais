from core.utils.cache import cache_property

from core.extract import list_planos_acao
from core.transform import get_status_planos_acao

@cache_property('all_planos_acao')
def all_planos_acao()->list[dict]:
    """
    Fetch all action plans.
    """
    planos = list_planos_acao(all=True)
    return planos['listaPlanosAcao']