'''
#first approach of finding key from value
a={"name":"test","age":34}
for key, val in a.items():  #".items" vanni inbuilt function ho jasle items haru ko key ra value lincha
    if val==34:
        print(key)

'''

#second approach of finding key

a={"name":"test","age":34}

#auta naya dictionary (inverse_dict) banako jun chai auta inverse dictionary ho
inverse_dict=dict((value,key) for key,value in a.items())  #loop lagayera inverse_dict ko key ra value ma  a  ko key ra  a  ko value haldai gako 

print(inverse_dict)
print(inverse_dict[34])
