from typing import Optional
from uuid import UUID

from pydantic import BaseModel, field_validator


class UserAge(BaseModel):
    user_id: UUID
    age: int

    @field_validator("age")
    def age_must_be_positive(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value <= 0:
            raise ValueError("age должен быть положительным числом.")
        return value
