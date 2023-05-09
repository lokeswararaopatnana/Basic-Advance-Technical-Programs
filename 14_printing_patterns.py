# Pattern-1==>Right Triangle
n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()
    
# Pattern-2==>Inverted Right Tr5iangle
n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("* ",end="")
    print()
    
# Pattern-3==>Pyramid
n = int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
    
# Pattern-4==>Inverted Pyramid
n = int(input("Enter the number of rows:"))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))