import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="medical"
)

cursor = connection.cursor()

print("Hello, Welcome to our Healthcare Management System")

print("Press 1 to sign in as a patient")
print("Press 2 to sign in as a doctor")
print("Press 3 to sign in as the hospital manager")

choice = int(input(""))


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
        print("Scheduling Appointment")

    def cancelAppointment(self):
        print("Cancelling Appointment")

    def viewBills(self):
        query = "SELECT Billing.bill_id, Billing.amount_due, Billing.amount_paid, Billing.insurance_provider FROM Billed JOIN Billing ON Billed.b_id = Billing.bill_id WHERE Billed.p_id = %s;"
        cursor.execute(query, (self.p_id))
        result = cursor.fetchall()
        for row in result:
            print(row)
    def viewAppointments(self):
        print("Viewing Appointments")

    def viewTreatments(self):
        print("Viewing Treatments")


class Doctor:
    def __init__(self, d_id):
        self.d_id = d_id

    def showOptions():
        pass

    def viewAppointments(self):
        pass

    def setAvailability(self):
        pass

    def assignTreatment(self):
        pass

class HospitalManager:
    pass

if choice == 1:
    id = int(input("Enter your patient ID"))
    user = Patient(id)
    
elif choice == 2:
    id = int(input("Enter your doctor ID"))
    user = Doctor(id)

user.showOptions()



