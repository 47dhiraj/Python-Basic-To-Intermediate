#auta image lai arko naya image banunxa ra tesma copy garxa pahila ko image

#yaha image.jpg lai copy.jpg ma copy garera rakheko

f = open("image.jpg", "rb")      #rb indicate read binary
g = open("copy.jpg", "wb")           #wb indicate write binary

while True:
    buf = f.read(1024)             #ekchoti ma 1024 bit read garxa orginal image batw and buffer ma rakhxa
    if len(buf) == 0:              #buffer ko length 0 navayesamma while loop chalai rakhni,,,, break le while loop batw bahira aaunxa
        break 
    g.write(buf)                   #g indicates new image (copy.jpg).............yo image ma write garxa ... while loop chalaunjel
f.close()
g.close()

