-- Active: 1745059584062@@127.0.0.1@5434@regSysEvents
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES


select id ,name, surname, papname, groupVuz 
from users 
WHERE id='a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'  

-- Получение информации обо всех events в которых зарегестрирован user по id
SELECT e.id, 
FROM event e
JOIN user_event ue ON e.id = ue.event_id
WHERE ue.user_id = 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11';

-- Получение user по tg_id
SELECT 
    u.id, 
    u.name, 
    u.surname, 
    u.papname, 
    u.groupvuz, 
    ua.age, 
    ul.is_laptop,
    tg.tg_name,
    tg.tgID
FROM users u
JOIN userage ua ON u.id = ua.user_id
JOIN userislaptop ul ON u.id = ul.user_id
JOIN tgdata tg ON u.id = tg.user_id;
