import os
import pandas as pd

class School:
    
    def menu(self):

        employee_path = 'employee.csv'
        student_path = 'student.csv'

        if os.path.exists(f"data/{employee_path}"):
            pass
        else:
            pd.DataFrame(columns=['employee_id', 'name', 'email', 'contact', 'salary', 'position']).to_csv(f"data/{employee_path}", index=False)

        if os.path.exists(f"data/{student_path}"):
            pass
        else:
            pd.DataFrame(columns=['student_id', 'name', 'contact', 'email', 'class_name', 'marks', 'age']).to_csv(f"data/{student_path}", index=False)

        user = input("Are you an admin or teacher? (Admin/Teacher): ").lower()

        if user == 'admin':
            while True:
                print("Admin Menu: ")
                print()
                print("1. Employee Management")
                print("2. Student Management")
                print("3. Class and Schedule Management")
                print("4. Exit")
                management = input("Select an option (1 to 4): ")

                print("1. Add Employee")
                print("2. Remove Employee")
                print("3. Update Employee")
                print("4. View Employees")
                print("5. Add Student")            