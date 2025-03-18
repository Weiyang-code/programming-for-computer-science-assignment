import os
import pandas as pd
from classes.person import Person
import numpy as np

class Admin(Person):

    def __init__(self, id, password):
        super().__init__(id, password)
    
    import pandas as pd

    def add_employee(self):
        existing_data = pd.read_csv('data/employee.csv', dtype={'employee_id': str, 'salary': int})  

        while True:
            employee_id = input("Enter Employee ID: ")
            
            if employee_id in existing_data['employee_id'].values:
                print(f"ERROR: Employee ID {employee_id} already exists! Try again.")
            else:
                break

        name = input("Enter Employee Name: ")
        email = input("Enter Employee Email: ")
        contact = input("Enter Employee Contact: ")
        
        while True:
            try:
                salary = int(input("Enter Employee Salary: ")) 
                break
            except ValueError:
                print("ERROR: Salary must be a number! Try again.")
        
        position = input("Enter Employee Position: ")

        new_data = {
            'employee_id': [employee_id], 
            'name': [name],
            'email': [email], 
            'contact': [contact], 
            'salary': [salary], 
            'position': [position]
        }

        employee_info = pd.DataFrame(new_data)

        employee_info.to_csv('data/employee.csv', mode='a', header=False, index=False)

        print("Employee information successfully added!")
        print()

    def remove_employee(self):
        data = pd.read_csv('data/employee.csv', dtype= {'employee_id': str}) 

        while True:
            employee_id = input("Enter Employee ID: ")
            
            if employee_id not in data['employee_id'].values:
                print(f"ERROR: Employee ID {employee_id} does not exist! Try again.")
            else:
                break

        data = data[data['employee_id'] != employee_id] 

        data.to_csv('data/employee.csv', index = False)

        print("Employee successfully removed!")
        print()

    def update_employee(self):
        existing_data = pd.read_csv('data/employee.csv', dtype={'contact': str, 'salary': int}) 

        existing_data['employee_id'] = existing_data['employee_id'].astype(str)

        while True:
            employee_id = input("Enter Employee ID: ")
            
            if employee_id not in existing_data['employee_id'].values:
                print(f"ERROR: Employee ID {employee_id} does not exist! Try again.")
            else:
                break
        
        employee_index = existing_data[existing_data['employee_id'] == employee_id].index[0]
        
        print(f"Enter new details for employee,{employee_id} (press Enter to keep existing values)")
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

    def view_employee(self):
        employee_list = pd.read_csv('data/employee.csv', dtype = {'contact' : str})    
        print(employee_list.to_string())
        print()        

    def add_student(self):
        existing_data = pd.read_csv('data/student.csv', dtype={'student_id': str, 'age': int})  

        while True:
            student_id = input("Enter Student ID: ")
            
            if student_id in existing_data['student_id'].values:
                print(f"ERROR: Student ID {student_id} already exists! Try again.")
            else:
                break

        name = input("Enter Student Name: ")
        email = input("Enter Student Email: ")
        contact = input("Enter Student Contact: ")
        class_name = (input("Enter Student Class: ")) 
        age = input("Enter Student Age: ")

        new_data = {
            'student_id': [student_id], 
            'name': [name],
            'email': [email], 
            'contact': [contact], 
            'class_name': [class_name], 
            'age': [age]
        }

        student_info = pd.DataFrame(new_data)

        student_info.to_csv('data/student.csv', mode='a', header=False, index=False)

        print("Student information successfully added!")
        print()

    def remove_student(self):
        data = pd.read_csv('data/student.csv', dtype= {'student_id': str}) 

        while True:
            student_id = input("Enter Student ID: ")
            
            if student_id not in data['student_id'].values:
                print(f"ERROR: Student ID {student_id} does not exist! Try again.")
            else:
                break

        data = data[data['student_id'] != student_id] 

        data.to_csv('data/student.csv', index = False)

        print("Student successfully removed!")
        print()

    def update_student(self):
        existing_data = pd.read_csv('data/student.csv', dtype={'contact': str, 'age': int}) 

        existing_data['student_id'] = existing_data['student_id'].astype(str)

        while True:
            student_id = input("Enter Student ID: ")
            
            if student_id not in existing_data['student_id'].values:
                print(f"ERROR Student ID {student_id} does not exist! Try again.")
            else:
                break
        
        student_index = existing_data[existing_data['student_id'] == student_id].index[0]
        
        print(f"Enter new details for student,{student_id} (press Enter to keep existing values)")
        print()

        name = input("Enter New Student Name: ") or existing_data.loc[student_index, 'name']
        email = input("Enter New Student Email: ") or existing_data.loc[student_index, 'email']
        contact = input("Enter New Student Contact: ") or existing_data.loc[student_index, 'contact']
        class_name = input("Enter New Student Class Name: ") or existing_data.loc[student_index, 'class_name']
        age = input("Enter Student age: ") or existing_data.loc[student_index, 'age']
        
        existing_data.loc[student_index, 'name'] = name
        existing_data.loc[student_index, 'email'] = email
        existing_data.loc[student_index, 'contact'] = contact
        existing_data.loc[student_index, 'class_name'] = class_name
        existing_data.loc[student_index, 'age'] = age

        existing_data.to_csv("data/student.csv", index=False)

        print("Student information successfully updated!")
        print()

    def view_student(self):
        student_list = pd.read_csv('data/student.csv', dtype = {'contact' : str})    
        print(student_list.to_string())
        print()  

    def schedule_class(self):

        if not os.path.exists("data/schedule"):
            os.makedirs("data/schedule")

        class_name = input("Enter Class:")
        day = input("Enter the day of the class schedule (Monday, Tuesday, Wednesday, Thursday, Friday): ")

        timeslot1 = "8am - 9am"
        timeslot2 = "9am - 10am"
        timeslot3 = "10am - 11am"
        timeslot4 = "11am - 12pm"
        timeslot5 = "12pm - 1pm"

        if os.path.exists(f"data/schedule/{class_name} - {day}.csv"):
            print("File already exists.")

        else:
            pd.DataFrame(columns=['timeslot', 'subject', 'teacher']).to_csv(f"data/schedule/{class_name} - {day}.csv", index=False)

            timeslot1_subject = input("Enter the subject for timeslot (8am - 9am): ")
            timeslot1_teacher = input("Enter the teacher for timeslot (8am - 9am): ")
            timeslot2_subject = input("Enter the subject for timeslot (9am - 10am): ")
            timeslot2_teacher = input("Enter the teacher for timeslot (9am - 10am): ")
            timeslot3_subject = input("Enter the subject for timeslot (10am - 11am): ")
            timeslot3_teacher = input("Enter the teacher for timeslot (10am - 11am): ")
            timeslot4_subject = input("Enter the subject for timeslot (11am - 12pm): ")
            timeslot4_teacher = input("Enter the teacher for timeslot (11am - 12pm): ")
            timeslot5_subject = input("Enter the subject for timeslot (12pm - 1pm): ")
            timeslot5_teacher = input("Enter the teacher for timeslot (12pm - 1pm): ")

            new_data = {
            'timeslot': [timeslot1, timeslot2, timeslot3, timeslot4, timeslot5], 
            'subject': [timeslot1_subject, timeslot2_subject, timeslot3_subject, timeslot4_subject, timeslot5_subject],
            'teacher': [timeslot1_teacher, timeslot2_teacher, timeslot3_teacher, timeslot4_teacher, timeslot5_teacher], 
            }

            schedule_info = pd.DataFrame(new_data)

            schedule_info.to_csv(f"data/schedule/{class_name} - {day}.csv", index=False)

            print(f"Schedule for {class_name} on {day} succesfully created!")
            print()

    def generate_reports(self):
        print("1. Generate Attendance Report")
        print("2. Generate Performance Report")
        print()
        report_option = input("Select an option (1 to 2): ")

        existing_data = pd.read_csv('data/student.csv', dtype={'contact': str, 'age': int}) 

        existing_data['student_id'] = existing_data['student_id'].astype(str)

        while True:
            if report_option == '1':

                while True:
                    student_id = input("Enter Student ID: ")
                    
                    if student_id not in existing_data['student_id'].values:
                        print(f"ERROR Student ID {student_id} does not exist! Try again.")
                    else:
                        break

                if not os.path.exists('data/report/attendance'):
                    os.makedirs('data/report/attendance')

                attendance_data = []

                for filename in os.listdir('data/attendance'):
                    file_name_section = filename.split(" - ")
                    date = file_name_section[0]
                    existing_data= pd.read_csv(f'data/attendance/{filename}', dtype={'student_id': str})

                    student_index = existing_data[existing_data['student_id'] == student_id].index[0]
                    
                    attendance_value = existing_data.loc[student_index, 'attendance']
                    attendance_data.append({'date': date, 'attendance': attendance_value})

                report = pd.DataFrame(attendance_data)
                report.to_csv(f"data/report/attendance/{student_id}.csv", index=False)
                
            elif report_option == '2':

                while True:
                    student_id = input("Enter Student ID: ")
                    
                    if student_id not in existing_data['student_id'].values:
                        print(f"ERROR Student ID {student_id} does not exist! Try again.")
                    else:
                        break

                year = input("Enter the year: ")
                semester = input("Enter the semester: ")

                if not os.path.exists('data/report/performance'):
                    os.makedirs('data/report/performance')
                
                performance_data = []

                for filename in os.listdir('data/marks'):
                    if filename.startswith(f"semester {semester} - {year}"):
                        file_name_section = filename.split(" - ")
                        subject = file_name_section[2]
                        subject_part = subject.split(".")
                        subject_name = subject_part[0]
                        existing_data= pd.read_csv(f'data/marks/{filename}', dtype={'student_id': str})

                        student_index = existing_data[existing_data['student_id'] == student_id].index[0]
                        
                        subject_marks = existing_data.loc[student_index, 'marks']
                        performance_data.append({'subject': subject_name, 'marks': subject_marks})

                    else:
                        continue

                report = pd.DataFrame(performance_data)
                report.to_csv(f"data/report/performance/{student_id} - semester {semester} - {year}.csv", index=False)

            else:
                print("Invalid option.")

            break

    def generate_stats(self):
        student_data = pd.read_csv('data/student.csv', dtype={'student_id': str, 'class_name': str})
 
        student_id = input("Enter the student ID: ").strip()

        if student_id not in student_data['student_id'].values:
            print("ERROR: Class not found.")
            return

        year = input("Enter the year: ").strip()
        semester = input("Enter the semester (1, 2, 3): ").strip()

        marks_file = f"data/report/performance/{student_id} - semester {1} - {year}.csv"

        if not os.path.exists(marks_file):
            print("ERROR: Marks file not found.")
            return

        marks_data = pd.read_csv(marks_file, dtype={'subject': str, 'marks': float})

        class_marks = marks_data['marks'].to_numpy()

    # Compute performance statistics
        avg_marks = np.mean(class_marks)
        std_dev = np.std(class_marks)
        highest_mark = np.max(class_marks)
        lowest_mark = np.min(class_marks)

        # Grade Distribution
        grade_A = np.sum(class_marks >= 80)
        grade_B = np.sum((class_marks >= 70) & (class_marks < 80))
        grade_C = np.sum((class_marks >= 60) & (class_marks < 70))
        grade_D = np.sum((class_marks >= 50) & (class_marks < 60))
        grade_F = np.sum(class_marks < 50)

        # Display results
        print("\nClass Performance Analytics:")
        print(f" Student: {student_id}")
        print(f" Year: {year} | Semester: {semester}")
        print(f" Average Marks: {avg_marks:.2f}")
        print(f" Standard Deviation: {std_dev:.2f}")
        print(f" Highest Mark: {highest_mark}")
        print(f" Lowest Mark: {lowest_mark}")
        print(" Grade Distribution:")
        print(f"   A (80+): {grade_A}")
        print(f"   B (70-79): {grade_B}")
        print(f"   C (60-69): {grade_C}")
        print(f"   D (50-59): {grade_D}")
        print(f"   F (<50): {grade_F}\n")