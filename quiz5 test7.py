def find(list1,num):
    for each in list1:
        if(each!=num):
            print(each)
        else:
            break
t=[]
for i in range(10):
    t.append(i)
find(t,9)
