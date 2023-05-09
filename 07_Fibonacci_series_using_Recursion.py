""" 1st Method """
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i))
    
    
""" 2nd Method """
def fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(9))