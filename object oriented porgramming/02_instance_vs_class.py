class Employee:
    language = "Python" # This is a class attribute
    salary = 12000

p1 = Employee()
p1.language = "Java" # This is an instance atteibute
print(p1.language, p1.salary)