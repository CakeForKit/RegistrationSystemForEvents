-- +goose Up
-- +goose StatementBegin

CREATE TABLE IF NOT EXISTS user (
  id UUID PRIMARY KEY,
  name VARCHAR(127),
  group VARCHAR(127),
  tgID BIGINT,
  -- tg_username VARCHAR(127),

  CONSTRAINT FIO_notnull CHECK (FIO IS NOT NULL),
  CONSTRAINT group_notnull CHECK (group IS NOT NULL)
);

CREATE TABLE IF NOT EXISTS userAge (
  user_id UUID PRIMARY KEY,
  age INT,
  CONSTRAINT age_positive CHECK (age > 0),
  CONSTRAINT tg_user_id FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE IF NOT EXISTS userIsLaptop (
  user_id UUID PRIMARY KEY,
  is_laptop BOOLEAN DEFAULT FALSE,
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