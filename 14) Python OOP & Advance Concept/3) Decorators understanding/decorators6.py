def name_dept(func):     #khas yo function ma aaune vaneko chocolate_dept() ko iiner function wheat_cream_and_choc() function ho
    def wheat_cream_choc_and_name():
        func()
        print("Name dept working")
    return wheat_cream_choc_and_name

def chocolate_dept(func):      #kkhas yo function ma aaune vaneko  cream_dept() ko inner function wheat_and_cream() ko return vale ho
    def wheat_cream_and_choc():
        func()
        print("Chocolate dept working")
    return wheat_cream_and_choc

def cream_dept(func):         #khas yo function ma aaune vaneko external wheat_dept() ho
    def wheat_and_cream():
        func()
        print("Cream Dept working")
    return wheat_and_cream

@name_dept
@chocolate_dept
@cream_dept
def wheat_dept():
    print("Wheat Dept working")

wheat_dept()