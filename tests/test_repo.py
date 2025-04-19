import uuid
from datetime import datetime

import pytest_asyncio, pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models.event import Event
from models.user import User
from models.tg import TG
from storage.storage import Storage

DATABASE_URL = "postgresql+asyncpg://puser:ppassword@postgres_test:5436/regSysEvents"


@pytest_asyncio.fixture
async def session():
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)
    async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session_maker() as session:
        yield session

    await engine.dispose() 


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

@pytest_asyncio.fixture
async def test_tg(test_user):
    tg_data = TG(
        user_id=test_user.id,
        tgID=12637,
        tg_name="@kkjjjj"
    )
    return tg_data


# Тест для создания пользователя
@pytest.mark.asyncio
async def test_create_user(storage, test_user):
    created_user = await storage.create_user(test_user)
    assert created_user.id == test_user.id
    assert created_user.name == "John"
    assert created_user.surname == "Doe"

@pytest.mark.asyncio
async def test_create_event(storage: Storage, test_event: Event):
    created_event = await storage.create_event(test_event)
    assert created_event.id == test_event.id
    assert created_event.evname == test_event.evname
    assert created_event.evdate == test_event.evdate
    assert created_event.place == test_event.place
    assert created_event.evdescription == test_event.evdescription

