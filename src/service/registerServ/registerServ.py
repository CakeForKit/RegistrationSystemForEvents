from typing import List, Optional
from uuid import UUID
from models.user import User, FullUserInfo
from models.event import Event


class RegisterServ:
    async def get_all_events(self) -> List[Event]:
        