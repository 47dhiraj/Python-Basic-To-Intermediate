def compose(h,f,g):    
    return lambda x: h(f(g(x)))

def sub(x):
    return x-1

def add(x):
    return x+1

def multiply(x):
    return x*2

new_func = compose(add, multiply, sub)   
print(new_func(2))




