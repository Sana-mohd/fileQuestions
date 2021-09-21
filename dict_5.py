#Write Python script to create a dictionary with players name and their score. Write a function that 
# accepts this dictionary as an argument and displays the name of the player with highest score.
#here dictionary is created .
dic={}
length_dic=int(input("enter your length of dict: "))
for i in range(length_dic):
    key_=input("enter the player name: ")
    value_=int(input("enter the score of the player: "))
    dic[key_]=value_
print(dic)
# here we are going to make a function which accepts dic as an argument and returns highest score
def max_score(dic):
    max=0
    for j in dic.values():
        if j>=max:
            max=j
    return max
print(max_score(dic))