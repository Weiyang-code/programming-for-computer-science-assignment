import os
import pandas as pd
from classes.admin import Admin
from classes.teacher import Teacher

class School:
    
    def menu(self):

        employee_path = 'employee.csv'
        student_path = 'student.csv'

        if not os.path.exists("data"):
            os.makedirs("data")

        if os.path.exists(f"data/{employee_path}"):
            pass
        else:
            pd.DataFrame(columns=['employee_id', 'name', 'email', 'contact', 'salary', 'position']).to_csv(f"data/{employee_path}", index=False)

        if os.path.exists(f"data/{student_path}"):
            pass
        else:
            pd.DataFrame(columns=['student_id', 'name', 'contact', 'email', 'class_name', 'age']).to_csv(f"data/{student_path}", index=False)

        user = input("Are you an admin or teacher? (Admin/Teacher): ").lower().strip()

        if user == 'admin':
            admin1 = Admin(name = input("Enter Your Username: "), password = input("Enter Your password: "))
            while True:
                print()
                print("Admin Menu: ")
                print()
                print("1. Employee Management")
                print("2. Student Management")
                print("3. Class and Schedule Management")
                print("4. Exit")
                print()
                opt = input("Select an option (1 to 4): ")
                print()

                if opt =='1':
                    while True:
                        print("Employee Management Menu:")
                        print()
                        print("1. Add Employee")
                        print("2. Remove Employee")
                        print("3. Update Employee")
                        print("4. View Employees")
                        print("5. Back to Admin Menu")
                        print()
                        employee_opt = input("Select an option (1 to 5): ")
                        print()

                        if employee_opt == '1':
                            admin1.add_employee()

                        elif employee_opt == '2':
                            admin1.remove_employee()
                        
                        elif employee_opt == '3':
                            admin1.update_employee()

                        elif employee_opt == '4':
                            admin1.view_employee()

                        elif employee_opt == '5':
                            break

                elif opt == '2':
                    while True:
                        print("Student Management Menu:")
                        print()
                        print("1. Add Student")
                        print("2. Remove Student")
                        print("3. Update Student")
                        print("4. View Student")
                        print("5. Back to Admin Menu")
                        print()
                        student_opt = input("Select an option (1 to 5): ")
                        print()   

                        if student_opt == '1':
                            admin1.add_student()

                        elif student_opt == '2':
                            admin1.remove_student()
                        
                        elif student_opt == '3':
                            admin1.update_student()

                        elif student_opt == '4':
                            admin1.view_student()

                        elif student_opt == '5':
                            break

                elif opt == '3':
                    while True:
                        print("Class and Schedule Management Menu:")
                        print()
                        print("1. Schedule Class")
                        print("2. Generate Reports")
                        print("3. Generate Statistical Insights")
                        print("4. Back to Admin Menu")
                        print()
                        class_opt = input("Select an option (1 to 4): ")
                        print()

                        if class_opt == '1':
                            admin1.schedule_class()

                        elif class_opt == '2':
                            admin1.generate_reports()

                        elif class_opt == '3':
                            admin1.generate_stats()

                        elif class_opt == '4':
                            break

                elif opt == '4':
                    print("You are exiting the system.")
                    break
        
        elif user == 'teacher':
            teacher1 = Teacher(name = input("Enter Your Username: "),  password = input("Enter Your password: "))

            while True:
                print()
                print("Teacher Menu: ")
                print()
                print("1. Attendance Management")
                print("2. Student Assessment & Grading")
                print("3. Profile & Task Management")
                print("4. Exit")
                print()
                opt = input("Select an option (1 to 4): ")
                print()

                if opt == '1':
                    while True:
                        print("Attendance Management Menu:")
                        print()
                        print("1. Mark Attendance")
                        print("2. View Attendance Reports")
                        print("3. Back to Teacher Menu")
                        print()
                        attendance_opt = input("Select an option (1 to 3): ")
                        print()
                        
                        if attendance_opt == '1':
                            teacher1.mark_attendance()

                        elif attendance_opt == '2':
                            teacher1.view_attendance()
                    
                        elif attendance_opt == '3':
                            break

                elif opt =='2':
                    while True:
                        print("Student Assessment & Grading Menu:")
                        print()
                        print("1. Add Student Marks")
                        print("2. Update Student Marks")
                        print("3. Generate Performance Analytics")
                        print("4. Back to Teacher Menu")
                        print()
                        marks_opt = input("Select an option (1 to 4): ")
                        print()

                        if marks_opt == '1':
                            teacher1.add_student_marks()

                        elif marks_opt == '2':
                            teacher1.update_student_marks()
                        
                        elif marks_opt == '3':
                            teacher1.generate_performance_analytics()

                        elif marks_opt == '4':
                            break

                elif opt == '3':
                    while True:
                        print("Profile & Task Management Menu: ")
                        print()
                        print("1. Update Teacher Profile")
                        print("2. Manage Class Schedules")
                        print("3. Create Lesson Plans")
                        print("4. Back to Teacher Menu")
                        print()
                        profile_opt = input("Select an option (1 to 4): ")
                        print()   

                        if profile_opt == '1':
                            teacher1.update_teacher_profile()

                        elif profile_opt == '2':
                            teacher1.manage_class_schedule()
                        
                        elif profile_opt == '3':
                            teacher1.create_lesson_plan()

                        elif profile_opt == '4':
                            break

                elif opt == '4':
                    print("You are exiting the system.")
                    break



                        