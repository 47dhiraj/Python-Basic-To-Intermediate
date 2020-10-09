#arithmmetic operatiors
 

 #Exponent
a= 2**4
print(a)

#Floor division
b =5//2
print(b)

#assignmetn operator
a=10
a+= 2 
print(a)


#Membership Operator

a=3 in [1,2,3]
print(a)
 
a=4 not in [1,2,3]
print(a)

#identity operators ::: integer data type ma use garda kunnai variable ko same value xa vani tyo duitai variable le same memory lai refer gardo raixa vanni buj vai

a=100
print(id(a))

b=100
print(id(b))

result = a is b   #memory location compare gareko
print(result)


# but list ko case  ma chai same memory refer gardaina
a=[1,2]
b=[4,5]
print(id(a))
print(id(b))

result = a is b   #memory location compare gareko
print(result)





















