from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(100),
    )

    amount: Mapped[float] = mapped_column(
        Float,
    )

    category: Mapped[str] = mapped_column(
        String(50),
    )