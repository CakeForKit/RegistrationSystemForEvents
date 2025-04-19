from typing import List, Optional
from uuid import UUID

from models.event import Event
from models.user import User, FullUserInfo
from storage.storage import BaseStorage


class RegisterServ:

    def __init__(self, storage : BaseStorage):
        self.stogare = storage

    async def get_all_events(self) -> List[Event]:
        return self.stogare.get_all_events()

    async def create_user(self, user_data: User) -> User:
        return self.stogare.create_user(user_data)

    async def get_user_by_tg_id(self, tg_id: int) -> Optional[FullUserInfo]:
        return self.stogare.get_user_by_tg_id(tg_id)

    async def get_user_events(self, user_id: UUID) -> List[Event]:
        return self.stogare.get_user_events(user_id)

    async def get_all_fields_user(self, tg_id: int) -> Optional[FullUserInfo]:
        return self.stogare.get_all_fields_user(tg_id)

    async def get_fields_for_event(self) -> List[str]:
        return self.stogare.get_fields_for_event()

    async def register_user_for_event(self, user_id: UUID, event_id: UUID) -> bool:
        return self.stogare.register_user_for_event(user_id, event_id)

    async def update_user(self, update_user: FullUserInfo) -> Optional[FullUserInfo]:
        return self.stogare.update_user(update_user)

    async def cancel_registration(self, user_id: UUID, event_id: UUID) -> None:
        return self.stogare.cancel_registration(user_id, event_id)
