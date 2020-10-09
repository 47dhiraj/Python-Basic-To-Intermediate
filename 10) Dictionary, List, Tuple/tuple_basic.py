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
