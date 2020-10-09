# SYNTAX: reduce(function, sequence[, initial]) -> value

#reduce function composition without initial value
'''
from functools import reduce

def do_sum(x1,x2):
    return x1+ x2

x = reduce(do_sum, [1,2,3,4])  #yo line ko do_sum le chai function call garxa ,,,, baki tyo list ma vayeko sequence number hary chai x1,x2 ma parameter jasari pass hunxa

print(x)

'''


#reduce function composition with initial value

from functools import reduce

def do_sum(x1,x2):
    return x1+ x2

x = reduce(do_sum, [1,2,3,4],10)  #yo line ko do_sum le chai function call garxa ,,,, baki tyo list of tuple ma vayeko sequence number hary chai x1,x2 ma parameter jasari pass hunxa

print(x)





