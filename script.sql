USE medical;

-- Insert data into Hospital
INSERT INTO Hospital (hospital_id, name, budget) VALUES
(373, 'City Hospital', 5000000),
(575, 'Green Valley Clinic', 2000000),
(898, 'Sunrise Medical Center', 8000000);

-- Insert data into Patients
INSERT INTO Patients (patient_id, first_name, last_name, date_of_birth, contact_number, medical_history) VALUES
(62627, 'John', 'Doe', '1985-06-15', 1234567890, 'Hypertension'),
(62628, 'Jane', 'Smith', '1990-11-22', 1876543210, 'Asthma'),
(62629, 'Sam', 'Brown', '1978-03-10', 1122334455, 'Diabetes'),
(62630, 'Lisa', 'Taylor', '2000-07-05', 1566778899, 'Healthy');

-- Insert data into Doctor
INSERT INTO Doctor (doctor_id, first_name, last_name, specialization, contact_number, availability, salary, hospital_id) VALUES
(123, 'Alice', 'Johnson', 'Cardiology', 1234561234, 'Mon-Fri 9:00-17:00', 150000, 373),
(467, 'Bob', 'Williams', 'Pediatrics', 2345672345, 'Tue-Thu 10:00-16:00', 120000, 898),
(293, 'Chris', 'Davis', 'Orthopedics', 3456783456, 'Mon-Wed 8:00-14:00', 130000, 575),
(029, 'Emma', 'Wilson', 'Dermatology', 4567894567, 'Fri-Sat 12:00-18:00', 110000, 373);

-- Insert data into Billing
INSERT INTO Billing (bill_id, amount_due, amount_paid, insurance_provider) VALUES
(02934, 2000, 1500, 'HealthFirst'),
(02384, 3000, 3000, 'CarePlus'),
(02945, 1500, 1000, 'MediCare'),
(02944, 4000, 3500, 'WellnessInsurance');

-- Insert data into Billed
INSERT INTO Billed (b_id, p_id) VALUES
(02934, 62627),
(02384, 62629),
(02945, 62628),
(02944, 62630);

-- Insert data into Scheduling
INSERT INTO Scheduling (appointment_id, date, time, reason) VALUES
(1, '2024-12-01', '10:00:00', 'Routine Check-up'),
(2, '2024-12-03', '11:30:00', 'Follow-up'),
(3, '2024-12-05', '14:00:00', 'Consultation'),
(4, '2024-12-07', '09:30:00', 'Specialist Visit');

-- Insert data into Appointment
INSERT INTO Appointment (d_id, p_id, a_id) VALUES
(123, 62627, 1),
(029, 62630, 2),
(123, 62628, 3),
(467, 62629, 4);

-- Insert data into Treatment
INSERT INTO Treatment (treatment_id, medication, dosage, date) VALUES
(001, 'Atorvastatin', '10mg', '2024-11-20'),
(002, 'Albuterol', '90mcg', '2024-11-21'),
(003, 'Metformin', '500mg', '2024-11-22'),
(004, 'Amoxicillin', '250mg', '2024-11-23');

-- Insert data into Details
INSERT INTO Details (p_id, t_id) VALUES
(62627, 001),
(62628, 002),
(62629, 003),
(62630, 004);
