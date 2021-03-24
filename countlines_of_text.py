f=open("people1.txt","r")
count=0
for i in f:
    if i!="\n":
        count=count+1
f.close()
print(count)



