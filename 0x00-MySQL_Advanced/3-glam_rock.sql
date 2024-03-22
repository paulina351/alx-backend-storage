-- a SQL script that lists all bands with Glam rock
-- as their main style, ranked by their longevity
USE holberton;
CREATE TABLE IF NOT EXISTS metal_bands (
    band_name VARCHAR(255) NOT NULL,
    lifespan VARCHAR(255) NOT NULL
);
INSERT INTO metal_bands(lifespan) VALUES('formed', 'spilt');
