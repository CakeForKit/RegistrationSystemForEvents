from pydantic import BaseModel, Field

from uuid import UUID
from typing import Optional
from typing import ClassVar


class Event(BaseModel):
    id: UUID
    evname: ClassVar[int] = 255
    evdate: datetime
    place: str
    evdescription: str

    @validator('evname')
    def evname_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("evname не может быть пустым.")
        return value

    @validator('place')
    def evname_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("place не может быть пустым.")
        return value

    @validator('evdescription')
    def description_max_length(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("value не может быть пустым.")
        if len(value) > 500:
            raise ValueError("value не может быть длиннее 500 символов.")
        return value