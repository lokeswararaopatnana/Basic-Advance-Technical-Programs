""" Q: Star Pattern Program to print Left Half Pyramid ? """

# Python star pattern to print left half pyramid
def pattern(n):
    for i in range(1,n+1):
        # print star
        print("*"*i)
# take input
n=int(input("Enter Number of Rows:"))
# function call
pattern(n)