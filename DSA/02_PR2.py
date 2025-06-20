# arr = [[1, 2], [2, 1], [3, 4], [8, 7], [5, 6], [9, 10], [10, 9], [2,2]]
# duplicates = []

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j] or arr[i] == arr[j][::-1]:
#             duplicates.append((arr[i], arr[j]))

# if duplicates:
#     print("Duplicate pairs (including reverse):")
#     for pair in duplicates:
#         print(pair)
# else:
#     print("No duplicate pairs found.")

arr = [[1, 2], [2, 1], [3, 4], [8, 7], [5, 6], [9, 10], [10, 9], [2, 2]]
duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # Exact match or reverse match (only if elements are not equal)
        if arr[i] == arr[j] or (arr[i][0] != arr[i][1] and arr[i] == arr[j][::-1]):
            duplicates.append((arr[i], arr[j]))

if duplicates:
    print("Duplicate pairs (including reverse and self-pairs):")
    for pair in duplicates:
        print(pair)
else:
    print("No duplicate pairs found.")
