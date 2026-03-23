# Задание_1
class Person:
    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return f"Имя: {self.name}, Возраст: {self.age}"

person1 = Person()
person2 = Person()

person1.set_data("Татьяна", 36)
person2.set_data("Сергей", 36)

print(person1.get_data())
print(person2.get_data())


# Задание_2_3

class Point:
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

p = Point()
p.set_coords(7, 12)
print(p.get_coords())
p.set_coords(-3, 5)
print(p.get_coords())

p1 = Point()
p1.set_coords(10, 20)
result1 = p1.get_coords()
print(result1)
get_method = getattr(p1, 'get_coords')
result2 = get_method()
print(result2)
print(result1 == result2)

# Задание_4_5

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}, возраст: {self.age}")

    def __del__(self):
        print(f"Удалён объект: {self.name}")


person = Person("Tatiana", 36)
person.show_info()

person3 = Person("Алексей", 56)
print(person3.name)
del person3

# Задание_6

class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect1 = Rectangle()
print(rect1)
rect2 = Rectangle(4,5)
print(rect2)
# rect3 = Rectangle(4)
# print(rect3)

# Задание_7

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        print("Инициализация логгера")

logger1 = Logger()
logger2 = Logger()

print(logger1)
print(logger2)
