from typing import Optional
from uuid import UUID

from pydantic import BaseModel, field_validator


class TG(BaseModel):
    user_id: UUID
    tgID: int
    tg_name: str

    @field_validator("tg_name")
    def tg_name_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("tg_name не может быть пустым.")
        return value
