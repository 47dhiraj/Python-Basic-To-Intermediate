#creating empty dictionary
details ={}
#dictioanry with paris
details ={"address":"ktm","birthyear":1992}


#adding valute to it
details["name"] = "Ram"
details["birthyear"]= 1990

print(details)
print(type(details))

#accessing specific value
val = details["name"]
print(val)

#geting all keys and values
print(details.keys())
print(details.values())

#deleting a pair
del details["name"]
print(details)

