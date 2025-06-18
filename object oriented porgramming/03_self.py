class Employee:
    language = "Python" # This is a class attribute
    salary = 12000

    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print(f"Good Morning")

    @staticmethod
    def greetStatic():
        print(f"Good Evening")

p1 = Employee()
# p1.language = "Java" # This is an instance atteibute

p1.getInfo()
p1.greet()
p1.greetStatic()
# Employee.getInfo(p1)