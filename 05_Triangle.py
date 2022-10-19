""" Q: Star Pattern Program to Print Pytamid or Triangle ? """
# Python star pattern program to print pyramid or triangle
def pattern(n):
    for i in range(n):
        # print stars
        print(" "*(n-i-1)+"*"*(2*i+1))
# take input
n= int(input("Enter Number of Rows:"))
# function call
pattern(n)