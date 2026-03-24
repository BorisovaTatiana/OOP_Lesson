# Задание_1

import math
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

c = Circle(5)
s = Square(4)

print(c.area())  # ~78.5
print(s.area())  # 16


# Задание_2
# 2. Создай базовый класс BasePage с методом open(url).
# Сделай добавь магический init, в котором указан текст на странице (любой)
# От него унаследуй LoginPage и добавь метод find(text).
# Проверь, что методы из базового класса тоже доступны:
# page = LoginPage()
# page.open("https://example.com/login")
# page.find("Зима")
# Вывод в консоли:
# На странице найден текст: "Зима"
class BasePage:
    def __init__(self):
        self.page_txt = "Любой весенний текст зима"

    def open(self, url):
        print(url)

class LoginPage(BasePage):
    def find(self, text):
        if text in self.page_txt:
            print(text)
        else:
            print("Не найдено")

page = LoginPage()
page.open("https://example.com/login")
page.find("Зима")
# Вывелось:
# https://example.com/login
# Не найдено

# Задание_3

class ResultList(list):
    def success_count(self):
        return sum(1 for item in self if item.get("status") == "passed")

results = ResultList([
    {"status": "passed"},
    {"status": "failed"},
    {"status": "passed"},
])

print(results.success_count())

# Задание_4

class BaseStep:
    pass

class LoginStep(BaseStep):
    pass

step = LoginStep()
print(issubclass(LoginStep, BaseStep))  # True
print(isinstance(step, BaseStep))

# Задание_5

class ExtendedDict(dict):
    def __str__(self):
        dict_beau = [f"{key}: {value}" for key, value in self.items()]
        return "\n".join(dict_beau)

d = ExtendedDict(a=1, b=2)
print(d)


# Задание_6

class Widget:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(Widget):
    def __init__(self, x, y, label):
        super().__init__(x,y)
        self.label = label

btn = Button(100, 200, "OK")
print(btn.x, btn.y, btn.label)

# Задание_7

# Без super конструктор родителя не выполнится,
# поэтому атрибуты x и y не создадутся.

# Задание_8

class Logger:
    def log(self, msg):
        print(msg)

class HTMLLogger(Logger):
    def log(self, msg):
        super().log(msg)
        print(msg)
logger = HTMLLogger()
logger.log("Login successful")