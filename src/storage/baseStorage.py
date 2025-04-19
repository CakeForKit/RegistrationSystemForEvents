from models import user
from models import event
from models import user_age
from models import user_is_laptop
from models.user import User, FullUserInfo
from models.event import Event
from uuid import UUID
from typing import List, Optional
# Deep seek  поделал глянь   get_events(self, filters: dict = None) тут какой-то фильтр ВТФ)))
class BaseStorage:
    async def get_all_events(self) -> List[Event]:
        raise NotImplementedError

    async def create_user(self, user_data: User) -> User:
        raise NotImplementedError

    async def get_user_by_tg_id(self, tg_id: int) -> Optional[FullUserInfo]:
        raise NotImplementedError

    async def get_user_events(self, user_id: UUID) -> List[Event]:
        raise NotImplementedError
    
    async def get_all_fields_user(self, tg_id: int) -> Optional[FullUserInfo]:
        raise NotImplementedError

    async def get_fields_for_event() -> List[str]:
        raise NotImplementedError

    async def register_user_for_event(self, user_id: UUID, event_id: UUID) -> bool:
        raise NotImplementedError
    
    async def update_user(self, update_user: FullUserInfo) -> Optional[FullUserInfo]:
        raise NotImplementedError
    
    async def cancel_registration(self, user_id: UUID, event_id: UUID) -> None:
        raise NotImplementedError
    
    # # User methods
    # #def get_user_by_id(self, user_id: UUID) -> Optional[user.User]:
    # #    raise NotImplementedError
        
    # def get_user_by_tg_id(self, tg_id: int) -> Optional[user.User]:
    #     raise NotImplementedError
        
    # def create_user(self, user_data: user.User) -> user.User:
    #     raise NotImplementedError
        
    # # def update_user(self, user_id: UUID, update_data: dict) -> user.User:
    # #    raise NotImplementedError
        
    # # Event methods
    # #def create_event(self, event_data: event.Event) -> event.Event: Не для участника
    # #    raise NotImplementedError
        
    # #def get_event_by_id(self, event_id: UUID) -> Optional[event.Event]:
    # #    raise NotImplementedError
        
    # def get_all_events(self) -> List[event.Event]:
    #     raise NotImplementedError

    # #def update_event(self, event_id: UUID, update_data: dict) -> event.Event: не для участника
    # #    raise NotImplementedError
        
    # #def delete_event(self, event_id: UUID) -> bool: не для участника
    # #    raise NotImplementedError
        
    # # Registration methods
    # def register_user_for_event(self, user_id: UUID, event_id: UUID) -> bool:
    #     raise NotImplementedError
        
    # def cancel_registration(self, user_id: UUID, event_id: UUID) -> bool:
    #     raise NotImplementedError
        
    # #def get_event_registrations(self, event_id: UUID) -> List[user.User]:
    # #    raise NotImplementedError
        
    # def get_user_registrations(self, user_id: UUID) -> List[event.Event]:
    #     raise NotImplementedError
        
    # # Additional user data methods
    # '''
    # def get_user_age(self, user_id: UUID) -> Optional[user_age.UserAge]:
    #     raise NotImplementedError
        
    # def set_user_age(self, user_id: UUID, age: int) -> user_age.UserAge:
    #     raise NotImplementedError
        
    # def get_user_laptop_preference(self, user_id: UUID) -> Optional[user_is_laptop.UserIsLaptop]:
    #     raise NotImplementedError
        
    # def set_user_laptop_preference(self, user_id: UUID, is_laptop: bool) -> user_is_laptop.UserIsLaptop:
    #     raise NotImplementedError
    #     '''

