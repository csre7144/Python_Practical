class Empolyee: # Base Class
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLangauge(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Empolyee): # Derived or Child Class
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a = Empolyee()
b = Programmer()
print(a.company, b.company) #Output: ITC ITC Infotech