class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student object initialized")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        print("Student object finalized")


s1 = Student("Arun", 21)

s1.display()

del s1