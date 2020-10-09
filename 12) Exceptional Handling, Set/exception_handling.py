#example: print(something/0)  i.e infinity hunxa so exception auxa
#exception aauda program exection stop hunxa

#handling the exception using "try" & "except" 
#exception aaune khako code "try" vitra lekhinxa
#exception aayepaxi "except" le aba k garni vanera bujauxa

'''

#Task1
print("Doing task 1")
a =12/0        # yo line execute huda exception aauxa & then program execution stop

print("Doing task 2")       #yo line execute nai hudaina



#Task2
try:
    print("Before dividing 12 by 0")
    a = 12/0                      #yo statement le exception create garxa... so siddai line no.23 ma janxa
    print("After dividing .......")
except:                          #receiving the exception and doing the task
    print("exception occurred")

'''

'''

#Task 3
print("Now u can do Task 3")

try:
    b = 12/0
    #a=[]
    #print(a[1])

   # result = open('fgg.txt', 'r')


except IndexError as ie:         #yo IndexError chai python inbuilt exception ho
    print("index Error exception occured")
    print(ie)

except ZeroDivisionError:            #yo ZeroDivisionError chai python ibuilt exception ho
    print("Zero division error Exception")

except:
    print("other exceptions")

'''


'''
#Catching multiple exceptions in one except
try:
    a=[]
    result = a[0]
except(IndexError, ArithmeticError):       #yo line le multiple statement catch garxa
    print("Exception")

'''


#using else: block
try:
    a=[]
    result=a[0]
    
except(IndexError, ArithmeticError):
    print("Exception")
    
else:
    print("No exception")

finally:    # yo finally vitra agadi exception aaye pani na aaye pani j code vaye pani run hunxa
    print("Clearing Resource")















