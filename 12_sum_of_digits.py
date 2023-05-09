num = int(input("Enter a number:"))
sum_of_digits = 0
while num>0:
    sum_of_digits += num % 10
    num //= 10
print("The sum of the digits in the number is:{}".format(sum_of_digits))