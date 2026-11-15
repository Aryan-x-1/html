
class Mobile:
    def __init__(self):
        self.__brand = "Samsung"

    def get_brand(self):
        return self.__brand

    def set_brand(self, new_brand):
        self.__brand = new_brand


phone1 = Mobile()


print("Original brand:", phone1.get_brand())


phone1.set_brand("Apple")


print("Updated brand:", phone1.get_brand())

