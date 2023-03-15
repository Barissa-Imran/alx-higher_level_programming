-- Creates the table unique_id with commands on mysql.
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT	DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
);
