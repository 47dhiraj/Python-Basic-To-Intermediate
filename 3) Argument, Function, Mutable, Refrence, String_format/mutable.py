#mutable ->change garna milne i.e auta mutable data structure lai change garda paxi teslai lai effect parne khalko
           #suppose same list,same set,same dictionary vaye pani tyo duita list ko memory location same hunxa....effect parna janxa

#defining the list
list1 =[10,30,40,50]

#defining the function
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function =",list1)

#calling the function
change_list(list1)
print("list outside function = ",list1)






#immutable ->  change garna namillne i.e effect naparne
               # memory location of string different hunxa , tuple pani different hunxa

string1 ="Hi I am there"

#defining the function
def change_string(str):
    str = str + "How is u"
    print("Printing the string inside fucntion:",str)

#calling the functionn
change_string(string1)

print("Printing the string outside function:",string1)
 

