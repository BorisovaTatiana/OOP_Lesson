# Задание_1

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Gav"

class Duck:
    def speak(self):
        return "QUak"

animals = [Cat(), Dog(), Duck(), Cat()]

for animal in animals:
    print(animal.speak())

# Задание_2

class Shape:
    pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_pr(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_pr(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_pr(self):
        return self.side1 + self.side2 + self.side3

perimeters = [Square(7), Rectangle(4,5), Triangle(3,5, 7)]
for perimeter in perimeters:
    print(perimeter.get_pr())

# Задание_3

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_pr(self):
        pass

# shape = Shape()
# print(shape.get_pr()) - TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'get_pr'

# Задание_4
# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.

class A:
    def __init__(self):
        print("init A")
        super().__init__()

class B:
    def __init__(self):
        print("init B")
        super().__init__()

class C:
    def __init__(self):
        print("init C")
        super().__init__()

class D(A, B, C):
    def __init__(self):
        print("init D")
        super().__init__()

d = D()
print(D.__mro__)  # D-> A -> B -> C

# Задание_5_6

import datetime

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.price}, {self.weight}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f"{self.id} продан в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def print_info(self):
        print(self.id)

class HotelBooking:
    def __init__(self, guest_name, nights):
        self.guest_name = guest_name
        self.nights = nights

    def confirm(self):
        return f"Бронь для {self.guest_name} на {self.nights} ночей"

class Booking(HotelBooking, MixinLog):
    def __init__(self, guest_name, nights):
        HotelBooking.__init__(self, guest_name, nights)
        MixinLog.__init__(self)

    def confirm(self):
        self.save_sell_log()
        result = super().confirm()
        return result

class NoteBook1(Goods, MixinLog):
    def __init__(self, name, weight, price):
        print("init NoteBook1")
        Goods.__init__(self, name, weight, price)
        MixinLog.__init__(self)

class NoteBook2(Goods, MixinLog):
    def __init__(self, name, weight, price):
        print("init NoteBook2")
        Goods.__init__(self, name, weight, price)
        MixinLog.__init__(self)

book1 = Booking("Anna", 3)
print(book1.confirm())

book2 = Booking("Max", 2)
print(book2.confirm())

book3 = Booking("JAne", 5)
print(book3.confirm())

print(MixinLog.ID)

class Notebook1(Goods, MixinLog):
    def __init__(self, name, weight, price):
        print("init Notebook1")
        Goods.__init__(self, name, weight, price)
        MixinLog.__init__(self)

class Notebook2(MixinLog, Goods):
    def __init__(self, name, weight, price):
        print("init Notebook2")
        MixinLog.__init__(self)
        Goods.__init__(self, name, weight, price)

nb1 =Notebook1("MacBook1", 1.5, 200000)
nb2 = Notebook2("MacBook2", 1.7, 250000)

nb1.print_info()
print(nb1)
nb2.print_info()
print(nb2)
# MacBook1, 200000, 1.5
# <__main__.Notebook1 object at 0x10a890590>
# 6
# <__main__.Notebook2 object at 0x10a8906e0>


# Задание_7

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")

# Задание_8

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: необходимо вводить числа!")


# Задание_9

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: необходимо вводить числа!")
except Exception:
    print("Произошла неизвестная ошибка")

# Задание_10

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ZeroDivisionError as e:
    print(f"На ноль делить нельзя! ({e})")
except ValueError as e:
    print(f"Ошибка ввода: {e}")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")

# Задание_11

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
    print(f"Результат: {result}")
except ArithmeticError as e:
    print(f"Арифметическая ошибка: {e}")

# Задание_12

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите число")
else:
    print("Деление выполнено успешно")
    print(f"Результат: {result}")

# Задание_13

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = a / b
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите числа")
else:
    print("Деление выполнено успешно")
    print(f"Результат: {result}")
finally:
    print("Работа программы завершена")

# Задание_14

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    try:
        result = a / b
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
except ValueError:
    print("Ошибка ввода: введите два числа")

# Задание_15

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return None

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    result = divide(a, b)
    if result is not None:
        print(f"Результат: {result}")
except ValueError:
    print("Ошибка ввода: введите два числа")