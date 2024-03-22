--  a SQL script that creates a trigger that resets
-- the attribute valid_email only when the email has been changed.
DELIMITER $$
USE `holberton`$$
CREATE
DEFINER =`paulina`@`localhost`
TRIGGER `users`.`reset`
AFTER UPDATE
ON `users`.`valid_email` FOR EACH ROW
BEGIN
	INSERT into users VALUES (user(), CONCAT('Update email ',
         OLD.email,' email :',OLD.valid_email,' valid_email ',
         NEW.valid_email));
END$$
