#Write a Python function that takes a list of strings as an argument and displays the strings which 
# starts with “S” or “s”. Also write a program to invoke this function.
def s_S(list):
    for i in list:
        if i[0]=="S" or i[0]=="s":
            print(i)
s_S(["sana","ali","Sara"])
