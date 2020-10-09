#Note: Both lambda & reduce le function return garxa

from functools import reduce

def test(*functions):
    def apple(f,g):
        print("combining {} and {}".format(f,g))
        return lambda x: f(g(x))
    return reduce(apple, functions)  #step 2: direct yo reduce function batw apple function call hunxa
                                        #step3: apple function call vayesi tesma f ko thau ma dec  &  g ko thau ma double dinxa


def double(x):
    return x*2

def inc(x):
    return x +1

def dec(x):
    return x - 1

final_function = test(dec, double, inc)  #step 1: yaha batw mathi ko test multiple function compostion cal hunxa
x = final_function(10)

print(x)

