-- a SQL script that creates an index idx_name_first_score on
-- the table names and the first letter of name and the score.
CREATE TABLE tableName (
ID int,
LName varchar(255),
FName varchar(255),
DOB varchar(255),
LOC varchar(255),
INDEX ( ID )
);
