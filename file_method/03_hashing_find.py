# arr = ["house", "red", "chilli", "land", "green"]

# def funct(arr, target):
#     combinations = set()
#     n = len(arr)

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue
#             first = arr[i] + arr[j]
#             combinations.add(first)

#     return target in combinations

# target = "greenhouse"
# print(funct(arr, target))
# Output: True

# arr = ["after", "back", "moon", "child"]

# def funct(arr, target):
#     combinations = set()
#     n = len(arr)

#     for i in range(n):
#         for j in range(n):
#             if i == j:
#                 continue
#             first = arr[i] + arr[j]
#             combinations.add(first)

#     return target in combinations

# target = "aftermoon"
# print(funct(arr, target))
# Output: False


# for (int i=0, i<n, i++){
#     for (int j=0, j<n, j++){
#         if (i != j){
#             if (wordarr[i]+wordarr[j]).equal(target){
#                 return True;
#             }
#         }
#     }
# }

# words = ["ab", "cd"]
# target = "abcd"

# def check_combination(wordarr, target):
#     n = len(wordarr)
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 if wordarr[i] + wordarr[j] == target:
#                     return True
#     return False

# result = check_combination(words, target)
# print(result)  # Output: True
    

# map<string,Interger> wordcount = newhashmap():
#     for (stringwrod. wordarry){
#         worldcount. put (word, wordcount.getDeafult(wrod,0)+1);
#     }


word_array = ["example", "word", "example", "test"]
word_count = {}

for word in word_array:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
