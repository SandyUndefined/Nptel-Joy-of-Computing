def fun(i,f):
    print(i)
    if(i==0):
        f=1
        fun(i+1,f)
    if(i==128):
        f=-1
        fun(i-1,f)
    if(f==1):
        fun(i+1,f)
    if(f==-1):
        fun(i-1,f)
fun(128,25)
