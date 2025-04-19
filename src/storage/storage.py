from __future__ import annotations

from typing import List, Optional
from uuid import UUID
from models.user import User, FullUserInfo
from models.event import Event


from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession


class Storage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all_events(self) -> List[Event]:
        query = text("""
            SELECT id, evname, evdate, place, evdescription
            FROM event
        """)

        try:
            result = await self.session.execute(query)
            rows = result.mappings().all()

            events = [
                Event(
                    id=row["id"],
                    evname=row["evname"],
                    evdate=row["evdate"],
                    place=row["place"],
                    evdescription=row["evdescription"]
                )
                for row in rows
            ]
            return events

        except Exception as e:
            print(f"Ошибка при получении событий: {e}")
            return []

    async def create_user(self, user_data: User) -> User:
        try:
            insert_user_query = text("""
                INSERT INTO users (id, name, surname, papname, groupVuz)
                VALUES (:id, :name, :surname, :papname, :groupVuz)
            """)
            await self.session.execute(insert_user_query, {
                "id": str(user_data.id),
                "name": user_data.name,
                "surname": user_data.surname,
                "papname": user_data.papname,
                "groupVuz": user_data.groupVuz
            })

            await self.session.commit()
            return user_data

        except SQLAlchemyError as e:
            await self.session.rollback()
            print(f"Ошибка при создании пользователя: {e}")
            raise

    async def get_user_by_tg_id(self, tg_id: int) -> Optional[FullUserInfo]:
        query = text("""
            SELECT u.id, u.name, u.surname, u.papname, u.groupvuz,
                ua.age, ul.is_laptop, tg.tg_name
            FROM users u
            JOIN userage ua ON u.id = ua.user_id
            JOIN userislaptop ul ON u.id = ul.user_id
            JOIN tgdata tg ON tg.user_id = u.id
            WHERE tg.tgID = :tg_id
        """)
        try:
            result = await self.session.execute(query, {"tg_id": tg_id})
            row = result.mappings().first()
            if row:
                return FullUserInfo(
                    id=row["id"],
                    name=row["name"],
                    surname=row["surname"],
                    papname=row["papname"],
                    groupVuz=row["groupvuz"],
                    age=row["age"],
                    is_laptop=row["is_laptop"],
                    tg_name=row["tg_name"]
                )
            return None
        except SQLAlchemyError as e:
            print(f"Ошибка при получении пользователя по tg_id: {e}")
            return None

    async def get_user_events(self, user_id: UUID) -> List[Event]:
        query = text("""
            SELECT e.id, e.evname, e.evdate, e.place, e.evdescription
            FROM event e
            JOIN user_event ue ON ue.event_id = e.id
            WHERE ue.user_id = :user_id
        """)

        try:
            result = await self.session.execute(query, {"user_id": str(user_id)})
            rows = result.fetchall()

            return [
                Event(
                    id=row[0],
                    evname=row[1],
                    evdate=row[2],
                    place=row[3],
                    evdescription=row[4]
                )
                for row in rows
            ]
        except SQLAlchemyError as e:
            print(f"Ошибка при получении регистраций пользователя: {e}")
            return []
        
    async def get_all_fields_user(self, tg_id: int) -> Optional[FullUserInfo]:
        return self.get_user_by_tg_id(tg_id)

    async def get_fields_for_event():
        return ["a", "f", "g"]

    async def register_user_for_event(self, user_id: UUID, event_id: UUID) -> bool:
        query = text("""
            INSERT INTO user_event (id, user_id, event_id)
            VALUES (gen_random_uuid(), :user_id, :event_id)
        """)

        try:
            await self.session.execute(query, {
                "user_id": str(user_id),
                "event_id": str(event_id)
            })
            await self.session.commit()
            return True

        except SQLAlchemyError as e:
            print(f"Ошибка при регистрации пользователя на событие: {e}")
            await self.session.rollback()
            return False

    # async def update_user_fields():
    #     pass

    async def update_user(self, update_user: FullUserInfo) -> Optional[FullUserInfo]:
        try:
            query_users = text("""
                UPDATE users
                SET name = :name, surname = :surname, papname = :papname, groupVuz = :groupVuz
                WHERE id = :id
            """)
            await self.session.execute(query_users, {
                "id": update_user.id,
                "name": update_user.name,
                "surname": update_user.surname,
                "papname": update_user.papname,
                "groupVuz": update_user.groupVuz
            })

            query_age = text("""
                UPDATE userAge
                SET age = :age
                WHERE user_id = :id
            """)
            await self.session.execute(query_age, {
                "id": update_user.id,
                "age": update_user.age
            })

            query_is_laptop = text("""
                UPDATE userIsLaptop
                SET is_laptop = :is_laptop
                WHERE user_id = :id
            """)
            await self.session.execute(query_is_laptop, {
                "id": update_user.id,
                "is_laptop": update_user.is_laptop
            })

            await self.session.commit()
            return update_user
        except SQLAlchemyError as e:
            print(f"Ошибка при обновлении пользователя: {e}")
            await self.session.rollback()
            return None
        
    async def cancel_registration(self, user_id: UUID, event_id: UUID) -> None:
        query = text("""
            DELETE FROM user_event
            WHERE user_id = :user_id AND event_id = :event_id
        """)

        try:
            await self.session.execute(query, {
                "user_id": str(user_id),
                "event_id": str(event_id)
            })
            await self.session.commit()

        except SQLAlchemyError as e:
            print(f"Ошибка при отмене регистрации пользователя: {e}")
            await self.session.rollback()



