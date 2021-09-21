# we are importing random to generate random number in given range and random is a module .
import random
# function named random_number is created and n is a parameter.
def random_number(n):
    # we are iterating in the range of n to generate random number in given times of n .
    for i in range(n):
        #here in randint start=1 and end=6 because a dice have six faces with numbers 1,2,3,4,5,6.
        a=random.randint(1,6)
        print(a)
# taking user input to know from the user that how many times a dice is rolled.
# n=int(input("enter the number of times dice should be rolled: "))
#calling the function with argument.
random_number(int(input("enter the number of times dice should be rolled: ")))