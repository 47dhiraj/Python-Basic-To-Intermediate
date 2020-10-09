'''
#empty tuple
a=()
print(a)

#tuple with single value
a=(2,)              #yesle tuple ho vanera janauncha so comma diyena vani '2' lai integer ho vanera janauncha
print(a)
print(type(a))

#creating a tuple
a=(1,2,3,"nepal",3.4,6,9)
print(a)

#accessing Values
val=a[0]
print(val)

#assigning values
a=(1,2,3,4)    
#a[1]=4      #tuple ma value assign garda error auncha so assign chai garna mildaina tuple a value.
print(a)



#updating tuple 
a=(3,4,5)
b=(9,)+a[1:3]  #yaha chai b lai update gareko
print(b)
'''



#deleting elements from tuples,single deletion is not possible , due to reason that tuple is immutable
#we can delete whole tuple

a=(1,2,3)
del a 

#tuple packing,or assignments
a=(1,2,"nepal")


#tuple unpacking
a=(1,2,"nepal")

#number1 =a[0]
#number2 =a[1]
#country =a[2]

(number1,number2,country) = a        #mathi ko 3 line ma lekheko code ,,, yesari single line ma lekhna milxa
print(number1,number2,country)


#excahnging values of two variables , with tuple

a=2
b=3
(a,b) = (b,a)      #yo line le tuple ko value swap garxa
print(a,b)







