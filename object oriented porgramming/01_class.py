# class Employee:
#     name = "chintan"
#     language = "Py" # This is a class attribute
#     salary = 1500

# st = Employee()
# print(st.name, st.language)

# Output: chintan Py


class Employee:
    name = "chintan" # Specific to each class

st = Employee() # Object Instatiation 
st.name
Employee.name = "Harshiv" # Changing class attribute
print(st.name) 
# Output: Harshiv

st.salary = "40K" # Adding isntance attribute
print(st.name, st.salary)
# Output: Harshiv 40K