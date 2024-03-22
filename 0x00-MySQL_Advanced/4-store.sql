-- A SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.
DELIMITER $$
USE `holberton`$$
CREATE     
DEFINER =`paulina`@`localhost`
TRIGGER `items`.`fruits`
AFTER DELETE
ON `items`.`fruits` FOR EACH ROW
BEGIN
	INSERT into items VALUES (user(), CONCAT('After new order ',
         OLD.items,' Clas :',OLD.quantity, '-> Deleted on ', NOW()));
END$$
