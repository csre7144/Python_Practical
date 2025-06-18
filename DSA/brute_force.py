# a = [1, 3, 5, 7]
# b = [3, 7]

# # Brute force duplicate check
# duplicates = []

# for i in a:
#     for j in b:
#         if i == j:
#             duplicates.append(i)

# if duplicates:
#     print("duplicates - YES")
#     print("Duplicate elements:", duplicates)
# else:
#     print("duplicate - NO")


a = input("Enter elements of list a separated by space: ")
b = input("Enter elements of list b separated by space: ")

# Convert the input strings to lists of integers
a = [int(x) for x in a.split()]
b = [int(x) for x in b.split()]

# Brute force duplicate check
duplicates = []

for i in a:
    for j in b:
        if i == j and i not in duplicates:
            duplicates.append(i)

if duplicates:
    print("duplicates - YES")
    print("Duplicate elements:", duplicates)
else:
    print("duplicate - NO")