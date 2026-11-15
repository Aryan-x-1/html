
class Employee:
    def __init__(self):
        self.__employee_id = "EMP101"

    def get_employee_id(self):
        return self.__employee_id


employee1 = Employee()

print(employee1.get_employee_id())

