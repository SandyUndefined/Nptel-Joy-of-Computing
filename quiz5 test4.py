t=[]
for i in range(10):
    a=int(input("enter"))
    if(len(t)==0):
        print("this is if")
        t.append(a)
    else:
        print("This is else")
        if(a>t[len(t)-1]):
            t.append(a)
print(t)
