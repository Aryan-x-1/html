class Employee:
    def __init__(self):
        self.department = "IT"
        self.__employee_id = "EMP202"


employee1 = Employee()

print("Department:", employee1.department)

try:
    print(employee1.__employee_id)
except AttributeError:
    print("Direct access failed!")

print("Employee ID:", employee1._Employee__employee_id)