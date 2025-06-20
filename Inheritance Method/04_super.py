class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c = 3

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# test = Employee()
# print(test.a) 
#Output: 
# Constructor of Employee
# 1

# test = Programmer()
# print(test.a , test.b) 
#Output:
# Constructor of Programmer
# 1 2

test = Manager()
print(test.a , test.b , test.c) 
#Output:
# Constructor of Manager
# 1 2 3

# Output 2
# Constructor of Programmer
# Constructor of Manager
# 1 2 3