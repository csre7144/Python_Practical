# f = open("d:/Python Roadmap 2025/Python Practical/function_method/second_file.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()

# Output: ['Hey Chintar, You are amazing.'] <class 'list'>


# f = open("d:/Python Roadmap 2025/Python Practical/function_method/second_file.txt")

# lines1 = f.readline()
# print(lines1, type(lines1))

# lines2 = f.readline()
# print(lines2, type(lines2))

# lines3 = f.readline()
# print(lines3, type(lines3))

# lines5 = f.readline()
# print(lines5 =="")

# f.close()

# Output:
# Hey Chintar, You are amazing.
#  <class 'str'>
# I am a second line.
#  <class 'str'>
# This is amazing. <class 'str'>
# True


f = open("d:/Python Roadmap 2025/Python Practical/function_method/second_file.txt")

line = f.readline()
while(line != "" ):
    print(line)
    line = f.readline()

f.close()

# Output:
# Hey Chintar, You are amazing.

# I am a second line.

# This is amazing.