a = 99

def fun():
    # Global
    a = 3
    print(a)

print(a)
fun()
# Output:
# 99
# 3