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

@cache_property('planos_acao_benficiario_default')
def planos_acao_beneficiario_default() -> list[dict]:
    """
    Fetch action plans for a specific beneficiary.
    """
    planos = list_planos_acao(all=False)
    return planos['listaPlanosAcao']

@cache_property('status_planos_acao')
def status_planos_acao_all() -> dict:
    """
    Get the status of all action plans.
    """
    planos = all_planos_acao()
    return get_status_planos_acao(planos)

@cache_property('status_planos_acao_beneficiario_default')
def status_planos_acao_beneficiario_default() -> dict:
    """
    Get the status of action plans for a specific beneficiary.
    """
    planos = planos_acao_beneficiario_default()
    return get_status_planos_acao(planos)