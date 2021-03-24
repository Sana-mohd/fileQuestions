f=open("question3.txt","r")
a=f.readlines()
for x in a:

    if "delhi" in x:
        
        d=open("delhi.txt","a")
        # l.append(x)
        d.write(x)
        print(x)
    elif "shimla" in x:
        s=open("shimla.txt","a")
        s.write(x)
    else:
        o=open("others.txt","a")
        o.write(x)
f.close()

