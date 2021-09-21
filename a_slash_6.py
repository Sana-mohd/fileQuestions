# Read a text file line by line and display each word separated by a #.
f=open("s_#.txt","r")
a=f.readlines()
for i in a:
    b=i.split()
    for j in b:
        print(j+"#",end="")
    print("")
f.close()

