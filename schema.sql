DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE users (
  id SERIAL UNIQUE PRIMARY KEY,
  username VARCHAR(20) UNIQUE NOT NULL,
  password VARCHAR(20) NOT NULL
);

CREATE TABLE posts (
  id BIGSERIAL UNIQUE PRIMARY KEY,
  author_id SERIAL NOT NULL,
  dateCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR NOT NULL,
  body VARCHAR NOT NULL,
  FOREIGN KEY (author_id) REFERENCES users (id)
);