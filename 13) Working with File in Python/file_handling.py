'''
#write garna ko lagi ....khas ma write command le overwrite garxa i.e  ek choti file close vayesi arko choti lekhda overwrite garxa

myfile=open("text.txt","w")
myfile.write("hello \n")
myfile.write(".................... \n")
myfile.write("Hello, world! \n")
myfile.close()
'''

'''
#read garna ko lagi
f= open("text.txt", "r")
content = f.read()
f.close()
print(content)
'''
'''
#reading line by line

handle = open("text.txt", "r")
while True:
    line= handle.readline()
    if len(line) ==0:
        break
    print(line)

handle.close()

'''

