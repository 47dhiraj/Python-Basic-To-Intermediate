
def make_pretty(func):    #decorator receiving ordinary function
    def inner():
        func()
        print("I got decorated")

    return inner

@make_pretty              #yo @make_pretty le automatically tala lekheko ordinary defination lai decoraotr ma halxa
def ordinary():
    print("I am ordinary")


ordinary()           #khas yo function call garda siddai mathi ko make_pretty() decorator clal hunxa