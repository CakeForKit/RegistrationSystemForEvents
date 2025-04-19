-- +goose Up
-- +goose StatementBegin

CREATE TABLE IF NOT EXISTS user (
  id UUID PRIMARY KEY,
  FIO VARCHAR(127),
  group VARCHAR(127),
  tg_username VARCHAR(127),

  CONSTRAINT FIO_notnull CHECK (FIO IS NOT NULL),
  CONSTRAINT group_notnull CHECK (group IS NOT NULL),
  CONSTRAINT tg_username_notnull CHECK (tg_username IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS user_type_1 (
  id UUID PRIMARY KEY,
  user_id UUID,
  gender VARCHAR(10),
  age INT,
  CONSTRAINT age_positive CHECK (age > 0),
  CONSTRAINT gender CHECK (gender IS NOT NULL),
  CONSTRAINT FIO_notnull CHECK (FIO IS NOT NULL),
  CONSTRAINT tg_user_id FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS user_type_2 (
  id UUID PRIMARY KEY,
  user_id UUID,
  is_laptop BOOLEAN DEFAULT FALSE,
  experience INT
  link_to_rep TEXT, 
  CONSTRAINT experience_positive CHECK (experience > 0),
  CONSTRAINT gender CHECK (gender IS NOT NULL),
  CONSTRAINT link_to_rep_notnull CHECK (link_to_rep IS NOT NULL),
  CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES user (id)
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
  CONSTRAINT evdescription_notnull CHECK (evdescription IS NOT NULL),
);


CREATE TABLE IF NOT EXISTS user_event (
  id UUID PRIMARY KEY,
  user_id UUID,
  event_id UUID,

  CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES user (id), 
  CONSTRAINT event_id FOREIGN KEY (event_id) REFERENCES event (id)
);

-- +goose StatementEnd
-- +goose Down
-- +goose StatementBegin
-- +goose StatementEnd