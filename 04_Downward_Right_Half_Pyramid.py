""" Q: Star Pattern Program to Print Downward Right Half Pyramid ? """
# Python star pattern program to print downward right half pyramid
def pattern(n):
    for i in range(n-1):
        for j in range(i+1):
            # printing spaces
            print(" ",end=" ")
        for k in range(n-i-1):
            # printing satrs
            print("* ",end="")
        print()
# take input
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)