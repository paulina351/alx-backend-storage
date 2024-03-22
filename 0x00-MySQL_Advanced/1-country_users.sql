-- A SQL Script that creates table called users
USE `holberton`
CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT,
       email varchar(255) NOT NULL,
       name varchar(255),
       country ENUM('US','CO','TN') NOT NULL,
       PRIMARY KEY (id),
       UNIQUE (email)
);
