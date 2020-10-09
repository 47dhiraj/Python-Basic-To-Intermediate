#overloading comparison operator

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y =y

    def __lt__(self,other):
        return self.x < other.x             #yaha batw return hune chai Boolean(true or false) value ho

p = Point(1,2)
q = Point(3,4)

result = p < q  #yo line ma '<' le automatically mathi ko inbuilt __lt__() function lai call gars
                #yo result le chai auta boolean value hold receive garxa
print(result)