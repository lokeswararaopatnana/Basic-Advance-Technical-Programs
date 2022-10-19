""" Q: Star Pattern Program to Print Right Half Pyramid ? """
# Python star pattern to print right half pyramid
def pattern(n):
    for i in range(1,n+1):
        # print star
        print(" "*(n-i)+"*"*i)  #{here " " space is important}
# take input
n=int(input("Enter Number of rows:"))
# function call
pattern(n)