from person import Person

class Teacher(Person):
    
    def __init__(self, name, employee_id, email, contact, salary, subject_classes):
        super().__init__(name, email, contact)
        self.employee_id = employee_id
        self.email = email
        self.contact = contact
        self.salary = salary
        self.subject_classes = {}

    def mark_attendance():
        pass

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