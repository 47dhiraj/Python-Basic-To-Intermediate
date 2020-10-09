#json to dictionary

import json

with open('test.json') as f:       #test.json file lai pahila open gareko
    y = json.load(f)        #json file ma vayeko data lai load ko help batw dictionary type ma load gareko

print(y)
print(type(y))
print(y["name"])      #dictionary ko key batw value access garna khojeko
