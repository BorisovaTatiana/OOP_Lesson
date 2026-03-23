# Задание_1

class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, text):
        if len(text) < self.min_length or len(text) > self.max_length:
            raise ValueError(f"Длина должна быть от {self.min_length}")
        return True

validator = LengthValidator(3, 10)
print(validator("python"))  # True
# print(validator("hi"))      # ValueError

# Задание_2

class Sumator:
    def __init__(self):
        self.total = 0

    def __call__(self, number):
        self.total += number
        return self.total

s = Sumator()
print(s(5))   # 5
print(s(10))  # 15
print(s(-2))  # 13

# Задание_3

class HasText:
    def __init__(self, substr):
        self.substr = substr

    def __call__(self, text):
        return self.substr in text

assert HasText("Success")("Test passed: Success") == True
assert HasText("Error")("All OK") == False

check1 = HasText("Success")
print(check1("Success!"))  # True
print(check1("Failed"))    # False



# Задание_4

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.author} — {self.title}"

    def __repr__(self):
        return f"<Книга '{self.title}' by {self.author}>"

book = Book("1984", "Джордж Оруэлл")
print(book)
print(repr(book))

# Задание_5

class TestUser:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<TestUser id={self.id} name='{self.name}' email='{self.email}'>"

user1 = TestUser(12, "Daniil", "daniil@example.com")
print(user1)