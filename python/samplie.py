# lets create a class with three properties
class student:
    pass
student1 = student()

student1.name = "John"
student1.age = 20
student1.marks = 85

print("Name:", student1.name)
print("Age:", student1.age)
print("Marks:", student1.marks)

# notice this line student1.name = "John" 
# it assigns a name attribute to the object referenced by student1
# however manuaqlly assigning attributes to every object is inconvenient and error-prone.
#Python provides a better way: the __init__() method.