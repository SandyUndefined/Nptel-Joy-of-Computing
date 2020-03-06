def printDict():
  x=int(input())
  d={}
  for i in range(x):
    d[i+1]=(i+1)**2
  print(d,end='') 
printDict()
