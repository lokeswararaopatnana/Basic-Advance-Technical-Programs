""" Q: Star Pattern Program to Print Left Pascal Triangle ? """
# Python star pattern program to print left pascal trianlge
def pattern(n):
    # print upper triangle
    for i in range(n):
        for j in range(n-i-1):
            # printing spaces
            print(" ",end=" ")
        for j in range(i+1):
            # print stars
            print("* ",end="")
        print()
    # print lower triangle
    for i in range(n-1):
        for j in range(i+1):
            # printing spaces
            print(" ",end=" ")
        for j in range(n-i-1):
            # print stars
            print("* ",end="")
        print()
# take inputs
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)