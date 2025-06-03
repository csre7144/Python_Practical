name = "Chintan"

# 1. len()
print(len(name))

# startswith() / endswith()
print(name.endswith("tan"))
print(name.endswith("taan"))
print(name.startswith("Chi")) # Output: True

# 2.capitalize()
print(name.capitalize)

# 3. lower() / upper()
print(name.lower())  # Output: hello
print(name.upper())  # Output: HELLO

# 4.find() / index()
print(name.find("Chintan"))  # Output: 6

# 5.replace()
print(name.replace("world", "Python"))  # Output: hello Python

# 6.count()
print(name.count("a"))  # Output: 1

# 7.strip() / lstrip() / rstrip()
s = "Chintan  "
print(s.strip())   # Output: "hello"

# 8.split() / rsplit()
s1 = "apple,banana,cherry"
print(s1.split(","))  # Output: ['apple', 'banana', 'cherry']


# 9.join()
words = ["Hello", "World"]
print(" ".join(words))  # Output: Hello World

# 10.isalnum() / isalpha() / isdigit()
# isalnum() – letters or numbers
# isalpha() – only letters
# isdigit() – only digits
s2 = "abc123"
print(s2.isalnum())  # Output: True

