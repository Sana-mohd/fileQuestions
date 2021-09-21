#Remove all the lines that contain the character `a' in a file and write it to another file.
f=open("a_.txt","r")
g=open("new_a.txt","w")
for line in f:
    if "a" in line:
        line=line.replace("a","")
    else:
        g.write(line)
    
f.close()
g.close()