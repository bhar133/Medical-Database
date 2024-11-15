# Medical-Database
CSC 4402 Database Project

Make sure to have a sql account, I used MySQL Workbench to run the database
Commands to test run the schema.sql file:
    -> mysql -u (your_username) -p
        ^ replace (your_username) with the username you set up your sql with, it is usually root
    Next: you will be prompted to enter your sql password if you have one
    -> source schema.sql
        ^if you have a different path to it, then enter the path there
    -> SHOW DATABASES;
    -> USE medical;
    -> SHOW TABLES;
    -> DESCRIBE (name of table)
        ^replace (name of table) with the one you want to look at