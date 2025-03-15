import os
import pandas as pd
from classes.person import Person

class Teacher(Person):
    
    def __init__(self, name, password):
        super().__init__(name, password)

    def mark_attendance(self):
        existing_data = pd.read_csv('data/student.csv', dtype={'contact': str, 'age': int}) 

        date = input("Enter date (eg: 5/6/2025, 27/5/2025): ").strip().replace("/", "_")

        class_name = input("Enter class name: ")

        if os.path.exists(f'data/{date} - {class_name} - attendance.csv'):
            pass

        else:
            pd.DataFrame(columns=['student_id', 'name', 'attendance']).to_csv(f'data/{date} - {class_name} - attendance.csv', index=False)

            filtered_students = existing_data[existing_data['class_name'] == class_name]

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
            df_attendance.to_csv(f"data/{date} - {class_name} - attendance.csv", index=False)

        print("Attendance marked succesfully!")
        print()

    def view_attendance():
        pass

    def add_student_marks():
        pass

    def update_student_marks():
        pass

    def generate_performance_analytics():
        pass

    def update_teacher_profile():
        pass

    def manage_class_schedule():
        pass

    def create_lesson_plan():
        pass