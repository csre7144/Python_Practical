class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

test = Employee()
print(test.a) #Output: 1

test = Programmer()
print(test.a , test.b) #Output: 1 2

test = Manager()
print(test.a , test.b , test.c) #Output: 1 2 3