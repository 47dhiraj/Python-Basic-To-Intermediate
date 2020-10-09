#FIRST WAY, importin all function and identifiers from module1
'''
import module1
sum_result = module1.sum(1,1)
substract_result = module1.substract(1,1)

print("sum",sum_result)
print("Substract", substract_result)
print("name", module1.name)
print ("address",module1._address)
module1._test()
'''
  

# SECOND WAY , importing selected function and identifiers ones form module
'''
from module1 import sum, substract, _test, name, _address
sum_result = sum(1,1)
substract_result = substract(1,1)
 
print("sum",sum_result)
print("Substract", substract_result)
print("name", name)
print("address", _address)
_test()
'''

#THIRD WAY, imports all functions and identifiers except fukctions starting with _ .
'''
from module1 import *
sum_result = sum(1,1)
substract_result = substract(1,1)

print("sum",sum_result)
print("Substract", substract_result)
print("name", name)
#print("address", _address) .....yo line ma eroor aauxa because underscore xa
#_test() .... yo line ma error aauxa because underscore xa
'''


#FOURTH WAY, import all function and identifier by renaming
'''

from module1 import sum as add, substract as minus, name as n, _address as a 

sum_result = add(1,1)
substract_result = minus(1,1)

print("sum",sum_result)
print("Substract", substract_result)
print("name", n)
print("address",a)
'''
import module1
print(dir(module1)) #dir vanni function le module1 vitra k k xa vanera display garauxa
print(module1.__name__) #jun module batw kura extract gareko xa tesko naam display garauxa





