#decorators auta yesto funciton jasle function nai linxa & tesma certain functionality (add)halera return garxa

def make_pretty(func):            #yo make_pretty() function chai khas ma decorator ho ... jasle auta function receive garxa and tyo receive gareko ma certain functionality halxa
    def inner():
        func()             #ordinary function lai feri call gareko
        print("I got decorated ")

    return inner

def ordinary():
    print("I am ordinary")

#calling a function directly
print("Calling function directly...")
ordinary()


#using the concept of decorators
pretty = make_pretty(ordinary)       #calling make_preety() decorator by passing function name ordinary    #yaha pretty chai function ho ..jasma function nai return aayera baseko xa

print("Using decorator.....")
pretty()











