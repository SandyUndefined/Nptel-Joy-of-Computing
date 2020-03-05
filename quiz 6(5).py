import random
def search(l,loc,item):
    if(loc<0):
        loc=0
    if(l[loc]==item):
        print("Found",item,"at",loc)
        return
    if(loc==len(l)-1):
        print("elements")
        return(0)
    else:
        return(search(l,loc+1,item))
l=[1,2,3,4,5,6,7,8,9]
search(1,4,3)
