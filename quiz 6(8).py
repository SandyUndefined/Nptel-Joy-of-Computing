def fun(i):
    print(i)
    if(i>128):
        print("over")
    else:
        fun(2*i)
fun(25)
