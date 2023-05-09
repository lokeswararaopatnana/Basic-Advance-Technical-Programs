num = int(input("Enter a number:"))
square = num ** 2
if str(square).endswith(str(num)):
    print("{} is an Automorphic number".format(num))
else:
    print("{} is not an Automorphic number".format(num))    