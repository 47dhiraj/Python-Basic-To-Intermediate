
#Fibonacci without using recursion
'''
n = int(input("How many numbers do u want to calculate fibonacci ? "))

n1 =0
n2 =1

if n ==1:
    print(n1)

elif n==2:
    print(n2)

else:
    for i in range(n):
        print(n1,"\n")
        nth = n1 + n2
        n1 =n2
        n2 = nth

'''

# Python program to display the Fibonacci sequence up to user input nth term using recursive functions

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))


n = int(input("How many numbers do u want to calculate fibonacci ? "))

if n <= 0:                 # check if the number of terms is positive or greater than 0
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print(fibo(i))






 