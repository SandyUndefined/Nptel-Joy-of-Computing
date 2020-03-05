import random
def guess(num):
    a=int(input("number"))
    print(a,num)
    if(a==num):
        print("s")
    else:
        guess(random.randint(1,100))
i=guess(random.randint(1,100))
