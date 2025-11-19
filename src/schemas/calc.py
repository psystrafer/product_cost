from decimal import Decimal
from typing import List

from pydantic import BaseModel


class MaterialRequest(BaseModel):
    name: str
    qty: Decimal
    price: Decimal


class CalcRequest(BaseModel):
    materials: List[MaterialRequest]


class CalcResponse(BaseModel):
    total_cost_rub: Decimal
