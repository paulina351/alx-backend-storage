-- A SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.
DELIMITER
$$
USE `items`
CREATE     
[DEFINER = { `paulina`@`localhost` }]
TRIGGER `items`.`fruits`
AFTER DELETE
ON `items`.`fruits` FOR EACH ROW
$$
