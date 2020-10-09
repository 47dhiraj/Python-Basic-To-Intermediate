#Memo ma 'dictionary' data structure use garincha

memo = {0:0,1:1}
def fibonacci(n):
    if n in memo:
        return memo[n]
    else:
        result=fibonacci(n-1)+fibonacci(n-2)
        memo[n]=result
        return result
nterm=4
print("Fibonacci Sequence:")

for i in range(nterm):
        print(fibonacci(i))

