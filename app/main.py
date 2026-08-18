# python -m uvicorn app.main:app --reload    (to run project)
from fastapi import Depends, FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.models import Expense
from app.schemas import ExpenseCreate, ExpenseResponse, ExpenseUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Expense API is running"}


# @app.get("/expenses")
# def get_expenses():
#     return [
#         {"id": 1, "title": "Lunch", "amount": 500},
#         {"id": 2, "title": "Taxi", "amount": 300},
#         {"id": 3, "title": "Coffee", "amount": 150},
#     ]


# @app.post("/expenses", response_model=ExpenseResponse)
# def create_expense(expense: ExpenseCreate):
#     return {
#         "id": 1,
#         "title": expense.title,
#         "amount": expense.amount,
#         "category": expense.category,
#         "description": expense.description,
#     }

# @app.get("/expenses/search")
# def search_expenses(category: str):
#     return {"category": category}


# @app.get("/expenses/{expense_id}")
# def get_expense(expense_id: int):
#     return {"id": expense_id, "message": "Expense found"}


# ---------------------------GET-------------------------------------------
@app.get("/expenses", response_model=list[ExpenseResponse])
def get_expenses(
    db: Session = Depends(get_db),
):
    expenses = db.query(Expense).all()
    return expenses


# ---------------------------GET BY ID-------------------------------------------
@app.get(
    "/expenses/{expense_id}",
    response_model=ExpenseResponse,
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found",
        )

    return expense


# ---------------------------POST-------------------------------------------
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
        description=expense.description,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


# ---------------------------PATCH-------------------------------------------
@app.patch("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
):
    existing_expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if existing_expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found",
        )
    update_data = expense.model_dump(exclude_unset=True)

    # equivalent to - existing_expense.amount = 150
    for field, value in update_data.items():
        setattr(existing_expense, field, value)

        db.commit()
        db.refresh(existing_expense)

    return existing_expense


# ---------------------------DELETE-------------------------------------------
@app.delete(
    "/expenses/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if expense is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Expense with id {expense_id} not found",
        )

    db.delete(expense)
    db.commit()

    return expense
