#calling parent's constructor from child class construcotr

class Employee:
    def __init__(self):
        self.salary = 2000

class BankEmployee(Employee):
    def __init__(self, name):
        super().__init__()        #yo line ko super() le i.e parent ko constructor lai pani call garxa....& yo line jahile child class ko construnctor ko just tala ko line ma lekhna parxa
        self.name = name


emp = BankEmployee("Ram")
print(emp.name)

print(emp.salary)
