import uuid
from datetime import datetime

import pytest_asyncio
import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from models.event import Event
from models.user import User, FullUserInfo
from models.tg import TG
from storage.storage import Storage

DATABASE_URL = "postgresql+asyncpg://puser:ppassword@postgres_test:5432/regSysEventsTest"

@pytest_asyncio.fixture(scope="function")
async def session():
    engine = create_async_engine(DATABASE_URL, echo=True)
    
    # Создаем все таблицы
    async with engine.begin() as conn:
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                name VARCHAR(127) NOT NULL,
                surname VARCHAR(127) NOT NULL,
                papname VARCHAR(127) NOT NULL,
                groupVuz VARCHAR(127) NOT NULL
            )
        """))
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS userAge (
                user_id UUID PRIMARY KEY REFERENCES users(id),
                age INT CHECK (age > 0)
            )
        """))
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS userIsLaptop (
                user_id UUID PRIMARY KEY REFERENCES users(id),
                is_laptop BOOLEAN NOT NULL DEFAULT FALSE
            )
        """))
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS event (
                id UUID PRIMARY KEY,
                evname VARCHAR(255) NOT NULL UNIQUE,
                evdate TIMESTAMP NOT NULL,
                place TEXT NOT NULL,
                evdescription TEXT NOT NULL
            )
        """))
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS user_event (
                id UUID PRIMARY KEY,
                user_id UUID REFERENCES users(id),
                event_id UUID REFERENCES event(id)
            )
        """))
        await conn.execute(text("""
            CREATE TABLE IF NOT EXISTS tgdata (
                user_id UUID PRIMARY KEY REFERENCES users(id),
                tgID BIGINT NOT NULL,
                tg_name VARCHAR(127) NOT NULL
            )
        """))
        await conn.commit()

    async_session_maker = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session_maker() as session:
        await session.execute(text("TRUNCATE TABLE tgdata, user_event, event, userIsLaptop, userAge, users CASCADE"))

        await session.execute(text("""
            INSERT INTO users (id, name, surname, papname, groupVuz) VALUES
            ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Иван', 'Иванов', 'Иванович', 'ИТ-101'),
            ('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'Петр', 'Петров', 'Петрович', 'ИТ-102'),
            ('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'Анна', 'Сидорова', 'Алексеевна', 'ИТ-103')
        """))
        
        await session.execute(text("""
            INSERT INTO userAge (user_id, age) VALUES
            ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 20),
            ('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 21),
            ('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 19)
        """))
        
        await session.execute(text("""
            INSERT INTO userIsLaptop (user_id, is_laptop) VALUES
            ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', TRUE),
            ('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', FALSE),
            ('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', TRUE)
        """))
        
        await session.execute(text("""
            INSERT INTO event (id, evname, evdate, place, evdescription) VALUES
            ('d3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'Хакатон 2025', '2025-05-15 10:00:00', 'Главный корпус, ауд. 101', 'Годовой хакатон для студентов IT-специальностей'),
            ('e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'Научная конференция', '2025-06-20 09:30:00', 'Конференц-зал', 'Межвузовская научная конференция'),
            ('f5eebc99-9c0b-4ef8-bb6d-6bb9bd380a16', 'Встреча выпускников', '2025-07-10 18:00:00', 'Актовый зал', 'Ежегодная встреча выпускников университета')
        """))
        
        await session.execute(text("""
            INSERT INTO user_event (id, user_id, event_id) VALUES
            ('11111111-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14'),
            ('22222222-9c0b-4ef8-bb6d-6bb9bd380a12', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15'),
            ('33333333-9c0b-4ef8-bb6d-6bb9bd380a13', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'f5eebc99-9c0b-4ef8-bb6d-6bb9bd380a16'),
            ('44444444-9c0b-4ef8-bb6d-6bb9bd380a14', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15')
        """))
        
        await session.execute(text("""
            INSERT INTO tgdata (user_id, tgID, tg_name) VALUES
            ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 123456789, 'ivan_ivanov'),
            ('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 987654321, 'petr_petrov'),
            ('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 555666777, 'anna_sid')
        """))
        
        await session.commit()
        yield session

    # Очистка после всех тестов
    async with engine.begin() as conn:
        await conn.execute(text("DROP TABLE IF EXISTS tgdata, user_event, event, userIsLaptop, userAge, users CASCADE"))
        await conn.commit()
        
@pytest_asyncio.fixture
async def storage(session):
    return Storage(session)

@pytest_asyncio.fixture
async def test_user():
    return User(
        id=uuid.uuid4(),
        name="John",
        surname="Doe",
        papname="Johnny",
        groupVuz="Computer Science",
    )

@pytest_asyncio.fixture
async def test_event():
    return Event(
        id='d3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14',
        evname="Хакатон 2025",
        evdate=datetime(2025, 5, 15, 10, 00),
        place="Главный корпус, ауд. 101",
        evdescription="Годовой хакатон для студентов IT-специальностей"
    )

@pytest.mark.asyncio
async def test_create_user(storage, session, test_user):
    created_user = await storage.create_user(test_user)
    
    result = await session.execute(
        text("SELECT * FROM users WHERE id = :id"),
        {"id": str(test_user.id)}
    )
    user = result.fetchone()
    
    assert user is not None
    assert user[1] == "John"
    assert user[2] == "Doe"

@pytest.mark.asyncio
async def test_get_user_by_tg_id(storage):
    existing_tg_id = 123456789
    user = await storage.get_user_by_tg_id(existing_tg_id)
    assert user is not None
    assert user.id == uuid.UUID("a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11")
    assert user.tg_name == "ivan_ivanov"
    
    non_existent_tg_id = 999999999
    user = await storage.get_user_by_tg_id(non_existent_tg_id)
    assert user is None


@pytest.mark.asyncio
async def test_create_event(storage, session, test_event):
    result = await session.execute(
        text("SELECT * FROM event WHERE id = :id"),
        {"id": str(test_event.id)}
    )
    event = result.fetchone()
    
    assert event is not None
    assert event[1] == "Хакатон 2025"


@pytest.mark.asyncio
async def test_get_user_events(storage):
    user_id = uuid.UUID("a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11")
    events = await storage.get_user_events(user_id)
    
    assert len(events) == 2
    event_names = {event.evname for event in events}
    assert "Хакатон 2025" in event_names
    assert "Научная конференция" in event_names

@pytest.mark.asyncio
async def test_register_user_for_event(storage, session, test_user):
    await storage.create_user(test_user)
    
    event_id = uuid.UUID("d3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14")
    result = await storage.register_user_for_event(test_user.id, event_id)
    assert result is True
    
    query = text("""
        SELECT * FROM user_event 
        WHERE user_id = :user_id AND event_id = :event_id
    """)
    result = await session.execute(query, {
        "user_id": str(test_user.id),
        "event_id": str(event_id)
    })
    assert result.fetchone() is not None
    
    invalid_event_id = uuid.UUID("d3eebc99-9c0b-4ef8-bb6d-6bb9bd383c99")
    result = await storage.register_user_for_event(test_user.id, invalid_event_id)
    assert result is False

@pytest.mark.asyncio
async def test_update_user(storage, session):
    user_id = uuid.UUID("a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11")
    updated_data = FullUserInfo(
        id=user_id,
        name="Михаил",
        surname="Петров",
        papname="Сергеевич",
        groupVuz="ИТ-201",
        age=22,
        is_laptop=False,
        tg_name="ivan_ivanov"
    )
    
    result = await storage.update_user(updated_data)
    assert result == updated_data
    
    user_query = text("SELECT * FROM users WHERE id = :id")
    user_result = await session.execute(user_query, {"id": str(user_id)})
    user_row = user_result.fetchone()
    assert user_row[1:] == ("Михаил", "Петров", "Сергеевич", "ИТ-201")
    
    age_query = text("SELECT age FROM userAge WHERE user_id = :id")
    age = await session.scalar(age_query, {"id": str(user_id)})
    assert age == 22
    
    laptop_query = text("SELECT is_laptop FROM userIsLaptop WHERE user_id = :id")
    is_laptop = await session.scalar(laptop_query, {"id": str(user_id)})
    assert is_laptop is False

@pytest.mark.asyncio
async def test_cancel_registration(storage, session):
    user_id = uuid.UUID("a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11")
    event_id = uuid.UUID("d3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14")
    
    query = text("""
        SELECT * FROM user_event 
        WHERE user_id = :user_id AND event_id = :event_id
    """)
    result = await session.execute(query, {
        "user_id": str(user_id),
        "event_id": str(event_id)
    })
    assert result.fetchone() is not None
    
    await storage.cancel_registration(user_id, event_id)
    
    result = await session.execute(query, {
        "user_id": str(user_id),
        "event_id": str(event_id)
    })
    assert result.fetchone() is None