marks = {
    "shubham": 100,
    "chintu": 67,
    "Roshan": 45,
    0: "ajit"
}
print(marks, type(marks)) #output: {'shubham': 100, 'chintu': 67, 'Roshan': 45} <class 'dict'>
print(marks["chintu"]) #output: 67

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"chintu": 65, "Roshan": 40})
print(marks)

print(marks.get("Roshan")) #output: 40
print(marks["Roshan"]) #output: 40

# print(marks["chintu2"]) # return an error


# Set session
e = set() #Don't use s = {} as it will create an empty dictionary
s = {1,3,5,6,7,8,3,3,3}
s1 = {1,3,5,6,7,8,3,3,3, "chintu"}
print(s) #output: {1, 3, 5, 6, 7, 8}
print(s1, type(s)) #output: {1, 3, 5, 6, 7, 8, 'chintu'} <class 'set'>


# Add Dictionary Method
s2 = {1,3,5,6,7,8,3,3,3}
s2.add(565)
print(s2) #output: {1, 3, 5, 6, 7, 8, 565}


# Union Dictionary Method
s3 = {2,5,8,9}
s4 = {3,5,4,1}
print(s3.union(s4)) #output: {1, 2, 3, 4, 5, 8, 9}

#Intersection  
s5 = {1,5,8,9}
s6 = {3,5,9,1} 
print(s5.intersection(s6)) #output: {9, 5, 1}

print(s5-s6) #output: {8}
