""" 1st Method """
def swap_numbers(a,b):
    a = a+b
    b = a-b
    a = a-b
    return a,b
# Example usage
x = 15
y = 10
print("Before swapping: x =",x,"and y =",y)
x,y = swap_numbers(x,y)
print("After swapping: x =",x,"and y =",y)



""" 2nd Method """
swap1 = int(input("Enter the value of swap1:"))
swap2 = int(input("Enter the value of swap2:"))
# condition apply
swap1,swap2 = swap2,swap1
# printing the swapping nummbers
print("swap1 value is:",swap1)
print("swap2 value is:",swap2)