from person import Person

class Student(Person):
    
    def __init__(self, name, contact, email, student_id, class_name, subject_marks, age):
        super().__init__(name, email, contact)
        self.student_id = student_id
        self.class_name = class_name
        self.subject_marks = {}
        self.age = age