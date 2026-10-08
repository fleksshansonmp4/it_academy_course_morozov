from dataclasses import dataclass, field
from enum import Enum
from shlex import split
from statistics import quantiles
from typing import List, Optional

#1
def test_info(author, component):
    def decorator(cls):
        cls.author = author
        cls.component = component
        return cls
    return decorator

@test_info(author="Иван", component="Auth")
class TestLogin:
    pass

print(TestLogin.author)     # Иван
print(TestLogin.component)  # Auth


#2
PAGES = []

def register_page(cls):
    PAGES.append(cls)
    return cls

@register_page
class LoginPage:
    pass

@register_page
class DashboardPage:
    pass

print([cls.__name__ for cls in PAGES])


#3

class Tag:
    def __init__(self, tag_name):
        self.tag_name = tag_name

    def __call__(self, cls):
        cls.tag = self.tag_name
        return cls


@Tag("smoke")
class SmokeTests:
    pass

@Tag("regression")
class RegressionTests:
    pass

print(SmokeTests.tag)	       # smoke
print(RegressionTests.tag)  # regression


#4
class Environment(Enum):
    DEV = "DEV"
    STAGE = "STAGE"
    PROD = "PROD"

BASE_URLS = {
    Environment.DEV: "https://dev.example.com",
    Environment.STAGE: "https://stage.example.com",
    Environment.PROD: "https://prod.example.com",
}

def get_base_url(env):
    return BASE_URLS[env]

print(get_base_url(Environment.DEV)) # https://dev.example.com
print(get_base_url(Environment.PROD)) # https://prod.example.com


#5
class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

tasks = [
    ("Починить тест логина", Priority.HIGH),
    ("Обновить документацию", Priority.LOW),
    ("Настроить CI", Priority.MEDIUM),
]
# Сортировка по значению enum
tasks_sorted = sorted(tasks, key=lambda x: x[1].value)

for name, prio in tasks_sorted:
    print(prio.name, "-", name)


#6
class TestType(Enum):
    API = "API"
    UI = "UI"
    UNIT = "UNIT"

tests = [
    ("test_login_api", TestType.API),
    ("test_login_ui", TestType.UI),
    ("test_sum", TestType.UNIT),
    ("test_profile_api", TestType.API),
]

def filter_tests_by_type(tests, test_type: TestType):
    return [task for task in tests if task[1] == test_type]

print(filter_tests_by_type(tests, TestType.API))
print(filter_tests_by_type(tests, TestType.UI))

#7
def parse_int_list(strings):
    nums = []
    for i in strings:
        try:
            nums.append(int(i))
        except BaseException:
            print(f"{i} нельзя преобразовать в целочисленное значение")
    return nums

raw = ["10", "20", "abc", "30", "4.5", "40"]
nums = parse_int_list(raw)
print(nums)  # [10, 20, 30, 40]


#9
@dataclass
class Point:

    x: float
    y: float

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)  # Point(x=1.0, y=2.0)
print(p2)  # Point(x=-3.5, y=4.2)


#10
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1

    def total(self):
        return self.price * self.quantity

p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0)

print(p1, "total:", p1.total())  # 100.0
print(p2, "total:", p2.total())  # 25.0

#11
@dataclass
class Book:
    title: str
    author: list[str] = field(default_factory=list)
    year: int | None = None

    def formatted(self):
        year = self.year if self.year is not None else "год неизвестен"
        return f"{self.title} ({year}) - {", ".join(self.author)}"

b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга")
b3 = Book("Совместный труд", ["Alice", "Bob"])

for b in (b1, b2, b3):
    print(b.formatted())