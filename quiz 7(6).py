import random
def play(psn):
    snake_begin=-1
    snake_end=-1
    while(snake_begin <= snake_end):
        snake_begin=random.randint(1,99)
        snake_end=random.randint(1,99)
    print("Snake From",snake_begin,"To",snake_end)
    r=random.randint(1,6)
    print("Dice rolled:",r)
    if(psn==0):
        if(r==1 or r==6):
            psn=1
    else:
        psn=psn+r
    print("Position = ",psn)
    input()
    if(psn==snake_begin):
        print("Bitten by snake")
        psn=snake_end
    if(psn>=100):
        print("Won")
        return
    play(psn)
position=0
print("Position=",position)
play(position)
