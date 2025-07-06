decimal = 11
binary = ""

while 0 < decimal:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2


# while decimal > 0:
#     binary = str(decimal % 2) + binary
#     decimal = decimal // 2

print(binary)
