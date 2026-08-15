from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Expense API is running"}


@app.get("/")
def home():
    return {"message": "Expense API is running"}


@app.get("/expenses")
def get_expenses():
    return [
        {"id": 1, "title": "Lunch", "amount": 500},
        {"id": 2, "title": "Taxi", "amount": 300},
        {"id": 3, "title": "Coffee", "amount": 150},
    ]


# @app.post("/expenses", response_model=ExpenseResponse)
# def create_expense(expense: ExpenseCreate):
#     return {
#         "id": 1,
#         "title": expense.title,
#         "amount": expense.amount,
#         "category": expense.category,
#         "description": expense.description,
#     }


@app.post(
    "/expenses",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


@app.get("/expenses/search")
def search_expenses(category: str):
    return {"category": category}


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    return {"id": expense_id, "message": "Expense found"}
