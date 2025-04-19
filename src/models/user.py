from pydantic import BaseModel, Field

from uuid import UUID
from typing import Optional
from typing import ClassVar

from dataclasses import dataclass

class User(BaseModel):
    id: UUID
    name: ClassVar[int] = 127
    surname: ClassVar[int] = 127
    papname: ClassVar[int] = 127
    groupVuz: ClassVar[int] = 127
    tgID: Optional[int] = None

    @validator('name', 'surname', 'papname', 'groupVuz')
    def not_empty_string(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Поля не могут быть пустыми.")
        return value

    @validator('tgID')
    def tg_id_must_be_positive(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value <= 0:
            raise ValueError("tgID должен быть положительным числом.")
        return value



@dataclass
class FullUserInfo:
    id: UUID
    name: str
    surname: str
    papname: str
    groupVuz: str
    age: int
    is_laptop: bool
    tg_name: str