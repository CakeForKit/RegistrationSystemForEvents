from pydantic import BaseModel, Field, validator

from uuid import UUID
from typing import Optional


class UserAge(BaseModel):
    user_id: UUID
    age: int

    @validator('age')
    def age_must_be_positive(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value <= 0:
            raise ValueError("age должен быть положительным числом.")
        return value
