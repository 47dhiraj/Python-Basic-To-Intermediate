#tuple lai pahile list ma laane fot to change tuple ani finally back to tuple mai laijane from the list

a=(1,2,3,4)  #yo tuple ho
b= list(a)   #tuple lai explicitly list ma lageko
b[2] = 9   # list ma halka modification gareko
c= tuple(b)  #feri list lai explicitly tuple ma lageko

print(b)
print(type(a))
print(type(b))
print(c)



