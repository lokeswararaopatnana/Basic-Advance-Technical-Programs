def is_perfect(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return n == sum
num = int(input("Enter a number:"))
if is_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")