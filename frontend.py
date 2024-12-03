import pymysql


running = True
#####################  Modify Code Here ###########################
# Connect to the MySQL database
conn = pymysql.connect(
    host='localhost',  # Replace with your database host
    user='root',  # Replace with your database username
    password='1234',  # Replace with your database password
    database='medical'  # Replace with your database name
)
cursor = conn.cursor()

def view_appointments():
    query = """
    SELECT Patients.first_name, Patients.last_name, Scheduling.date, Scheduling.time, Scheduling.reason FROM Appointment JOIN Patients ON Appointment.p_id = Patients.patient_id JOIN Scheduling ON Appointment.a_id = Scheduling.appointment_id WHERE Appointment.d_id = 29;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nAppointments:")
    for row in results:
        first_name, last_name, date, time, reason = row
        # Convert time to a readable format
        if isinstance(time, (str, bytes)):
            time_str = time
        else:
            time_str = str(time)
        print(f"{first_name} {last_name}, {date}, {time_str}, {reason}")

def schedule_appointment():
    query1 = "INSERT INTO Scheduling (appointment_id, date, time, reason) VALUES (5, '2024-12-10', '15:00:00', 'Follow-up Checkup');"
    query2 = "INSERT INTO Appointment (d_id, p_id, a_id) VALUES (29, 62627, 5);"
    try:
        cursor.execute(query1)
        cursor.execute(query2)
        conn.commit()
        print("\nAppointment successfully scheduled.")
    except Exception as e:
        conn.rollback()
        print(f"Error scheduling appointment: {e}")

def view_bill():
    query = """
    SELECT Billing.bill_id, Billing.amount_due, Billing.amount_paid, Billing.insurance_provider
    FROM Billing
    JOIN Billed ON Billing.bill_id = Billed.b_id
    WHERE Billed.p_id = 62627;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nBill Details:")
    for row in results:
        print(row)

def view_medications():
    query = """
    SELECT Patients.first_name, Patients.last_name, Treatment.medication, Treatment.dosage, Treatment.date
    FROM Details
    JOIN Patients ON Details.p_id = Patients.patient_id
    JOIN Treatment ON Details.t_id = Treatment.treatment_id
    WHERE Details.p_id = 62627;
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nMedications:")
    for row in results:
        print(row)

def find_cardiologist():
    query = """
    SELECT Doctor.first_name, Doctor.last_name, Doctor.contact_number, Doctor.availability
    FROM Doctor
    WHERE Doctor.specialization = 'Cardiology' AND Doctor.availability LIKE '%Mon%';
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\nAvailable Cardiologists:")
    for row in results:
        print(row)

def main():
    # Show options that correlate to test cases
    print("Select an option:")
    print("1. See all of Emma's appointments")
    print("2. Schedule a new appointment")
    print("3. View a patient's bill")
    print("4. View a patient's medications")
    print("5. Find a cardiologist available on Monday")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_appointments()
        return True
    elif choice == "2":
        schedule_appointment()
        return True
    elif choice == "3":
        view_bill()
        return True
    elif choice == "4":
        view_medications()
        return True
    elif choice == "5":
        find_cardiologist()
        return True
    elif choice == "6":
        return False
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

#Loop to run until user presses 6
while running:
    running = main()

# Close the database connection
cursor.close()
conn.close()
