def fun(i):
    print(i)
    if(i==0):
        print("over")
    else:
        fun(i/2)
fun(5)
