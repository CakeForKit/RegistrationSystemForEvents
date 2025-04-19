from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, field_validator


class Event(BaseModel):
    id: UUID
    evname: str
    evdate: datetime
    place: str
    evdescription: str

    @field_validator("evname")
    def evname_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("evname не может быть пустым.")
        return value

    @field_validator("place")
    def place_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("place не может быть пустым.")
        return value

    @field_validator("evdescription")
    def description_max_length(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("value не может быть пустым.")
        if len(value) > 500:
            raise ValueError("value не может быть длиннее 500 символов.")
        return value
