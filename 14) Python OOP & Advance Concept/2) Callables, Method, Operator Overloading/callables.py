#Non callable object

class Test1:
    def __init__(self,a):
        self.a = a
    
    def __call__(self):               #yo chai kunnai object lai callable banauna milne inbuilt python function ho
        print("You have called an object")

t1 = Test1(12)
t1()           #yo chai object lai call gareko 
