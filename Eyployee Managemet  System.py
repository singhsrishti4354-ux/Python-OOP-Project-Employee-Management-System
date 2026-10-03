print("--- Python OOP Project : Employee Management System ---")
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    # def show_details(self):
    #     print("Name:",self.name)
    #     print("Age:",self.age)

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        Person.__init__(self,name,age)
        self.employee_id=employee_id
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        Employee.__init__(self,name,age,employee_id,salary)
        self.department=department
# print("--- Python OOP Project : Employee Management System ---")
while True:
    print("\nChoose an Operation:")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")
    choice =int(input("Enter Your Choice:"))

    if choice==1:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        person1=Person(name,age)
        print(f"Person Created:{person1.name} , Age: {person1.age}")
        print("\n--Choose another operation--")

    elif choice==2:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        employee_id=input("Enter Employee ID:")
        salary=float(input("Enter Salary:"))
        employee1=Employee(name,age,employee_id,salary)
        print(f"Employee Created:{employee1.name} , Age: {employee1.age}, Employee ID: {employee1.employee_id}, Salary: {employee1.salary}")
        print("\n--Choose another operation--")

    elif choice==3:
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        employee_id=input("Enter Employee ID:")
        salary=float(input("Enter Salary:"))
        department=input("Enter Department:")
        manager1=Manager(name,age,employee_id,salary,department)
        print(f"Manager Created:{manager1.name} , Age: {manager1.age}, Employee ID: {manager1.employee_id}, Salary: {manager1.salary}, Department: {manager1.department}")
        print("\n--Choose another operation--")

    elif choice==4:
        print("Details Of Created Employees and Managers:")
    elif choice==5:
        print("Exiting The Program.GoodBye!")
    break

