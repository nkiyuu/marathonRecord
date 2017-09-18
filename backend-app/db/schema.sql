drop table if exists entries;

-- create user table
create table users (
  id integer primary key autoincrement,
  name string not null unique,
  created_at  text not null default current_timestamp,
  delete_at
);

-- create records table
create table records (
  id integer primary key autoincrement,
  user_id INTEGER not null,
  date text not null,
  time text not null,
  course integer not null,
  created_at text not null default current_timestamp,
  deleted_at text
);

-- create course table
create table courses (
  id integer primary key autoincrement,
  url text not null,
  distance real not null,
  created_at text not null default current_timestamp,
  delete_at text
);
