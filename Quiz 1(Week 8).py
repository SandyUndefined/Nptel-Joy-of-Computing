import random
def play():
    a=input("Enter a number from 1 to 10")
    r=random.randint(1,10)
    if(a==r):
        return 1
    else:
        return 0

amt = 0
for i in range(1,366):
    amt=amt+play()

print(amt)
