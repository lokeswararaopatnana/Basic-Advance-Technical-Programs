""" 1st Method """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**(0.5))+1):
        if n%i == 0:
            return False
    return True
num = int(input("Enter the value of num:"))
if is_prime(num):
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))
    
    
""" 2nd Method """
prime = int(input("Enter the value of prime:"))
# if given number is equal to 1
if prime == 1:
    print(f"{prime} is not prime number")
elif prime > 1:
    # Iterate from 2 to prime/2
    for i in range(2,int(prime/2)+1):
        # If prime is divisible by any number between 2 and prime/2, it is not a prime number
        if (prime%i) == 0:
            print(f"{prime} is not a prime number")
            break
    else:
        print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime number")