# f = open("d:/Python Roadmap 2025/Python Practical/function_method/second_file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:
with open("d:/Python Roadmap 2025/Python Practical/function_method/second_file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file 

# Output:
# Hey Chintar, You are amazing.
# I am a second line.
# This is amazing.