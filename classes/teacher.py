import os
import pandas as pd
from classes.person import Person
import numpy as np

class Teacher(Person):
    
    def __init__(self, name, password):
        super().__init__(name, password)

    def mark_attendance(self):
        existing_data = pd.read_csv('data/student.csv', dtype={'contact': str, 'age': int}) 

        if not os.path.exists("data/attendance"):
            os.makedirs("data/attendance")

        date = input("Enter date (eg: 5/6/2025, 27/5/2025): ").strip().replace("/", "_")

        class_name = input("Enter class name: ")

        filtered_students = existing_data[existing_data['class_name'] == class_name]

        if os.path.exists(f'data/attendance/{date} - {class_name} - attendance.csv'):
            print("File already exists.")

            while True:
                for index, student in filtered_students.iterrows():
                    student_id = student['student_id']
                    name = student['name']
                    
                    student_attendance = existing_data[existing_data['student_id'] == student_id]

                    status = input(f"Update attendance for {name} (yes/no): ").strip().lower()  or existing_data.loc[index, 'attendance']
                    
                    existing_data.loc[index, 'attendance'] = status

                existing_data.to_csv(f'data/attendance/{date} - {class_name} - attendance.csv', index=False)
                print("Attendance updated successfully!")
                print()

                break

        else:
            pd.DataFrame(columns=['student_id', 'name', 'attendance']).to_csv(f'data/attendance/{date} - {class_name} - attendance.csv', index=False)

            attendance_data = []

            for index, student in filtered_students.iterrows():
                student_id = student['student_id']
                name = student['name']
                
                status = input(f"Enter attendance for {name} (yes/no): ").strip().lower()
                while status not in ['yes', 'no']:  
                    status = input(f"Invalid input. Enter attendance for {name} (yes/no): ").strip().lower()

                attendance_data.append({
                    'student_id': student_id,
                    'name': name,
                    'attendance': status
                })

            df_attendance = pd.DataFrame(attendance_data)
            df_attendance.to_csv(f"data/attendance/{date} - {class_name} - attendance.csv", index=False)

            print("Attendance marked succesfully!")
            print()

    def view_attendance(self):
        print("View attendance records by students or class.")      
        print()
        print("1. Students")
        print("2. Class")
        print()
        attendance_option = input("Select an option (1 to 2): ")

        while True:
            if attendance_option == '1':
                student_id = input("Enter Student ID: ")

                if os.path.exists(f"data/report/attendance/{student_id}.csv"):
                    attendance = pd.read_csv(f'data/report/attendance/{student_id}.csv')

                    print(attendance.to_string())
                    print()

                else:
                    print(f"Attendance report for student {student_id} does not exist!")

                break

            elif attendance_option == '2':
                while True:
                    date = input("Enter date (eg: 5/6/2025, 27/5/2025): ").strip().replace("/", "_")
                    class_name = input("Enter class name: ")

                    if os.path.exists(f'data/attendance/{date} - {class_name} - attendance.csv'):
                        attendance = pd.read_csv(f'data/attendance/{date} - {class_name} - attendance.csv')    
                        print(attendance.to_string())
                        print()

                    else:
                        print(f"Attendance record for {class_name} on {date} does not exist!")

                    break

            else:
                print("Invalid Option.")

            break

    def add_student_marks(self):
        existing_student_data = pd.read_csv('data/student.csv', dtype={'student_id': str,}) 
        existing_student_data['student_id'] = existing_student_data['student_id'].astype(str)

        year = int(input("Enter the year: "))
        semester = input("Enter the semester (1, 2, 3): ")
        subject = input("Enter the subject: ")

        if not os.path.exists("data/marks"):
            os.makedirs("data/marks")  

        if os.path.exists(f'data/marks/semester {semester} - {year} - {subject}.csv'):   
             pass
        else:       
            pd.DataFrame(columns=['student_id', 'marks']).to_csv(f"data/marks/semester {semester} - {year} - {subject}.csv", index=False)    

        existing_mark_data = pd.read_csv(f"data/marks/semester {semester} - {year} - {subject}.csv", dtype={'student_id': str, 'marks': str})
        
        while True:

            student_id = input("Enter Student ID: ")

            if student_id not in existing_student_data['student_id'].values:
                print(f"ERROR: Student ID {student_id} does not exist. Try again.")
                continue  

            if student_id in existing_mark_data['student_id'].values:
                print(f"Student ID {student_id} already has marks recorded. Skipping...")
                return 

            break
          
        mark = input("Enter Student Marks: ")

        new_data = {
        'student_id': [student_id], 
        'marks': [mark],
        }   

        mark_info = pd.DataFrame(new_data)

        mark_info.to_csv(f"data/marks/semester {semester} - {year} - {subject}.csv", mode='a', header=False, index=False)

        print("Student information successfully added!")
        print()

    def update_student_marks(self):
        year = input("Enter the year: ")
        semester = input("Enter semester (1, 2, 3): ")
        subject = input("Enter the subject: ")

        if os.path.exists(f'data/marks/semester {semester} - {year} - {subject}.csv'):
            existing_data = pd.read_csv(f'data/marks/semester {semester} - {year} - {subject}.csv', dtype={'student_id': str, 'marks': str})

            while True:
                student_id = input("Enter student ID: ")

                if student_id not in existing_data['student_id'].values:
                    print(f"ERROR: Student ID {student_id} does not exist in file! Try again.")
                    continue

                mark_index = existing_data[existing_data['student_id'] == student_id].index[0]

                mark = input("Enter Student Marks: ") or existing_data.loc[mark_index, 'marks']

                existing_data.loc[mark_index, 'marks'] = mark

                existing_data.to_csv(f"data/marks/semester {semester} - {year} - {subject}.csv", index=False)

                print("Student mark successfully updated!")
                print()

                break

        else:
            print("The file does not exist.")

    def generate_performance_analytics(self):
        pass

    def update_teacher_profile(self):
        existing_data = pd.read_csv('data/employee.csv', dtype={'contact': str, 'salary': int}) 
        existing_data['employee_id'] = existing_data['employee_id'].astype(str)
        
        while True:
            employee_id = input("Enter Employee ID: ")
            
            if employee_id not in existing_data['employee_id'].values:
                print(f"ERROR: Employee ID {employee_id} does not exist! Try again.")
                continue
            
            employee_index = existing_data[existing_data['employee_id'] == employee_id].index[0]
            employee_position = existing_data.loc[employee_index, 'position']
            
            if employee_position != "teacher":
                print(f"ERROR: Employee ID {employee_id} is not a teacher. Current position: {employee_position}. Try again.")
                continue
            
            break
        
        print(f"Enter new details for employee {employee_id} (press Enter to keep existing values)")
        print()

        name = input("Enter New Employee Name: ") or existing_data.loc[employee_index, 'name']
        email = input("Enter New Employee Email: ") or existing_data.loc[employee_index, 'email']
        contact = input("Enter New Employee Contact: ") or existing_data.loc[employee_index, 'contact']
        
        while True:
            salary_input = input("Enter Employee Salary: ")

            if salary_input == "": 
                salary = existing_data.loc[employee_index, 'salary']
                break

            try:
                salary = int(salary_input)
                break
            except ValueError:
                print("ERROR: Salary must be a number! Try again.")
        
        position = input("Enter Employee Position: ") or existing_data.loc[employee_index, 'position']
        
        existing_data.loc[employee_index, 'name'] = name
        existing_data.loc[employee_index, 'email'] = email
        existing_data.loc[employee_index, 'contact'] = contact
        existing_data.loc[employee_index, 'salary'] = salary
        existing_data.loc[employee_index, 'position'] = position

        existing_data.to_csv("data/employee.csv", index=False)

        print("Employee information successfully updated!")
        print()

    def manage_class_schedule(self):

        existing_data = pd.read_csv('data/student.csv', dtype={'contact': str, 'age': int}) 

        class_name = input("Enter Class:")

        day = input("Enter the day of the class schedule (Monday, Tuesday, Wednesday, Thursday, Friday): ")

        if os.path.exists(f"data/schedule/{class_name} - {day}.csv"):
            existing_data = pd.read_csv(f"data/schedule/{class_name} - {day}.csv")

            while True:

                for index, timeslot in existing_data.iterrows():
                    timeslot = timeslot['timeslot']

                    new_subject = input(f"Update subject for {timeslot}: ").strip().lower()  or existing_data.loc[index, 'subject']
                    new_teacher = input(f"Update subject for {timeslot}: ").strip().lower()  or existing_data.loc[index, 'teacher']
                    
                    existing_data.loc[index, 'subject'] = new_subject
                    existing_data.loc[index, 'teacher'] = new_teacher

                existing_data.to_csv(f"data/schedule/{class_name} - {day}.csv", index=False)

                print("Class schedule successfully updated!")
                print()

                break
        else:
            print("File does not exist.")

    def create_lesson_plan(self):
        pass