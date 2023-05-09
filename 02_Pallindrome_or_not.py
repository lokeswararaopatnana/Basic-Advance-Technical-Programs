""" 1st method """
def is_pallindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
# Example usage
print(is_pallindrome(121))
print(is_pallindrome(143))


""" 2nd Method """
char = input("Enter the character to check pallindrome or not:")
# condtion apply
if char == char[::-1]:
    print("{} is a Pallindrome".format(char))
else:
    print("{} is not a Pallindrome".format(char))