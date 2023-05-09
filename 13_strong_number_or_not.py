# function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# function to check if a number is strong or not
def is_strong_number(num):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10

    return sum == num

# taking input from user
num = int(input("Enter a number: "))

# checking if the number is strong or not
if is_strong_number(num):
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")
