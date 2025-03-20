from person import Person

class Student(Person):
    
    def __init__(self, id, password, contact, email, class_name, age):
        super().__init__(id, password)
        self.class_name = class_name
        self.age = age
        self.contact = contact
        self.email = email
