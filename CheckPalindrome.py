#3. Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “malayalam” is a palindrome, but “music” is not a palindrome.

def check_Palindrome(str):
    x=len(str)
    temp=True
    if x%2==0:
        temp= False
    
    fwd=0
    end=x-1
    
    while fwd<x:
        if str[fwd]!=str[end]:
            temp= False
        fwd=fwd+1
        end=end-1
    
    return temp

str=input("Enter a string: ")
check_Palindrome(str)
