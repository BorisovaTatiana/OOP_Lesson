# Задание_1

class Dog:
    species = "canis"
    legs = 4

dog1 = Dog()
dog2 = Dog()

dog1.species = "lupus"
print(dog1.species)
print(dog2.species)
print(Dog.species)

print(dog1.__dict__)
print(dog2.__dict__)

# Задание_2
# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.

print(Dog.__doc__)
dog = Dog()
setattr(dog, "name", "Шарик")
setattr(dog, "age", 3)

print(dog.name)

delattr(dog, "name")
print(dog.__dict__) #{'age': 3}

# Задание_3_4

class User:
    role = "guest"
    active = True

user = User()
setattr(user, "role", "admin")
print(getattr(user, "role"))

print(hasattr(user, "active"))

setattr(user, "email", "user@mail.ru")
print(getattr(user, "email"))

delattr(user, "role")
print(hasattr(user, "role"))

print(user.__dict__)
print(User.role)
