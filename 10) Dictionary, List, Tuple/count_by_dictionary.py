#we use Dictionary for counting variable

letters ="Mississippi"        #letters chai string ho
letter_counts={}        #yo letter_counts chai empty dictionary ho

for index in range(len(letters)):
    letter=letters[index]
    letter_counts[index]=letter_counts.get(letter,0)+1 #khas yo code le key lai value assign garna khojeko ho #comma agadi ko letter chai yaha key ko kaam gareko xa ,,,,yo +1 chai  harek choti 0 sanga add hunxa (i.e comma paxadi ko 0 chai value ho)
print(letter_counts)          #finally printing key value pairs of this letter_counts dictionary