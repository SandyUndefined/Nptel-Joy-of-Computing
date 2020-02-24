r, c = map(int,input().split(" "))
matrix=[[0 for i in range(c)]for j in range(r)]
n=1
for i in range(r):
    for j in range(c):
        matrix[i][j]=n
        n+=1
for i in range(r):
    for j in range(c):
        if j !=(c-1):
            print(matrix[i][j], end=" ")
        else:
            print(matrix[i][j], end="")
    if i !=(r-1):
        print()
