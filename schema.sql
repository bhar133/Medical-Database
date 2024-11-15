-- Create the database
CREATE DATABASE IF NOT EXISTS medical;
USE medical;

-- Create the Patients table (Entity)
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number INT,
    medical_history VARCHAR(255)
);

-- Create the Doctor table (Entity)
CREATE TABLE Doctor (
    doctor_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    specialization VARCHAR(100),
    contact_number BIGINT,
    availability TEXT,
    salary INT
);

-- Create the Hospital table (Entity)
CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget INT
);

-- Create the Billing table (Relationship)
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY,
    patient_id INT,
    amount_due INT NOT NULL,
    amount_paid INT,
    insurance_provider VARCHAR(100),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Create the Treatment table (Relationship)
CREATE TABLE Treatment (
    treatment_id INT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    medication VARCHAR(100) NOT NULL,
    dosage VARCHAR(50),
    date DATE,
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

-- Create the Appointment table (Relationship)
CREATE TABLE Appointment (
    patient_id INT,
    doctor_id INT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    reason VARCHAR(255),
    PRIMARY KEY (patient_id, doctor_id, date, time),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);
