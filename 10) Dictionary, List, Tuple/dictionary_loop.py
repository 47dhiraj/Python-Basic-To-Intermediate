#iteration of dictionary

#".items" vanni inbuilt function ho jasle items haru ko key ra value lincha

details={'name': 'Ram','age':24}   #details vanni yeuta dictonary ho. Yesma Key and value huncha "curly bracket" leh vancha yo dictionary ho.
print(details.items())          #dictonary ma key ra values pair pair banayera xutaideko huncha

for key,val in details.items():     #loop lagayera  details ko key ra details ko value haldai gako 
    print(key,val)                   #haleko key,value  print gareko

