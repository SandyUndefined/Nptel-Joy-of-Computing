def guess(num):
    a=input("number")
    if(a==num):
        print("s")
    else:
        guess(num)

guess(10)
