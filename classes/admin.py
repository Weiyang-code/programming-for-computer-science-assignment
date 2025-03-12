import pandas as pd
from classes.person import Person

class Admin(Person):

    def __init__(self, name, password):
        super().__init__(name, password)
    
    import pandas as pd

    def add_employee(self):
        # Load existing employee data
        existing_data = pd.read_csv('data/employee.csv', dtype={'employee_id': str})  

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


    def remove_employee(self):
        data = pd.read_csv('data/employee.csv') 

        data['employee_id'] = data['employee_id'].astype(str)

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

    def update_employee():
        pass     

    def view_employee(self):
        employee_list = pd.read_csv('data/employee.csv', dtype = {'contact' : str})    
        print(employee_list.to_string())
        print()        

    def add_student():
        pass

    def remove_student():
        pass

    def update_student():
        pass

    def view_student():
        pass

    def schedule_class():
        pass

    def generate_reports():
        pass

    def generate_stats():
        pass