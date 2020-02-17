with open("fi.txt","w") as f:
    f.write("hey! I m writing");
    f.close()
with open("fi.txt","w")as f:
    f.write("hey i m writing the second line");
    f.close()
    with open("fi.txt","r") as f:
        print(f.read())
        f.close()
