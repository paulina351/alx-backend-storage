-- a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
USE holberton;
CREATE TABLE glam IF NOT EXISTS (
        band_name VARCHAR(255) NOT NULL,
        lifespan VARCHAR(255) NOT NULL,
);

INSERT INTO glam(lifespan) VALUES('formed', 'spilt');
