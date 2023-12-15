-- Create and Use Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Create a table with 3 columns
-- One column can’t be null and must be a FOREIGN KEY that references to id of the table created
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCES states(id));
