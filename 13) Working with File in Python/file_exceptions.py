
print('Doing task one')

try:
    f = open("testy.txt", 'r')
    print(f.read())

except IOError as e:
    print("IO Error")
    print(e)

print('Doing next task')