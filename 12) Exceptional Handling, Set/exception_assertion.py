#assertion vaneko true or right or thik xa ki nai vanera herxa
#Developer level testing ko lagi use hunxa
'''
a=12
assert a==13    #a ko value 13 aauxa vanera expect garejastai ho...so 13 xa ki nai vanera check garxa....xaina vane exception aauxa
print("done")
'''

'''
#raising an exception if assertion is false

a=13
assert a==12, "value is not equal to 12"
print("done")
'''

#previous example of age validation wihtout raise keyword
def validate_age(age):
    assert age>= 18,"Age must be greater than 17 to vote"
    print("your age is valid")

validate_age(17)