# task 1> student class- class and object
# your task:
#*>create a class student with atributes name,roll_no,and course.
#*>create a method display_student()that prints all students details.
#*>create at least five students objects with diffrent value.
#*>call display_studnet() for both objects.


# class student: #student class creation

#     # constructor to initialize the value of the class 
#     def __init__(self,n,roll,c):
#         self.name = n
#         self.roll_no  = roll
#         self.course = c

#     def display_student(self): #method to display the value of the class
#         print(f"name:{self.name}")
#         print(f"roll no:{self.roll_no}")
#         print(f"course:{self.course}")
#         print("=-="*50)   #print a blank line for batter readability

    
# s1 = student("Megharaj",101,"python full stack")    #creating an object of student class
# s2 = student("Dipak",102,"java full stack")       #creating an object of student class
# s3 = student("Jagruti",103,"data science using python")         #creating an object of student class
# s4 = student("Tushar",104,"python GI dev")   #creating an object of student class
# s5 = student("Nikhil",105,"java scripy full stack")       #creating an object of student class

# s1.display_student()
# s2.display_student()
# s3.display_student()
# s4.display_student()
# s5.display_student()


# task 2> Task 2: Employee – Constructor (__init__) 
# class employee:  #create class
#     def __init__(self,i,n,d,s):
#         self.id = i
#         self.name = n
#         self.department = d
#         self.salary = s
#     def display_details(self): #create method
#         print(f"ID :{ self.id}")
#         print(f"Name :{self.name}")
#         print(f"Departement :{self.department}")
#         print(f"Salary :{self.salary}")
#         print("-" * 25)

# e1 = employee(101,"Megharaj Desale","IT",1000000)
# e2 = employee(102,"Dipak Desale","HR",200000)
# e3 = employee(103,"Jagruti Desale","dev",300000)

# e1.display_details()
# e2.display_details()
# e3.display_details()


# task 3>  Bank Account – Instance Methods 
# Class that represents a bank account
# class BankAccount:

#     # Constructor: sets the values when the object is created
#     def __init__(self, a_no, h_name, bal):
#         self.account_number = a_no
#         self.holder_name = h_name
#         self.balance = bal
#         self.transaction_history = []          # empty list to store transactions

#     # Method to add money
#     def deposit(self, amount):
#         if amount > 0:                         # amount must be positive
#             self.balance += amount             # add to balance
#             self.transaction_history.append(f"Deposited: {amount}")   # save in history
#             print(f"Deposited: {amount}")
#         else:
#             print("Deposit amount must be positive.")

#     # Method to take out money
#     def withdraw(self, amount):
#         if amount <= 0:                        # check for invalid amount
#             print("Withdrawal amount must be positive.")
#         elif amount <= self.balance:           # withdraw only if enough balance
#             self.balance -= amount             # subtract from balance
#             self.transaction_history.append(f"Withdrawn: {amount}")   # save in history
#             print(f"Withdrawn: {amount}")
#         else:
#             print("Insufficient balance!")     # not enough money

#     # Method to show the current balance
#     def check_balance(self, label="Current Balance"):
#         print(f"{label}: {self.balance}")

#     # Method to show all transactions
#     def show_history(self):
#         print("Transaction History:")
#         for t in self.transaction_history:     # loop through every transaction
#             print("-", t)


# # ---------- Testing ----------

# acc = BankAccount(101, "Megharaj", 10000)

# acc.check_balance("Initial Balance")   # Initial Balance: 10000
# acc.deposit(3000)                      # Deposited: 3000
# acc.withdraw(2500)                     # Withdrawn: 2500
# acc.check_balance()                    # Current Balance: 10500
# acc.show_history()                     # print all transactions


# task 4> : Inheritance – Employee and Developer 

# Parent class: stores common details of an employee
class Employee:

    # Constructor: sets name and salary
    def __init__(self, n, s):
        self.name = n                  # store employee name
        self.salary = s                # store employee salary

    # Method to show basic employee details
    def display_info(self):
        print(f"Name : {self.name}")
        print(f"salary :{self.salary}")


# Child class: Developer inherits everything from Employee
# class Developer(Employee):

#     # Constructor: sets name, salary and programming language
#     def __init__(self, n, s, p):
#         Employee.__init__(self, n, s)  # call parent constructor to set name and salary
#         self.programming_language = p  # store programming language (extra attribute)

#     # Method to show all developer details
#     def show_developer_info(self):
#         self.display_info()            # call parent method (shows name and salary)
#         print(f"Programming Language :{self.programming_language}")


# # ---------- Testing ----------

# # Create a Developer object: name, salary, language
# dev = Developer("Megharaj", 300000, "Python")

# # Display all information
# dev.show_developer_info()

# Task 5: Method Overriding – Vehicle System 
# Parent class: common base for all vehicles
class Vehicle:

    # Method to start the vehicle (general behavior)
    def start(self):
        print("Vehicle is starting")


# Child class: Car inherits from Vehicle
class Car(Vehicle):

    # Override start() with Car's own behavior
    def start(self):
        print("Car starts with a key or push button")


# Child class: Bike inherits from Vehicle
class Bike(Vehicle):

    # Override start() with Bike's own behavior
    def start(self):
        print("Bike starts with a kick or self-start")


# ---------- Testing ----------

# Create objects
v = Vehicle()
c = Car()
b = Bike()

# Same method name, different behavior
v.start()
c.start()
b.start()



# Task 6: Mini Project – Employee Management System 

# Parent class: stores common details of an employee
class Employee:

    # Constructor: sets id, name and salary
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id     # store employee id
        self.name = name                   # store employee name
        self.salary = salary               # store employee salary

    # Method to show basic employee details
    def display_info(self):
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")


# Child class: Developer inherits from Employee
class Developer(Employee):

    # Constructor: sets common details and programming language
    def __init__(self, employee_id, name, salary, programming_language):
        Employee.__init__(self, employee_id, name, salary)   # call parent constructor
        self.programming_language = programming_language     # store language

    # Override display_info() to add developer details
    def display_info(self):
        print("Role: Developer")
        Employee.display_info(self)                          # reuse parent method
        print(f"Programming Language: {self.programming_language}")


# Child class: Tester inherits from Employee
class Tester(Employee):

    # Constructor: sets common details and testing tool
    def __init__(self, employee_id, name, salary, testing_tool):
        Employee.__init__(self, employee_id, name, salary)   # call parent constructor
        self.testing_tool = testing_tool                     # store testing tool

    # Override display_info() to add tester details
    def display_info(self):
        print("Role: Tester")
        Employee.display_info(self)                          # reuse parent method
        print(f"Testing Tool: {self.testing_tool}")


# ---------- Testing ----------

# Create two developers and two testers
dev1 = Developer(101, "Megharaj", 30000, "Python")
dev2 = Developer(102, "dipak", 35000, "Java")
test1 = Tester(201, "Jagruti", 28000, "Selenium")
test2 = Tester(202, "Madhuri", 27000, "Postman")

# Store all objects in one list
employees = [dev1, dev2, test1, test2]

# Loop through the list and display details
for emp in employees:
    emp.display_info()                     # correct method runs for each object
    print("-" * 25)                         # separator line




        