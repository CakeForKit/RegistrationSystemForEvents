-- Active: 1745054944224@@127.0.0.1@5434@regSysEvents
-- +goose Up
-- +goose StatementBegin

CREATE TABLE IF NOT EXISTS users (
  id UUID PRIMARY KEY,
  name VARCHAR(127) NOT NULL,
  surname VARCHAR(127) NOT NULL,
  papname VARCHAR(127) NOT NULL,
  groupVuz VARCHAR(127) NOT NULL,
  tgID BIGINT
  -- tg_username VARCHAR(127),
);

CREATE TABLE IF NOT EXISTS userAge (
  user_id UUID PRIMARY KEY,
  age INT,
  CONSTRAINT age_positive CHECK (age > 0),
  CONSTRAINT tg_user_id FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS userIsLaptop (
  user_id UUID PRIMARY KEY,
<<<<<<< HEAD
  is_laptop BOOLEAN DEFAULT FALSE, 
  CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users (id),
=======
  is_laptop BOOLEAN DEFAULT FALSE,
>>>>>>> d45a9585682aaede530ecf95e55c6a8ad107786a
  CONSTRAINT is_laptop_notnull CHECK (is_laptop IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS event (
  id UUID PRIMARY KEY,
  evname VARCHAR(255),
  evdate TIMESTAMP,
  place TEXT,
  evdescription TEXT,

  CONSTRAINT evname_notnull CHECK (evname IS NOT NULL),
  CONSTRAINT evname_uniq UNIQUE (evname),
  CONSTRAINT evdate_notnull CHECK (evdate IS NOT NULL),
  CONSTRAINT place_notnull CHECK (place IS NOT NULL),
  CONSTRAINT evdescription_notnull CHECK (evdescription IS NOT NULL)
);


CREATE TABLE IF NOT EXISTS user_event (
  id UUID PRIMARY KEY,
  user_id UUID,
  event_id UUID,

  CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES users (id), 
  CONSTRAINT event_id FOREIGN KEY (event_id) REFERENCES event (id)
);

-- +goose StatementEnd
-- +goose Down
-- +goose StatementBegin
-- +goose StatementEnd