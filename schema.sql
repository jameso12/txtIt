DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE users (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
  username VARCHAR(20) UNIQUE NOT NULL,
  password VARCHAR(20) NOT NULL
);

CREATE TABLE posts (
  id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
  author_id uuid NOT NULL,
  dateCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title VARCHAR NOT NULL,
  content VARCHAR NOT NULL,
  FOREIGN KEY (author_id) REFERENCES users (id)
);