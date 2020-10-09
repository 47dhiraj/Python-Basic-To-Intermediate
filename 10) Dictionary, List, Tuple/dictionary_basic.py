#creating an empty dictionary
details={}

#dictionary with pairs
details ={"address":"ktm","birthyear":1992}


#adding values to it
details["name"]="Ram"
details["birthyear"]=1990

print(details)
print(type(details))

#accessing specific value
val=details["name"]
print(val)

#getting all keys and values
print(details)
print(details.values())


#deleting a pair
del details["name"]
print(details)

#deleting the all items
details.clear()
print(details)

#len returns returns the number of pairs
details["name"]="RAM"
print(len(details))