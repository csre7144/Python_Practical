class Employee:
    language = "Python" # This is a class attribute
    salary = 12000

    def __init__(self, name,salary, language): # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print(f"Good Morning")

    @staticmethod
    def greetStatic():
        print(f"Good Evening")

p1 = Employee("Chintu", 13000, "JAVA")
# p1.name = "Chintu"
print(p1.name, p1.salary)
# Output:
# I am creating an object
# Chintu 13000
print(p1.name, p1.salary, p1.language)
# Output:
# I am creating an object
# Chintu 13000 JAVA

# Output:
# I am creating an object
# Chintu 12000

# rohan = Employee() # Output: I am creating an object