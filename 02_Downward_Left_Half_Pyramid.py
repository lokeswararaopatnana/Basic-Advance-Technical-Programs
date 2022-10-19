""" Q: Star Pattern Program to Print Downward Left Half Pyramid ? """

# Python star pattern program to print downward left half pyramid
def pattern(n):
    for i in range(n):
        # print star
        print("*"*(n-i))
# Take input
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)