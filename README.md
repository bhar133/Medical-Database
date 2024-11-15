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

    Here is a command i ran to put an example person in the patients table:
        INSERT INTO Patients (patient_id, first_name, last_name, date_of_birth, contact_number, medical_history)
        VALUES (1, 'John', 'Doe', '1990-01-01', 1234567890, 'None');
    To see that data run this:
        SELECT * FROM Patients;