from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class CalcResult(Base):

    __tablename__ = "calc_result"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    total_cost_rub: Mapped[Decimal] = mapped_column(nullable=False, default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
