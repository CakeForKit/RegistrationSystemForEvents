-- Active: 1745059584062@@127.0.0.1@5434@regSysEvents
-- Заполнение таблицы users
INSERT INTO users (id, name, surname, papname, groupVuz) VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Иван', 'Иванов', 'Иванович', 'ИТ-101'),
('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'Петр', 'Петров', 'Петрович', 'ИТ-102'),
('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'Анна', 'Сидорова', 'Алексеевна', 'ИТ-103');

-- Заполнение таблицы userAge
INSERT INTO userAge (user_id, age) VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 20),
('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 21),
('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 19);

-- Заполнение таблицы userIsLaptop
INSERT INTO userIsLaptop (user_id, is_laptop) VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', TRUE),
('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', FALSE),
('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', TRUE);

-- Заполнение таблицы event
INSERT INTO event (id, evname, evdate, place, evdescription) VALUES
('d3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'Хакатон 2025', '2025-05-15 10:00:00', 'Главный корпус, ауд. 101', 'Годовой хакатон для студентов IT-специальностей'),
('e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'Научная конференция', '2025-06-20 09:30:00', 'Конференц-зал', 'Межвузовская научная конференция'),
('f5eebc99-9c0b-4ef8-bb6d-6bb9bd380a16', 'Встреча выпускников', '2025-07-10 18:00:00', 'Актовый зал', 'Ежегодная встреча выпускников университета');

-- Заполнение таблицы user_event
INSERT INTO user_event (id, user_id, event_id) VALUES
('11111111-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'd3eebc99-9c0b-4ef8-bb6d-6bb9bd380a14'),
('22222222-9c0b-4ef8-bb6d-6bb9bd380a12', 'b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15'),
('33333333-9c0b-4ef8-bb6d-6bb9bd380a13', 'c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'f5eebc99-9c0b-4ef8-bb6d-6bb9bd380a16'),
('44444444-9c0b-4ef8-bb6d-6bb9bd380a14', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'e4eebc99-9c0b-4ef8-bb6d-6bb9bd380a15');

INSERT INTO tgdata (user_id, tgID, tg_name) VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 123456789, 'ivan_ivanov'),
('b1eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 987654321, 'petr_petrov'),
('c2eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 555666777, 'anna_sid');