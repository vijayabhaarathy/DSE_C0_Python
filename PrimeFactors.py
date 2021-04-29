#5. Given a number n, write a function to print all prime factors of n. For example, if the input number is 12, then output should be “2 2 3”.

import math
def find_primefactors(num):
    prime=[]
    while num%2==0:
        prime.append(2)
        num=num/2
    
    for i in range(3,int(math.sqrt(num)+1)):
        while num%i==0:
            prime.append(i)
            num=num/i
    
    if num>2:
        prime.append(num)
    
    print(prime)

num=int(input("Enter a number: "))
find_primefactors(num)
