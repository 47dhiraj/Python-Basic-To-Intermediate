def compose(f,g):    #duita function f & g lai compose garna khojeko
    return lambda x: f(g(x))

def add(x):
    return x+1

def multiply(x):
    return x*2

new_func = compose(add, multiply)    #suru ma multiply hunxa ani tespaxi addition hunxa
print(new_func(2))




