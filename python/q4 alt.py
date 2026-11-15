
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.b == 0:
            return "Cannot divide by zero"
        return self.a / self.b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

calc = Calculator(a, b)

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Addition:", calc.addition())

elif choice == 2:
    print("Subtraction:", calc.subtraction())

elif choice == 3:
    print("Multiplication:", calc.multiplication())

elif choice == 4:
    print("Division:", calc.division())

else:
    print("Invalid choice")

