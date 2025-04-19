from pydantic import BaseModel, Field

from uuid import UUID
from typing import Optional


class UserIsLaptop(BaseModel):
    user_id: UUID
    is_laptop: bool = False
