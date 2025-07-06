# a = int(input("Enter a number: "))
# b = int(input("Enter second number: "))

# print(f"The Division a/b is {a/b}") # Output: The Division a/b is 0.875



a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

# if (b == 0):
#     raise ZeroDivisionError ("Hey Our Program is not meant to divide numbers by zero")
# else:
#     print(f"The Division a/b is {a/b}") # Output: Hey Our Program is not meant to divide numbers by zero

# ZeroDivisionError OR TypeError

if (b == 0):
    raise TypeError ("Hey Our Program is not meant to divide numbers by zero")
else:
    print(f"The Division a/b is {a/b}") # Output: Hey Our Program is not meant to divide numbers by zero

