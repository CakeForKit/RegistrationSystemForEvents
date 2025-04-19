from uuid import UUID

from pydantic import BaseModel


class UserIsLaptop(BaseModel):
    user_id: UUID
    is_laptop: bool = False
