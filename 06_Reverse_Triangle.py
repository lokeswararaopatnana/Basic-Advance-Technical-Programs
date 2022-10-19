""" Q: Star Pattern Program to Print Reverse Pyramid or Triangle ? """
# Python star pattern program to print reverse pyramid or triangle
def pattern(n):
    # number of spaces
    a=(2*n)-2
    for i in range(n,-1,-1):
        for j in range(a,0,-1):
            print(end=" ")
        # incrementing a after each loop
        a=a+1
        for j in range(0,i+1):
            # print stars
            print("* ",end="")
        print("\r")
# take inputs
n=int(input("Enter Noumber of Rows:"))
# function call
pattern(n)