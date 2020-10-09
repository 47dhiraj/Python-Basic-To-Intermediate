
f= open("friends.txt", "r")       # small bracket vitra ko sense("file ko path", "shortcut of command")
xs = f.readlines()     #readlines()  inbuilt function le line line by code read garera list ma rakhxa...i.e here 'xs' vaneko chai list ho
f.close()

xs.sort()         #list ko kura lai sorted gareko using sort() inbuilt function

g = open("sortedfriends.txt", "w")    #naya file banayera tesma write gareko
for v in xs:                  #here v means list
    g.write(v)          #writing each lines
g.close()
