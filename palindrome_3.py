#Write a function that takes a string as an argument and return Palindrome if the string is a palindrome 
# herwise return Not A Palindrome. Also write a complete Python program to call this function.

# by using while loop and using negetive index on string
def palindrome(string):
    rev=""
    i=-1
    while i>=-len(string):
        rev=rev+string[i]
        i-=1
    if rev==string:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(palindrome("madam"))

# Alternate method by using slicing on string
def palindrome(string):
    rev=string[::-1]
    if string==rev:
        return "Palindrome"
    else:
        return "Not a Palindrome"
print(palindrome("mad"))


