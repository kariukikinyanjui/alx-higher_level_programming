-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

--  Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT FULL,
	PRIMARY KEY (id),
	UNIQUE KEY id_unique (id)
);
