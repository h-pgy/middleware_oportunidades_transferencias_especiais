from fastapi import APIRouter, Query, HTTPException

from typing import List, Optional

from core.assets.planos_acao import (
                        all_planos_acao,
                        planos_acao_beneficiario_default,
                        status_planos_acao_all,
                        status_planos_acao_beneficiario_default
                    )
from core.schemas.plano_acao import PlanoAcaoBase
from core.schemas.page import PlanoBasePage
from core.parsers import parse_plano_acao_basico

app = APIRouter()

@app.get('/planos-acao')
def get_all_planos_acao(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of records to return")
) -> PlanoBasePage:
    """
    Endpoint to get all action plans with pagination.
    """
    planos = all_planos_acao()
    paginated_planos = planos[skip:skip + limit]
    parsed = parse_plano_acao_basico(paginated_planos, to_pydantic=True)
    page = PlanoBasePage(
        total=len(planos),
        skip=skip,
        limit=limit,
        data=parsed
    )

    return page