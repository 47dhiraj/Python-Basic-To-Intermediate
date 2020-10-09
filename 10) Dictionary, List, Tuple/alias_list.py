#yaha things ra a_list duitai list ho ... auta list ko refrence or memory location arko lai assign gareko... so yesto lai aliasing vaninxa
#both list le same memory location lai refer gareko xa... auta list ma change garda arko pani chane hunxa

def test(a_list):
    for index in range(len(a_list)):
        a_list[index]=a_list[index]*2      #loop vitra ko statement ho yo
    print(a_list)            #loop bahirako but test definition vitra ko statement ho yo

    

things=[2,5,'spam',9.5]
test(things)
print(things)



