l = list(map(int,input().split()))
ar=[]
for i in l:
    if(i%5!=0):
        ar.append(i)
print(*ar)
