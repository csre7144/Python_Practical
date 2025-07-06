# from collections import defaultdict

# def check_word_combination(wordsArray, target):
#     # Step 1: Count word frequencies
#     wordCount = defaultdict(int)
#     for word in wordsArray:
#         wordCount[word] += 1

#     # Step 2: Check prefix
#     for word in wordsArray:
#         if target.startswith(word):
#             suffix = target[len(word):]
#             if suffix in wordCount:
#                 if suffix != word or wordCount[word] > 1:
#                     return True

#     # Step 3: Check suffix
#     for word in wordsArray:
#         if target.endswith(word):
#             prefix = target[:len(target) - len(word)]
#             if prefix in wordCount:
#                 if prefix != word or wordCount[word] > 1:
#                     return True

#     return False


# wordsArray = ["ans", "key", "cat", "key"]
# target = "ansans"

# print(check_word_combination(wordsArray, target))  # Output: True


# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# # Example usage
# nums = [2, 6, 9, 1, 3]
# target = 9
# result = two_sum(nums, target)
# print("Indices:", result)



# arr = [8, 12, 11, 1, 3, 8]
# target = 9

# found = False
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(f"Pair found: {arr[i]} + {arr[j]} = {target}")
#             found = True

# if not found:
#     print("No pair found")
arr = [8, 12, 11, 1, 3, 8]  # sorted version
target = 9

i = 0
j = len(arr) - 1

found = False
while i < j:
    current_sum = arr[i] + arr[j]
    
    if current_sum == target:
        print(f"Pair found: {arr[i]} + {arr[j]} = {target}")
        found = True
        break
    elif current_sum < target:
        i += 1
    else:
        j -= 1

if not found:
    print("No pair found")
