class User:
    def __init__(self, name, email, user_id):
        self.name=name
        self.email=email
        self.user_id=user_id
    def login(self):
        return f"(self.name) logged in"
    
class student(User):
    def enroll_course(self,course_name):
        self.course_name = course_name
        return f"course name is {self.course_name}"

class teacher(User):
    def create_course(self,course_name):
        self.course_name = course_name
        return f"student {self.name} enrolled in {self.course_name}"
    
    def login(self):
        return f"student {self.name} logged in"
    
student1 = student("abc","abc@gmail",101)
print(student1.login())
print(student1.enroll_course("python"))

teacher1 = teacher("xyz","xyz@gmail",102)

print(teacher1.login())
print(teacher1.create_course("python"))