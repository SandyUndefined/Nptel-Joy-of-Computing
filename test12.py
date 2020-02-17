with open("f.text","w") as myfile:
    myfile.write("0110");
    myfile.close()
with open("f.txt","r") as myfile:
    l=list(myfile.read());
    sum1=0
    for each in l:
        sum1=sum1+int(each)
    print(sum1)
    myfile.close()
