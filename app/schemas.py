from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    description: str | None = None

class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: str | None = None

class ExpenseUpdate(BaseModel):
    title: str | None = None
    amount: float | None = None
    category: str | None = None
      
model_config = {
   "from_attributes": True 
}