#IMPLICIT type conversion (yaha hierarchy ko basis ma type promotion  hunxa i.e integer ko vanda float ko hierachy badi hunxa)
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo         #yo line ma num_new varibale ma add hune bela implicit type conversion vayera value add hunxa
print("datatype of num_int:",type(num_int))
print("datatype of num_int:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


#EXPLICIT type conversion

a=2
b=4.0
print("Data type of a", type(a))
print("Data type of b",type(b))

converted_a = float(a)    #yo line ma lekheko float chai python le diyeko function ho so ta convert explicitly
sum = converted_a + b

print("Data type of a after converison", type(converted_a))
print("sum",sum)
print("Data type of sum", type(sum))


