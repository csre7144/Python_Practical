# a = (1,3,5,7,9)
a = (1,3,5,7,9, "Harry", False)
print(type(a))

# count
no = a.count(45) #output: 0 
no = a.count(7) #output: 1

# index
no = a.index(9) #output: 4
print(no)

# concatenation
b = (2,4,6)
c = (8,10,12)
concatenated = b+c
print(concatenated) #output: (2, 4, 6, 8, 10, 12)

# Repletition
d = (2,4,6)
repeated = d*3
print(repeated) #output: (2, 4, 6, 2, 4, 6, 2, 4, 6)

# memebership
my_tuple = (2,4,6)
print(2 in my_tuple) #output: True
print(3 in my_tuple) #output: False

# length
my_tuple2 = (2,4,6,8)
print(len(my_tuple2)) #output: 4

# min and max
my_tuple3 = (2,4,6,8)
print(min(my_tuple3)) #output: 2
print(max(my_tuple3)) #output: 8


# slicing 
my_tuple4 = (2,4,6,8,10,12,14)
sliced = my_tuple4[1:4]
print(sliced) #output: (4, 6, 8)


# unpacking
my_tuple5 = (2,4,6,8,10)
a, b, c, d, e = my_tuple5
print(a, b, c, d, e) #output: 2 4 6 8 10