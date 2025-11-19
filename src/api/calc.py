from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from src.schemas.calc import CalcResponse
from src.services.calc import get_product_cost

router = APIRouter(tags=["Calculation"])
router.add_api_route(
    path="/calc",
    endpoint=get_product_cost,
    response_model=CalcResponse,
    methods=["POST"],
    status_code=HTTP_201_CREATED,
)