""" Q: Star Pattern Program to Print Scalene Triangle ? """
# Python star pattern program to print scalene traingle
def pattern(n):
    # number of spaces
    a=n-1
    for i in range(n):
        for j in range(a):
            print(end=" ")
        # incrementing a after each loop
        a=a-1
        for j in range(i+1):
            # print stars
            print("* ",end=" ")
        print("\r")
# take inputs
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)