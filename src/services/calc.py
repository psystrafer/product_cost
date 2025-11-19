from decimal import Decimal

from src.clients.db import AsyncSession
from src.db.calc_result import CalcResult
from src.schemas.calc import CalcResponse, CalcRequest


async def get_product_cost(request: CalcRequest, session: AsyncSession):
    total_cost = sum(m.qty * m.price for m in request.materials)
    total_cost_rounded = total_cost.quantize(Decimal("0.00"))
    async with session.begin() as s:
        s.add(CalcResult(total_cost_rub=total_cost_rounded))
    return CalcResponse(total_cost_rub=Decimal(total_cost_rounded))
