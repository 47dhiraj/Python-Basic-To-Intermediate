#Note: range()  function le diyeko num vanda less than 1 numbers haru generate garxa or range generate ggarxa

'''
#First way -> by default range starting from 0
for i in range(10):
    print(i)


#second way -> starting value user le diyeko i.e 2 and final range upto 9 (i.e 10)
for i in range(2, 10):
    print(i)

#third way
for i in range(2,10,3):   #here, 2 is starting vale, 10 is final value , and 3 is range to increment
        print(i)

'''

'''
fruits =['orange','banana','apple']

#index ko value by default 0 batw start hunxa
for index in range(len(fruits)): #fruits list ko length calculate garera tei length ko range samma for loop chalako
    print(fruits[index])
    
fruits =['orange','banana','apple']


#index ko value by default 0 batw start hunxa
for index in range(len(fruits)): #fruits list ko length calculate garera tei length ko range samma for loop chalako
    print(fruits[index])

else:       #for loop ma else pani use garna sakinxa
    print("Over and out")

    '''

'''
#Using Break statement -> to come out of loop
fruits=['orange','mango','apple']

for fruit in fruits:
    print(fruit)
    if fruit=='mango':
        print("fruit is mango.so,breaking for loop")
        break  #yo break statement le loop batw nai bahira nikalxa



#Using Break statement -> 
fruits=['orange','mango','apple']

for fruit in fruits:
    if fruit=='mango':
            continue   #yo continue le loop ko tyo particular iteration step lai matra ignore garxu aru iterative step lai as usual run garxa
    print(fruit)

    '''

'''
        
#Finding Duplilcate using nested for loop
numbers=[1,3,9,3,7,1,5,9]

for i in range(len(numbers)):
        for j in range(len(numbers)):
                if i!=j and i<j and numbers[i] == numbers[j]:
                        print(numbers[i])
                        
'''


                        




















