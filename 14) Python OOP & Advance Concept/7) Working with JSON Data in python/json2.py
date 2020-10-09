import json

x={                   #x chai dictiionary ho
    'name': 'test','age':23
    
}

y =json.dumps(x)    #x chai dictionary type ho jaslai hamile dumps use garera string ma convert gareko

print(y)
print(type(x))
print(type(y))
