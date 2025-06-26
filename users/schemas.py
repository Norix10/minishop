from pydantic import BaseModel, EmailStr, Field

class CreateUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: str | None = None