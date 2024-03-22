-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
USE `holberton`;
CREATE TABLE IF NOT EXISTS metal_bands (
    origin VARCHAR(255) NOT NULL,
    nb_fans VARCHAR(255) NOT NULL
);
