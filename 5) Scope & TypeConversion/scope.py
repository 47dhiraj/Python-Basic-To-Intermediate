#1> Locsl scope
#2> Global scope

def print_message():
    message = "hello !! I am going to print a message. " #this message is local to the print_message function 
    print(message)

print_message()   #yo calling statement le chai function lai call garxa

# print(message)        #This statement will cause an error, since a local variable cannot be accessible here




#GLOBAL scope and LOCAL scope both

def calculate(*args):
    sum=0                  #local variable
    for arg in args:
        sum= sum+arg
        print("The sum is",sum) #YO SUM KO VALUE LOCAL VARIABLE KO VALUE

sum=0              #global varibale

calculate(10,20,30)
print("Value of sum outside the function:",sum)  #yo statement ma sum ko value vaneko global varibale


#PROBLEMATIC SCOPE
'''
sum=2
def test():
    sum= sum+2 #yo statement ko sum local variable ho jun chai function definition ma sum ko value initialize gareko xaina
    print(sum)

test()


print(sum)

'''

#Solution of above problematic scope

sum=2
def test():
    global sum
    sum= sum + 2 #yo statement ko sum local variable ho jun chai function definition ma sum ko value initialize gareko xaina
    print(sum)

test()

print(sum)


