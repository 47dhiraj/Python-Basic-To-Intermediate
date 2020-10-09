#inheritance basic example

#Note: chid ko object, parent ko pani object hunxa
#Note: parent ko object, child ko pani object hunai sakdaina

#Note: child class le parent class ko attribute(property) inherit garna pauxa
#Note: parent class le child class ko attribute(property) inherit garna paudaina


class Animal:        #parent class ho,, having its own speak function
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):  #child class Dog inheriting  the base(parent) class Animal......
    def bark(self):         #bark() chai child class ko function ho
        print("Dog barking")

d = Dog()         #child class Dog ko object banako
d.bark()          #calling child class function with child class ko object
d.speak()           #calling parent class function also with child class ko object

