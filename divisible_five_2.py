# Write a function that takes a list of numbers as argument and return the sum of all numbers which are
#  divisible by 5. Also write a complete Python program to call this function.

# passing list as an argument in the function and using for loop
def sum_of_elements(list):
    sum=0
    for i in list:
        sum=sum+i
    return sum
print(sum_of_elements([7,9,8]))


# taking list from user and using while loop. here we are taking list elements from user by passing length of list as an argument from user and returning sum of the elements
def sum_of_elements(user_length):
    user_list=[]
    sum=0
    for i in range(user_length):
        user_element=int(input("enter the number: "))
        user_list.append(user_element)
        sum=sum+user_element
    print("your list is ",user_list)
    return "Sum of the elements of list is "+str(sum)
print(sum_of_elements(int(input("enter the length of list: "))))
