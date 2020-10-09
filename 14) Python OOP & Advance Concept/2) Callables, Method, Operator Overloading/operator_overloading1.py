#Overloading of  + operator

class Point:
    def __init__(self, x =0, y =0):    #creating constructor automatically during creating object
        self.x =x
        self.y =y

    def __add__(self, other):  #here, self represent object p  & other represent object q
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)            #khas ma chai yo return line le yo __add__ function batw both object ( p  &  q ) nai return garxa
                                    #object return garne belama return type chai class ko name hunxa... khyal gares
p = Point(1,2)
q = Point(3,4)

result_object = p + q    #yo line ma '+' le automatically python ko special function __add__ lai call garxa
                        #yo line ma result_object pani auta user define object ho i.e mathi __add__ function batw object nai return hunxa so automatically object aayera basxa
print(result_object.x, result_object.y)




