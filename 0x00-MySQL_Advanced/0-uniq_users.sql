-- A SQL Script that creates a table users
USE `holberton`;
CREATE TABLE IF NOT EXIST users (
	Id int NOT NULL | AUTO_INCREMENT | PRIMARY KEY,
	Email varchar(255) NOT NULL |UNIQUE,
	Name varchar(255)
);
