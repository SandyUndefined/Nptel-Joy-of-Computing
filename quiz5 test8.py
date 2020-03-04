import random
while(1):
    r=random.randint(1,6)
    if(r%2==0):
        print('This is if')
        print('rollling')
        break
    else:
        print('this is else')
        print('rolling')
