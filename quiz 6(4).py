def mul(num):
    if(num==1):
        return(-1)
    return(-1*mul(num-1))
n=int(input("no"))
print(mul(n))
