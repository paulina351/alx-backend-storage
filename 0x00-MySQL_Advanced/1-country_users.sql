-- A SQL Script that creates table called users

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country VARCHAR(2) NOT NULL DEFAULT 'US',
    CONSTRAINT chk_country CHECK (country IN ('US', 'CO', 'TN'))
);
