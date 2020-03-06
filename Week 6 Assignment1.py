t = int(input())
a = [int(i) for i in input().split()]
f = int(input())

b = sorted(a)

x = a[f-1]

print(b.index(x)+1,end="")
