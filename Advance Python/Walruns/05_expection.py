# Practice 01
# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)


# except Exception as e:
#     print(e)


# Practice 02
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyy")
    print(v)

except Exception as e:
    print(e)