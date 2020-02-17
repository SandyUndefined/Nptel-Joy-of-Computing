def aradd(ar):
    rev_ar = ar[::-1]
    result=[]
    for i in range(0,len(ar)):
        result.append(ar[i]+rev_ar[i])
    return result
t=int(input())
ar=list(map(int, input().strip().split()))[:t]
print(*aradd(ar))
