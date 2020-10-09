def test3():
    print("inside of test3 function")

def test2():
    test3()
    print("inside of test2 function")

def test1():
    test2()
    print("inside of test1 function")

test1()

print("after test1 function")



