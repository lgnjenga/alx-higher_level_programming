-- Create a table with 2 columns
-- One column has a unique default value
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
