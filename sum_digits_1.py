# Write a program to calculate sum of the digits of a number using functions.
# using foor loop 
def sum_of_number(number):
    sum=0
    for i in str(number):
        sum+=int(i)
    print(sum)
sum_of_number(input("enter your number: "))

# using while loop
def sum_of_number(number):
    sum=0
    i=0
    while i<len(number):
        sum=sum+int(number[i])
        i+=1
    print(sum)
sum_of_number(input("enter your number: "))

 

