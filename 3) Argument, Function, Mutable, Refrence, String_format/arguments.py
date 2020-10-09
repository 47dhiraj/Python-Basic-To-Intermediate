#serially -> Require or Positionallly or sequentially argument pass hune


#defining the function
def func(name):
    print("Hi",name)

#calling the function
func("Dhiraj")


#keyword Arguments
def showName(name,age):
    print(name)
    print(age)

showName(age=20, name="Dhiraj Kafle")   #argument pass garda serially nagare pani hune but particular value lai particular variable ma assign garera pass garne milne ..yesto lai keyword arguments vaninxa 

#Default arguments
def showName(name,age=23):
    print(name)
    print(age)

showName("Dhiraj Kafle")

#Overridden Default arguments
def showName(name,age=23):
    print(name)
    print(age)

showName("Dhiraj Kafle",age=24)

#Variables Length arguments
def showName(*names):           #yaha,  *names auta tuple ho jasle jati ota pani argument accept garna sakxa having dynamic behaviour i.e *names varibale chai haina mind it
    print(names)

showName("Dhiraj","Hari","Avisek","Vibhu")


#variable length keyword arguments
def test(**kwargs):  #yaha, **kwargs ko type chai dictionary ho....khyal gar double astrik xa
    print(type(kwargs))
    print(kwargs)
    print(kwargs["name"])

test(name = "Dhiraj" , age=23)  #yaha, jati ota pani keyword pass garna milxa..i.e working as dynamic



#sequential 
#1.Positionallly
#2.variable Legth
#3.keyword
#4.


#following all types of sequence parameters
def test(a,b,*e,d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(e)
    print(kwargs)

test(1,2,4,5,6, d = 3,name="test",age=23)  #arguments haru sequentially mathi parameters ma pass hunxa

#Unfollowing all types of sequence parameters always occur error
def test(**kwargs,a,b,*e,d):
    print(kwargs)
    print(a)
    print(b)
    print(d)
    print(e)
   

test(name="test",1,2,4,5,6, d = 3) 
#yo mathi ko code le error generate garxa









