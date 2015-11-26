DROP TABLE if EXISTS users;
DROP TABLE if EXISTS images;

CREATE TABLE users(
	name text,
	user text,
	email text,
	pass text
);

CREATE TABLE images(
	user text,
	image blob,
	desc text,
	date text
);