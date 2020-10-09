#decorating function wiht parameters

def smart_divide(func):
    def inner(a,b):
        if b == 0:
            print("cannot divide by zero")
            return None

        return func(a,b)           #divide function lai call garera return gareko
    return inner             #sabbai kura decorated vai sake paxi inner le gareko return

@smart_divide         #@smart_divide decorator apply gareko tline 13 ko divide() function lai    
def divide(a,b):
    return a/b

result = divide(6,2)      #yo line execute vaye paxi...line 12 execute hunxa...ani siddai line 3 hunxa
print(result)

