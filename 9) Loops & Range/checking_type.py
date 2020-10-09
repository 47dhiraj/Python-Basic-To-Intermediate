#CHECKING TYPE -> using isinstance function
'''
def factorial(n):
    if not isinstance(n, int):        #input diyeko n chai integer ho ki nai check garna inbuit function isinstance use gareko
        print("factorial is only define for integers.")
        return     #yaha batw kei pai value integer navayeko vayera output aauda None pani sangai aauxai
    elif n<0:
        print("factorial is only defined for positive integers.")
        return -1

    elif n== 1 or n== 0:
        return 1
    else:
        return n* factorial(n-1)

result = factorial(1.5)
print(result)

'''

def factorial(n):
    if not isinstance(n, int):        #input diyeko n chai integer ho ki nai check garna inbuit function isinstance use gareko
        print("factorial is only define for integers.")
        return         
    elif n<0:
        print("factorial is only defined for positive integers.")
        return -1

    elif n== 1 or n== 0:
        return 1
    else:
        return n* factorial(n-1)

result = factorial(5)
print(result)
