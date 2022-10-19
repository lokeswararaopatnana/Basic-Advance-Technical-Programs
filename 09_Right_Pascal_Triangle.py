""" Q: Star Pattern Program to Print Right Pascal Triangle ? """
# Python star pattern program to print right pascal triangle
def pattern(n):
    for i in range(n):
        print("* "*(i+1))
    for i in range(n):
        print("* "*(n-i-1))
# take inputs
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)