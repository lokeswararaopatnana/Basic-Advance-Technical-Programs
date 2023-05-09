""" 1st Method """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number:"))
if num<0:
    print("Sorry! Factorial doen't exist for negative numbers")
elif num == 0:
    print("The factorial of '0'and '1' is always equals to '1'.")
else:
    print("The factorial of",num,"is",factorial(num)) 
    
    
""" 2nd Method """
def factorial(m):
    return 1 if (m == 0 or m == 1) else m*factorial(m-1)
number = int(input("Enter the value of number:"))
print("Factorial of",number,"is",factorial(number))


""" 3rd method """
import math as m
print(m.factorial(3))