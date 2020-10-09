#Raising error by user themselves

def validate_age(age):
    if age < 18:
        error = ValueError("Age must be greater than 18 to vote.")  #yo line ko ValueError vaneko user aafaile error generate garna ko lagi python le diyeko inbuilt functio ho
        raise error            #yaha batw error raise vayera siddai line no 15 ma janx

    print("Your age is Valid")       #exception na aaye matra yo statment execute hunxa 

age= int(input("Enter your age"))

try:
    validate_age(age)

except ValueError:        #error aaye paxi run hunxa yo
    print("Value error occured")


