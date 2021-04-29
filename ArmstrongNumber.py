#2. Given a number, check whether the given number is an Armstrong number or not. A positive integer is called an Armstrong number of order n if: abcd... = a^n + b^n + c^n + d^n + ... Example: 153 = 1x1x1 + 5x5x5 + 3x3x3 153 is an Armstrong number of order 3. Inputs from the user will be number and order n.

def num_split(num):
    sum=0
    x=0
    num1 = []
    while num>0:
        rem=num%10
        num1.append(rem)
        x=x+1
        num=(num-rem)/10
    return num1

def check_arms(num,order):
    num1=num_split(num)
    sum=0
    for item in num1:
        temp=item**order
        sum=sum+temp
        
    if sum==num:
        return (f"{num} is an Armstrong number")
    else:
        return (f"{num} is not an Armstrong number")

num = int(input("Enter the  number: "))
order = int(input("Enter the order: "))
check_arms(num,order)
