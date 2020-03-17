def func(mx,i):
    tur = turtle.Turtle()
    tur.setpos(i,i)
    for ind in range(i,n-i):
        tur.goto(i,ind)
    for ind in range(i+1,n-i):
        tur.goto(i,n-1-i)
    for ind in range(n-2-i,i,-1):
        tur.goto(n-1-i,ind)
    for ind in range(n-i-1,i,-1):
        tur.goto(ind,i)

def func1(mx):
    n=len(mx)
    i=0
    while(i<=n-1):
        func(mx,i)
        i=i+10

print(func1(1400))
