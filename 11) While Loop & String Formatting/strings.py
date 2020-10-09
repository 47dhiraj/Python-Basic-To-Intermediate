'''
#Use of IN operator
#Note -> char holds single character each time
vowels = 'aeiou'

text ='nepal'

for char in text:      #logic -> diyeko stirng batw vowels nikalne
    if char in vowels:        #checking whether the text character is vowel character or not
        print(char)

'''

'''
a = 'nepal'

for index in range(len(a)):
    char = a[index]
    print(char,'\n')

'''

'''

#Sting Slicing

a = "nepal"

print(a[2:4])  # : agadi ko chai inclusive ho &  : paxadi ko number exclusive ho i.e 1 less 

print(a[:3])

print(a[2:])

print(a[:])       #no boundary 

'''
'''
country = "nepal"
if country == "nepal":          # == le country & nepal ko value lai comparison garxa i.e not the memory
    print("you are nepali")

#comparing lexicographically(comparing with dictionary)
country = "india"
 
if country < "nepal":  #lexicographically herda indiak ko 'i' chai nepal ko 'n' vanda pahila aauxa
    print("Inside if")

else:
    print("Inside else")
'''
'''
#stings are immutable
country = "nepal"
country[0] = "k"

print(country)
'''
'''
#logic to make string mutable
country = "nepal"
new_country = "k " + country[0:]

print(new_country)

print(country)
'''






















