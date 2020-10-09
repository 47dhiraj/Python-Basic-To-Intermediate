#calling parent's constructor with parameters
class Employee:   
    def __init__(self, salary):  
        self.salary = salary
        self.position = "employee"
        self.department = "Account"

    
class BankEmployee(Employee):
    def __init__(self, name, sal):
        super().__init__(sal)
        self.name = name
        print(self.salary)
        print(self.position)
    

emp = BankEmployee("Ram", 2000)
print(emp.department)