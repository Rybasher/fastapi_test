from pydantic import BaseModel,  validator
from datetime import date
from database import EnumChoice
from fastapi import HTTPException


# Создаем pydantic модель
class User(BaseModel):
    user_name: str
    email: str
    password: str
    status: str = "active"
    created_at: date
    updated_at: date = None

    @validator('status')
    def status_validate(cls, status_value):
        # breakpoint()
        choice_list = [EnumChoice.active.value, EnumChoice.inactive.value, EnumChoice.deleted.value]
        if status_value not in choice_list:
            raise (HTTPException(status_code=500, detail="invalid status, use ('active', 'inactive', 'deleted')"))
        return status_value




