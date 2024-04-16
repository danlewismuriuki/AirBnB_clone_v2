-- Write a script that prepares a MySQL server for the project:

-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

-- create a dtabse `hbnb_dev_db`
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create a new user hbnb_dev in @localhost with passwd hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
GRANT ALL PRIVILEGES ON hbnb_dev_db.* To 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- FLUSH PRIVILEGES to apply changes
FLUSH PRIVILEGES;
