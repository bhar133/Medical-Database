-- Create the database
CREATE DATABASE IF NOT EXISTS medical;
USE medical;

-- Create the Hospital table (Entity)
CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    budget INT
);

-- Create the Patients table (Entity)
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    contact_number BIGINT,
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
    salary INT,
    hospital_id INT,
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);

-- Create the Billing table (Entity)
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY,
    amount_due INT NOT NULL,
    amount_paid INT,
    insurance_provider VARCHAR(100)
);

-- Create the Billed table (Relationship)
CREATE TABLE Billed (
    b_id INT,
    p_id INT,
    PRIMARY KEY (b_id, p_id),
    FOREIGN KEY (b_id) REFERENCES Billing(bill_id),
    FOREIGN KEY (p_id) REFERENCES Patients(patient_id)
);

-- Create the Scheduling table (Entity)
CREATE TABLE Scheduling (
    appointment_id INT PRIMARY KEY,
    date DATE NOT NULL,
    time TIME NOT NULL,
    reason VARCHAR(255)
);

-- Create the Appointment table (Relationship)
CREATE TABLE Appointment (
    d_id INT,
    p_id INT,
    a_id INT,
    PRIMARY KEY (d_id, p_id, a_id),
    FOREIGN KEY (d_id) REFERENCES Doctor(doctor_id),
    FOREIGN KEY (p_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (a_id) REFERENCES Scheduling(appointment_id)
);

-- Create the Treatment table (Entity)
CREATE TABLE Treatment (
    treatment_id INT PRIMARY KEY,
    medication VARCHAR(100) NOT NULL,
    dosage VARCHAR(50),
    date DATE
);

-- Create the Details table (Relationship)
CREATE TABLE Details (
    p_id INT,
    t_id INT,
    PRIMARY KEY (p_id, t_id),
    FOREIGN KEY (p_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (t_id) REFERENCES Treatment(treatment_id)
);