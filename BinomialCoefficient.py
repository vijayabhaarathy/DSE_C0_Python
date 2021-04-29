#6. Given two numbers n and r, find the value of nCr (binomial coefficient: nCr = (n!) / (r! * (n-r)!))

def calc(n,r):
    return factorial(n)/(factorial(r) * (n-r))

def factorial(x):
    fact=1
    while x>0:
        fact=fact*x
        x=x-1
    return fact

n=int(input("Enter value of n:"))
r=int(input("Enter value of r:"))
calc(n,r)
