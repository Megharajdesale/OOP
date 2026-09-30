# Problem Statement
# A college has students and teachers.
# A Student has roll, name, marks, and address.
# A Teacher has name, salary, department, and address.

class Student:
    def __init__(self, roll, name, marks, address):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.address = address

    def display(self):
        print("--- Student Details ---")
        print(f"Roll No : {self.roll}")
        print(f"Name    : {self.name}")
        print(f"Marks   : {self.marks}")
        print(f"Address : {self.address}")


class Teacher:
    def __init__(self, name, salary, dept, address):
        self.name = name
        self.salary = salary
        self.dept = dept
        self.address = address

    def display(self):
        print("--- Teacher Details ---")
        print(f"Name       : {self.name}")
        print(f"Salary     : {self.salary}")
        print(f"Department : {self.dept}")
        print(f"Address    : {self.address}")


# Objects create 
s1 = Student(101, "Megharaj", 86, "Pune")
s2 = Student(102, "Dipak", 78, "Dhule")

t1 = Teacher("Atul Sir", 300000, "Computer Science", "Pune")

# Method call 
s1.display()
s2.display()
t1.display()