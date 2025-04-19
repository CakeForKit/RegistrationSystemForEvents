from dataclasses import dataclass
from typing import ClassVar, Optional
from uuid import UUID

from pydantic import BaseModel, field_validator


class User(BaseModel):
    id: UUID
    name: str
    surname: str
    papname: str
    groupVuz: str
    tgID: Optional[int] = None

    @field_validator("name")
    def name_not_empty_string(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Поля name не могут быть пустыми.")
        return value

    @field_validator("surname")
    def surname_not_empty_string(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Поля surname не могут быть пустыми.")
        return value

    @field_validator("papname")
    def name_not_empty_string(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Поля papname не могут быть пустыми.")
        return value

    @field_validator("groupVuz")
    def name_not_empty_string(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Поля groupVuz не могут быть пустыми.")
        return value

    @field_validator("tgID")
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
