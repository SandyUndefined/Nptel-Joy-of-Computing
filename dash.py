import random
c=0
movies =["titanic","chinatown","avengers","3idiots","conjuring","junglebook","matrix"]
ch =random.choice(movies)
print(ch)
for i in range (len(ch)):
    print ('_'),
    c=c+1
print(c)
