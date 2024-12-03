# Medical-Database
CSC 4402 Database Project

Make sure to have a sql account, I used MySQL Workbench to run the database
Commands to test run the schema.sql file:
    -> mysql -u (your_username) -p
        ^ replace (your_username) with the username you set up your sql with, it is usually root
    Next: you will be prompted to enter your sql password if you have one
    -> source schema.sql
        ^if you have a different path to it, then enter the path there
    -> source script.sql
        ^if different path use that
        ^ this will fill the database with mock code
    -> SHOW DATABASES;
    -> USE medical;
    -> SHOW TABLES;
    -> DESCRIBE (name of table)
        ^replace (name of table) with the one you want to look at


To Run the Frontend, open frontend.py and change the database variables in line 7-11 to your connections host, user, and password.
In terminal run the command pip install pymysql 
Then run using the command python frontend.py

Test Queries


See all of Emmas appointments
SELECT Patients.first_name, Patients.last_name, Scheduling.date, Scheduling.time, Scheduling.reason
FROM Appointment
JOIN Patients ON Appointment.p_id = Patients.patient_id
JOIN Scheduling ON Appointment.a_id = Scheduling.appointment_id
WHERE Appointment.d_id = 29;


first_name  last_name date  time  reason
Lisa  Taylor  2024-12-03  11:30:00  Follow-up
John  Doe 2024-12-10  15:00:00  Follow-up Checkup


A patient wants to schedule an appointment
		INSERT INTO Scheduling (appointment_id, date, time, reason)
VALUES (5, '2024-12-10', '15:00:00', 'Follow-up Checkup');
INSERT INTO Appointment (d_id, p_id, a_id)
VALUES (29, 62627, 5);


Result: No output (data successfully inserted).


A patient wants to see their bill for a treatment
SELECT Billing.bill_id, Billing.amount_due, Billing.amount_paid, Billing.insurance_provider
FROM Billing
JOIN Billed ON Billing.bill_id = Billed.b_id
WHERE Billed.p_id = 62627;


bill_id amount_due  amount_paid insurance_provider
2934  2000  1500  HealthFirst


A doctor wants to view all the medications a patient is on
SELECT Patients.first_name, Patients.last_name, Treatment.medication, Treatment.dosage, Treatment.date
FROM Details
JOIN Patients ON Details.p_id = Patients.patient_id
JOIN Treatment ON Details.t_id = Treatment.treatment_id
WHERE Details.p_id = 62627;


first_name  last_name medication  dosage  date
John  Doe Atorvastatin  10mg  2024-11-20


A patient is looking for a doctor with a speciality in cardiology available on .
SELECT Doctor.first_name, Doctor.last_name, Doctor.contact_number, Doctor.availability
FROM Doctor
WHERE Doctor.specialization = 'Cardiology' AND Doctor.availability LIKE '%Mon%';


first_name  last_name contact_number  availability
Alice Johnson 1234561234  Mon-Fri 9:00-17:00


