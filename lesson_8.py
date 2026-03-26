# Задание_1

# def inner():
#     result = 10 / 0
#     return result
#
# def outer():
#     return inner()
# outer()
# ZeroDivisionError: division by zero

# Задание_2

# def inner():
#     result = 10 / 0
#     return result
#
# def outer():
#     return inner()
#
# try:
#     outer()
# except ZeroDivisionError:
#     print("Ошибка перехвачена на верхнем уровне")
# Вывелось

# Задание_3

# def inner():
#     try:
#         result = 10 / 0
#         return result
#     except ZeroDivisionError:
#         return "Ошибка в inner"
#
# def outer():
#     return inner()
#
# result = outer()
# print(f"Результат: {result}")
#  Результат: Ошибка в inner

# Задание_4

# def inner():
#     result = 10 / 0
#     return result
#
# def outer():
#     try:
#         return inner()
#     except ZeroDivisionError:
#         print("Ошибка в outer")
#         return None
#
# outer()
# Ошибка в outer

# Задание_5

def get_value():
    raise ValueError("Неверное значение")

def test_get_value():
    try:
        get_value()
    except ValueError:
        assert False

try:
    test_get_value()
except AssertionError as e:
    print(f"Поймано исключение {e}")

# Задание_6

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return x / y

try:
    print(divide(7, 2))
    print(divide(18, 0))
except ZeroDivisionError as e:
    print(f"Ошибка: {e}")

# Задание_7

import math

class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError(f"Нельзя извлечь корень из {x}")
    return math.sqrt(x)

try:
    print(f"sqrt(16) = {sqrt(16)}")
    print(f"sqrt(-4) = {sqrt(-4)}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

# Задание_8

class MathError(Exception):
    pass

class NegativeNumberError(MathError):
    pass

class DivisionByZeroError(MathError):
    pass

def safe_divide(x, y):
    if y == 0:
        raise DivisionByZeroError("Деление на ноль!")
    return x / y

try:
    print(safe_divide(87, 4))
    print(safe_divide(19, 0))
except MathError as e:
    print(f"Математическая ошибка: {e}")

# Задание_9

class NegativeNumberError(Exception):
    pass

def sqrt(x):
    if x < 0:
        raise NegativeNumberError(f"Нельзя извлечь корень из {x}")
    return math.sqrt(x)

def test_sqrt():
    try:
        sqrt(-4)
        print("Тест пройден")
    except NegativeNumberError:
        assert False, "Нельзя брать корень из отрицательного числа"

try:
    test_sqrt()
except AssertionError as e:
    print(f"{e}")

# Задание_10

with open('sample.txt', 'w') as f:
    f.write("Привет, мир!\nЭто тестовый файл.")

with open('sample.txt', 'r') as f:
    content = f.read()
    print(content)

# Задание_11

class BackupList:
    def __init__(self, lst):
        self.lst = lst
        self.backup = None

    def __enter__(self):
        self.backup = self.lst.copy()
        print(self.backup)
        return self.lst

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Ошибка: {exc_val}")
            print("Откат изменений")
            self.lst[:] = self.backup
        else:
            print("Изменения сохранены")
        return True

data = [1, 2, 3]
with BackupList(data) as lst:
    lst.append(4)
    lst.append(5)
print(f"Результат: {data}")

data1 = [1, 2, 3]
with BackupList(data1) as lst:
    lst.append(4)
    raise ValueError("Тестовая ошибка")
print(f"Результат после отката: {data1}")

# Задание_12

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"{self.func.__name__} выполнено за {end - start:.4f} сек")
        return result

@Timer
def slow_function():
    time.sleep(1)
    return

@Timer
def fast_function():
    return

print(slow_function())
print(fast_function())