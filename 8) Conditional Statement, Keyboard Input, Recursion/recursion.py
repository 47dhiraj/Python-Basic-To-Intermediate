#INFINITE RECURSION
'''

def test():
    test()

test()
 
'''

#Factorial using Recursion function
'''
def factorial(n):
    if n == 1:   #yo line ko condition lai chai base condition of recursion function vaninxa
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5) #yo line le mathi ko factorial definition lai call garxa
print(result)
'''
#Fibonacci using Recursion function

