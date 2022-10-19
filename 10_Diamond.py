""" Q: Star Pattern Program to Print Diamond ? """
# Python star pattern program to print diamond
def pattern(n):
    # print upper pyramid
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
        # print stars
            print("*",end="")
        print()
    # print downward pyramid
    for i in range(n-1):
        for j in range(i+1):
            print(" ",end="")
        for j in range(2*(n-i-1)-1):
            print("*",end="")
        print()
# take inputs
n=int( input("Enter Number of Rows:"))
# function call
pattern(n)