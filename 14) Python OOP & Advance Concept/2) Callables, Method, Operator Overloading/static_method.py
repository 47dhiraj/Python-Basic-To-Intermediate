#static methods

class Test:

    def __init__(self,name):
        self.name = name

    @staticmethod              #static method ko mathi yo line lekhna parxa.... just denote gareko yo tala ko method chai static ho vanera
    def show():
        print("Inside show static method")

t = Test("broadway")          #creating t object

Test.show()         #static method call garna ko lagi directly class ko name ani '.' garera function name 
