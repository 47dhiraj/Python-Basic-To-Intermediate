import datetime
def fibonacci(n):
    if n<= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nterms = 10
print("Fibonacci sequence:")
start_time = datetime.datetime.now()
for i in range(nterms):
    print(fibonacci(i))

end_time = datetime.datetime.now()
time_diff = end_time - start_time
print(time_diff)