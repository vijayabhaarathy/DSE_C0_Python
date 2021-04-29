#1. Given a number, find the sum of its digits. Take the number as an input from the user.

n = int(input("Enter a number: "))

sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=(n-rem)/10
    
print(sum)
