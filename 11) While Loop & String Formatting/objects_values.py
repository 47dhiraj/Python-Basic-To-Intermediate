#TO be noted : string is mutable i.e same value of differnet object refer to same memory location
# to be noted : list is immutable i.e same value of different object refer to different memory location

'''
#string's case
a = "banana"
b="banana"
print(a == b)
print(a is b)


#list's case
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)
'''


#ALIASING

a = [1,2,3]
b = a                 #mutable ho list so same memory location of both a & b
print(a is b)


b[1] = 5             #list is mutable so can be modified easily
print(a)
print(b)



