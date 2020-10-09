#calling parents constructor with parameters
class employee:
    def __init__(self,salary):
        self.salary=salary
class bankemployee(employee):
    def __init__(self,name,salary):
        super().__init__(salary)#this should be in first line of child constructor which excess teh parents property
        self.name=name
emp=bankemployee("ram",2000)
#print(emp.name)
print(emp.salary)