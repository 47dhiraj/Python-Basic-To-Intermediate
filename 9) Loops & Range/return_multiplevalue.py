'''
#FIRST WAY

def calculate(a,b):
    sum = a+b
    substract =a -b
    return sum, substract   #returning multiple values (i.e TUPLE) from a function

result1= calculate(1,2)
print(result1)


#SECOND WAY

def calculate(a,b):
    sum = a+b
    substract =a -b
    return sum, substract   #returning multiple values (i.e TUPLE) from a function

result1, result2= calculate(1,2)  #yo statement ma calculate ma aayeko both values lai result1 & result2 ma halxa so yesto process lai unwrapping vaninxa

print(result1)
print(result2)

'''




