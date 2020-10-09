import json
x={
    'name':'test', 'age':23

}

with open('test2.json', 'w') as f:      #test2.json vanni file ma write garna lageko mathiko string
    json.dump(x, f)          #string write garne bela dump lekhinxa
