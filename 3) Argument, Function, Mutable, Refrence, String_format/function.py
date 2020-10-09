def hello_world():
    print("hello world")   #identation dinu parxa definition ko body lekhda....no parenthesis is used...Uniform identation dinu parxa

hello_world()


#parameter passing
def showName(name):                      #definition having name as parameter
    print("Hello! {0}".format(name))

showName("Dhiraj Kafle")       #calling function by passing argument


#Multiple parameter passing
def showName(name,age):                      #definition having name & age as parameter
    print("Hello! {0}. Your age is {1}.".format(name,age))

showName("Dhiraj Kafle",23)       #calling function by passing multiple argument





