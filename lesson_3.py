# Задание_1_2_3
import math

class Circle:
    MIN_RADIUS = 1
    MAX_RADIUS = 1000

    @classmethod
    def is_valid_radius(cls, r):
        return cls.MIN_RADIUS <= r <= cls.MAX_RADIUS

    @staticmethod
    def area(radius):
        return math.pi * radius**2

    def __init__(self, radius):
        if self.is_valid_radius(radius):
            self.radius = radius
        else:
            raise ValueError("Error: radius is not in diapasone")

    def print_info(self):
        print(self.radius)
        print(f"Допустимый диапазон: [{type(self).MIN_RADIUS}, {type(self).MAX_RADIUS}]")


print(Circle.is_valid_radius(500))
print(Circle.is_valid_radius(1500))

c = Circle(10)
print(c.area(c.radius))

c.print_info()

# Задание_4_5_6

class User:
    def __init__(self):
        self.__login = None
        self.__password = None

    def __encrypt_password(self, password):
        return password.upper()

    def set_credentials(self, login, password):
        if isinstance(login, str) and isinstance(password, str):
            self.__login = login
            self.__password = self.__encrypt_password(password)
            print("Данные сохранены")
        else:
            print("Проверить условие ввода данных")

    def get_credentials(self):
        return(self.__login, self.__password)

    def check_password(self, password):
        return self.__password == self.__encrypt_password(password)

user1 = User()
user1.set_credentials("Tatiana", "qwerty")
print(f"Данные пользователя: {user1.get_credentials()}")
#
# user1.__login = "Tata"
# print(u.get_credentials())

user2 = User()
user2.set_credentials("Sergey", "qwerty")
print(user2.check_password("qwerty"))
print(user2.check_password("qwe"))
print(user2.check_password("QWERTY"))

try:
    user2.__encrypt_password("test")
except AttributeError as e:
    print(e)

try:
    print(user2.__password)
except AttributeError as e:
    print(e)

try:
    print(user2.User__password)
except AttributeError as e:
    print(e)

# Потому что приватные методы не вызываются извне.
# С ними напрямую можно работать исключительно внутри класса
