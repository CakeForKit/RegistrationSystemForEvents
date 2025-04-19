import uuid
from datetime import datetime

import pytest_asyncio, pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models.event import Event
from models.user import User
from storage.storage import Storage

DATABASE_URL = "postgresql+asyncpg://puser:ppassword@postgres_container:5434/regSysEvents"



engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def session():
    async with SessionLocal() as session:
        yield session


@pytest_asyncio.fixture
async def storage(session):
    return Storage(session)


@pytest_asyncio.fixture
async def test_user():
    user_data = User(
        id=uuid.uuid4(),
        name="John",
        surname="Doe",
        papname="Johnny",
        groupVuz="Computer Science",
    )
    return user_data


@pytest_asyncio.fixture
async def test_event():
    event_data = Event(
        id=uuid.uuid4(),
        evname="Tech Conference",
        evdate=datetime(2023, 10, 10, 12, 30),
        place="Conference Hall",
        evdescription="A great tech conference",
    )
    return event_data


# Тест для создания пользователя
@pytest.mark.asyncio
async def test_create_user(storage, test_user):
    created_user = await storage.create_user(test_user)
    assert created_user.id == test_user.id
    assert created_user.name == "John"
    assert created_user.surname == "Doe"


# # Тест для получения пользователя по tg_id
# @pytest_asyncio.mark.asyncio
# async def test_get_user_by_tg_id(storage, test_user):
#     tg_id = 12345  # Пример tg_id
#     # Запишем пользователя в базу данных (это должно быть выполнено до запроса)
#     await storage.create_user(test_user)

#     # Выполним запрос
#     result = await storage.get_user_by_tg_id(tg_id)
#     assert result is not None
#     assert result.name == "John"
#     assert result.surname == "Doe"


# # Тест для создания события
# @pytest_asyncio.mark.asyncio
# async def test_create_event(storage, test_event):
#     created_event = await storage.create_event(test_event)
#     assert created_event.id == test_event.id
#     assert created_event.evname == "Tech Conference"
#     assert created_event.place == "Conference Hall"


# # Тест для регистрации пользователя на событие
# @pytest_asyncio.mark.asyncio
# async def test_register_user_for_event(storage, test_user, test_event):
#     # Создаем пользователя и событие
#     created_user = await storage.create_user(test_user)
#     created_event = await storage.create_event(test_event)

#     # Регистрируем пользователя на событие
#     success = await storage.register_user_for_event(created_user.id, created_event.id)
#     assert success is True

#     # Проверяем, что регистрация прошла
#     registrations = await storage.get_user_registrations(created_user.id)
#     assert len(registrations) == 1
#     assert registrations[0].id == created_event.id


# # Тест для отмены регистрации
# @pytest_asyncio.mark.asyncio
# async def test_cancel_registration(storage, test_user, test_event):
#     # Создаем пользователя и событие
#     created_user = await storage.create_user(test_user)
#     created_event = await storage.create_event(test_event)

#     # Регистрируем пользователя на событие
#     await storage.register_user_for_event(created_user.id, created_event.id)

#     # Отменяем регистрацию
#     await storage.cancel_registration(created_user.id, created_event.id)

#     # Проверяем, что регистрация отменена
#     registrations = await storage.get_user_registrations(created_user.id)
#     assert len(registrations) == 0
