#Write a program that reads a text file and count the number of words ending with “ing”.
f=open("ing.txt","r")
a=f.readlines()
count=0
for i in a:
    b=i.split(" ")
    for j in b:
        if len(j)>=3:
            if j[-3::]=="ing":
                print(j)
f.close()
