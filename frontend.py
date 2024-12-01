import pymysql
from datetime import datetime

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="medical"
)

cursor = connection.cursor()



def find_account_by_details():
    try:
        with connection.cursor() as cursor:
            # Collect search details from the user
            print("Search for Patient Account:")
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()

            # Query the database for the patient's account number
            cursor.execute("""
                SELECT patient_id 
                FROM Patients
                WHERE first_name = %s AND last_name = %s AND date_of_birth = %s;
            """, (first_name, last_name, date_of_birth))

            # Fetch the result
            result = cursor.fetchone()

            if result:
                print(f"Patient Account Number: {result[0]}")
            else:
                print("No patient found with the provided details.")

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")

def add_patient_to_database():
    # Connect to the MySQL database
    try:
        with connection.cursor() as cursor:
            # Collect patient details from the user
            print("Enter new patient details:")
            patient_id = int(input("Patient ID: "))
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            while True:
                date_of_birth = input("Date of Birth (YYYY-MM-DD): ").strip()
                try:
                    datetime.strptime(date_of_birth, "%Y-%m-%d")  # Validate date format
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            contact_number = input("Contact Number (or press Enter to skip): ").strip()
            contact_number = int(contact_number) if contact_number else None
            medical_history = input("Medical History (or press Enter to skip): ").strip() or None

            # Insert the new record into the table
            try:
                cursor.execute("""
                    INSERT INTO Patients (patient_id, first_name, last_name, date_of_birth, contact_number, medical_history)
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, (patient_id, first_name, last_name, date_of_birth, contact_number, medical_history))
                connection.commit()
                print("Patient added successfully!")
            except pymysql.IntegrityError as e:
                print(f"Error: {e}")
    except:
        print("error")

class Patient:
    def __init__(self, p_id):
        self.p_id = p_id

    def showOptions(self):
        while True:
            print("\n--- Patient Options ---")
            print("1. Schedule an Appointment")
            print("2. Cancel an Appointment")
            print("3. View Bills")
            print("4. View Appointments")
            print("5. View Treatments")
            print("6. Exit")
            try:
                action = int(input("Enter the number corresponding to your choice: "))
                if action == 1:
                    self.scheduleAppointment()
                elif action == 2:
                    self.cancelAppointment()
                elif action == 3:
                    self.viewBills()
                elif action == 4:
                    self.viewAppointments()
                elif action == 5:
                    self.viewTreatments()
                elif action == 6:
                    print("Exiting options. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def scheduleAppointment(self):
            try:
                with connection.cursor() as cursor:
                    # Collect appointment details from the user
                    
                    # Check if the patient exists
                    cursor.execute("SELECT * FROM Patients WHERE patient_id = %s;", (self.p_id,))
                    doctor_id = int(input("Enter Doctor ID: "))
                    
                    # Check if the doctor exists
                    cursor.execute("SELECT * FROM Doctor WHERE doctor_id = %s;", (doctor_id,))
                    if cursor.rowcount == 0:
                        print("Doctor not found. Please check the Doctor ID.")
                        return
                    appointment_id = input("Enter the Appointment ID: ")
                    appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ").strip()
                    appointment_time = input("Enter Appointment Time (HH:MM:SS): ").strip()
                    reason = input("Enter the reason for the appointment: ").strip()

                    # Validate date and time
                    try:
                        datetime.strptime(appointment_date, "%Y-%m-%d")
                        datetime.strptime(appointment_time, "%H:%M:%S")
                    except ValueError:
                        print("Invalid date or time format.")
                        return

                    # Insert the scheduling record
                    cursor.execute("""
                        INSERT INTO Scheduling (appointment_id, date, time, reason)
                        VALUES (%s, %s, %s, %s);
                    """, (appointment_id, appointment_date, appointment_time, reason))
                    connection.commit()

                    # Insert the relationship in the Appointment table
                    cursor.execute("""
                        INSERT INTO Appointment (d_id, p_id, a_id)
                        VALUES (%s, %s, %s);
                    """, (doctor_id, self.p_id, appointment_id))
                    connection.commit()

                    print(f"Appointment scheduled successfully! Appointment ID: {appointment_id}")

            except pymysql.MySQLError as e:
                print(f"Database error: {e}")

    def cancelAppointment(self):
        print("Cancelling Appointment")

    def viewBills(self):
        query = "SELECT Billing.bill_id, Billing.amount_due, Billing.amount_paid, Billing.insurance_provider FROM Billed JOIN Billing ON Billed.b_id = Billing.bill_id WHERE Billed.p_id = %s;"
        cursor.execute(query, (self.p_id))
        result = cursor.fetchall()
        for row in result:
            print(row)
        payBillID = int(input("Enter the Bill ID you would like to pay or 0 to return to the menu: "))
        if payBillID == 0:
            pass
        else:
            amount_paid = int(input("How much would you like to pay"))
            query = """
            UPDATE billing
            SET 
                amount_paid = amount_paid + %s,
                amount_due = amount_due - %s
            WHERE billing_id = %s
            """
            cursor.execute(query, (amount_paid, amount_paid, payBillID))

    def viewAppointments(self):
        print("Viewing Appointments")

    def viewTreatments(self):
        print("Viewing Treatments")


class Doctor:
    def __init__(self, d_id):
        self.d_id = d_id

    def showOptions(self):
        while True:
            print("\n--- Doctor Options ---")
            print("1. View Appointments")
            print("2. Set Availability")
            print("3. Assign Treatment")
            print("4, Exit")
            try:
                action = int(input("Enter the number corresponding to your choice: "))
                if action == 1:
                    self.viewAppointments()
                elif action == 2:
                    self.setAvailability()
                elif action == 3:
                    self.assignTreatment()
                elif action == 4:
                    print("Exiting options. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def viewAppointments(self):
        pass

    def setAvailability(self):
        pass

    def assignTreatment(self):
        pass

class HospitalManager:
    pass

def mainMenu():
    print("Hello, Welcome to our Healthcare Management System")

    print("Press 0 to register a new account")
    print("Press 1 to sign in as a patient")
    print("Press 2 to sign in as a doctor")
    print("Press 3 to find account number")

    choice = int(input(""))


    if choice == 0:
        add_patient_to_database()
    elif choice == 1:
        id = int(input("Enter your patient ID"))
        user = Patient(id)
        user.showOptions()
        
    elif choice == 2:
        id = int(input("Enter your doctor ID"))
        user = Doctor(id)
        user.showOptions()

    elif choice == 3:
        find_account_by_details()
    
    mainMenu()


mainMenu()


