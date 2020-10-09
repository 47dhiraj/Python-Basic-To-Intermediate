#json basic
#json file ma data dictionary type ma rakhinxa


import json

x = '{"name":"test", "age":23}' #yaha x chai khas string ho .. json string

y =json.loads(x)        #x ko json string lai loads garni vaneko ... y ma dictionary type ma load gareko

print(y)
print(type(x))
print(type(y))
