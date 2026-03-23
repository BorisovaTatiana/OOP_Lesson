# Задание_1_2

class SecureData:
    def __init__(self, secret):
        self.__secret = secret

    def __getattribute__(self, name):
        if name == "__secret":
            raise ValueError("Доступ запрещен")
        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "token":
            raise AttributeError("Запрет!")
        object.__setattr__(self, name, value)

    def get_secret(self):
        return self.__secret

data = SecureData("пароль123")
# print(data.__secret)
print(data.get_secret())
# data.token = "abc123"
data.other = "ok"

# Задание_3

class SafeDict:
    def __getattr__(self, name):
        return "N/A"

    def __delattr__(self, name):
        if hasattr(self, name):
            print(f"Удален атрибут {name}")
            object.__delattr__(self, name)
        else:
            print(f"Атрибут {name} не существует")

d = SafeDict()
print(d.unknown)     # "N/A"
d.key = 10
del d.key            # "Удалён атрибут key"

# Задание_4_5

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Error!")
        self.__salary = value

    @salary.deleter
    def salary(self):
        del self.__salary

    @property
    def name(self):
        return self.__name

e = Employee("Daniil", 5000)
print(e.salary)   # 5000
e.salary = 8000
print(e.salary)   # 8000
# e.salary = -100

del e.salary
print(e.__dict__)  # salary нет

# Задание_6

class LoginForm:
    def __init__(self):
        self.username = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

form = LoginForm()
form.username = "admin"  # выводит лог
print(form.username)

# Задание_7

import time
from datetime import datetime
class Card:
    def __init__(self, number = None):
        self.__number = number

    @property
    def number(self):
        if self.__number is None:
            return None
        return self.__number[-4:]

    @number.setter
    def number(self, value):
        if not isinstance(value, str) or len(value) != 16 or not value.isdigit():
            raise ValueError("Error!")
        self.__number = value

    @number.deleter
    def number(self):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        del self.__number

card = Card()
card.number = "1234567890987654"
print(card.number)
del card.number


# Задание_8

import json

class UserData:
    def __init__(self, email, age, is_active=True):
        self.email = email
        self.age = age
        self.is_active = is_active

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Email должен содержать '@'!")
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 18:
            raise ValueError("Возраст должен быть ≥ 18!")
        self._age = value

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_active должен быть bool!")
        self._is_active = value

    @property
    def json(self):
        return {
            "email": self.email,
            "age": self.age,
            "is_active": self.is_active
        }
try:
    user = UserData("test@test.com", 15)
except ValueError:
    print("age < 18")

try:
    user = UserData("invalid", 18)
except ValueError:
    print("email без @")

user1 = UserData("test@test.com", 36, True)
expected = {"email": "test@test.com", "age": 36, "is_active": True}
print(user1.json)