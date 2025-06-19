class Empolyee: # Base Class
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")


class Programmer(Empolyee, Coder): # Derived or Child Class
    company = "ITC Infotech"
    def showLangauge(self):
        print(f"The name is {self.company} and the he  is  good with {self.language} language")

a = Empolyee()
b = Programmer()

b.show()
b.printLanguage()
#Output:
# The name of the Employee is Default Name and the company is ITC Infotech
# Out of all the language here is your language: Python