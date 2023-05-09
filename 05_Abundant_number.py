def is_abundant(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    return sum>n
num = int(input("Enter the value of num:"))
if is_abundant(num):
    print(f"{num} is abundant number")
else:
    print(f"{num} is not a abundant number")