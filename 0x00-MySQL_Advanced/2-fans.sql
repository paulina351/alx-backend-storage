-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
USE holberton;
CREATE TABLE country IF NOT EXISTS (
	origin VARCHAR(255) NOT NULL,
	nb_fans VARCHAR(255) NPT NULL,
);
