from sqlalchemy import Float, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(255),
    )

    expenses: Mapped[list["Expense"]] = relationship(
        back_populates="user",
    )
    
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
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    
    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    user: Mapped["User"] = relationship(
        back_populates="expenses",
    )