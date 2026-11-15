class Mobile:
    def __init__(self):
        self.brand = "Samsung"
        self.__imei_number = "IMEI123456"


phone1 = Mobile()

print(phone1.brand)

print(phone1.__imei_number)