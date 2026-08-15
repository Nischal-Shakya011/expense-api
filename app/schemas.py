from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    description: str | None

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: str
    
model_config = {
   "from_attributes": True 
}