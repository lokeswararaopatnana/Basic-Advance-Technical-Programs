def is_harshad(n):
    # calculter the sum of digits
    sum = 0
    for digit in str(n):
        sum += int(digit)
    # check if the number is divisible by the sum of its digits
    if n%sum == 0:
        return True
    else:
        return False
# Take input from the user
num = int(input("Enter the value of num:"))
if is_harshad(num):
    print(f"{num} is a harshad number")
else:
    print(f"{num} is not a harshad number")