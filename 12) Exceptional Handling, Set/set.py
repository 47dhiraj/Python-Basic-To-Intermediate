'''
#is a sequence that can store elements.
#it is mutable
#it has no ordering i.e indexing garnu mildaina element lai
#it consists of unique elements (duplicate element basdaina)

#creating  a set
a = {1,2,3}
print(a)
print(type(a))

#creating EMPTY set
a = set()
print(a)
print(type(a))


#set can consist of unique elements only (set ma repeated same element halna mildaina)
a={1,2,3,1}
print(a)


#iteration in the set
a ={1,2,3,1}
for item in a:
    print(item)


#deleting or removing element of set by using remove inbuilt function
a={1,2,3}
a.remove(3)
#a.remove(3)       #remove vai sakeko item feri pani remove garna khojyo vani throws error or exception 
print(a)


#removing element by using discard inbuilt function 
a={1,2,3}
a.discard(2)
a.discard(2)   #discard ko remove vako item feri remove garna khoje pani error faldaina
print(a)
'''


'''
#for finding UNINON(U) of element of set
a={1,2,3}
b={3,4,2}
c = a.union(b)

#alternative for UNION(U)
a={1,2,3}
b={2,3,4}

union = a | b

#peroforming multiple Union using multiple sets
a={1,2,3}
b={2,3,4}
c ={4,5,6}
multiple_union = a | b | c
print(multiple_union)



#intersection
c = a.intersection(b)
print(c)

#alternative for Intersection
a={1,2,3}
b={2,3,4}

intersection = a & b

#difference
c = a.difference(b)
print(c)

#alternative for difference
a={1,2,3}
b={2,3,4}

difference= a - b


#adding elements to the set
a ={1,2,3}
a.add(4)
print(a)


#updating set (i.e all elements) to another earliler set using update function i.e adding all element of b to a
a= {1,2,3}
b={3,4,2}

a.update(b)
print(a)



'''

#pop item or element
a = {1,2,3}
b = a.pop()
print(a)
print(b)




















