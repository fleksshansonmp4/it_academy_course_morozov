import math
from abc import abstractmethod, ABC

#1.1
class Product:

    def __init__(self, price):
        if price >= 0:
            self.price = price
        else:
            self.price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Отрицательную цену задать нельзя")


p = Product(-10)
print(p.price)   # 100
p.price = 250
print(p.price)   # 250
p.price = -10  # Отрицательную цену задать нельзя
print(p.price)   # 250


#1.2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    @property
    def area(self):
        return self.height * self.width

rect = Rectangle(3, 4)
print(rect.area)      # 12
rect.width = 10


#1.3
class TestStats:
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total

    @property
    def success_rate(self):
        return self.passed / self.total * 100

stats = TestStats(8, 10)
print(stats.success_rate)   # 80.0
stats.passed = 9
print(stats.success_rate)   # 90.0


#2.1
class PermissionMixin:
    def has_permission(self, role):
        if role == "admin":
            return True
        else:
            return False

class SecureAction(PermissionMixin):

    def execute(self, role):
        if self.has_permission(role):
            print("Админ. Метод запущен")
        else:
            print("Нет прав")

action = SecureAction()
action.execute("user") # Нет прав.
action.execute("admin") # Админ. Метод запущен


#2.2
class Logger:
    def log(self, message):
        print(f"[Log] {message}")

class Service:
    def __init__(self):
        self.logger = Logger()

    def process(self):
        self.logger.log("Начал обработку")
        print("Обрабатываю")
        self.logger.log("Закончил обработку")

s = Service()
s.process()


#2.3
class Admin:

    def create_user(self, name):
        print(f"Создан пользователь {name}")

class Support:

    def create_ticket(self, ticket):
        print(f"Создан тикет: {ticket}")

class SuperUser(Admin, Support):
    pass

su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")


#2.4
class A:
    def who_am_i(self):
        print("A")

class B(A):
    def who_am_i(self):
        print("B")

class C(A):
    def who_am_i(self):
        print("C")

class D(B, C):
    pass

d = D()
d.who_am_i()       # B (по MRO)
print(D.mro())


#2.5
class LoginMixin:
    def log(self):
        print("[LOG] Выполняет задачу")

class RetryMixin:
    def retry(self, number):
        for i in range(0, number):
            print(f"Попытка {i+1}")
            self.log()
            self.run()

class Job(LoginMixin, RetryMixin):
    def run(self):
        print("Job что-то делает...")

j = Job()
j.retry(2)

#3.1
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return f"Прямоугольник. Площадь: {self.width * self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"Круг. Площадь: {round(math.pi  * self.radius * self.radius, 2)}"

shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    print(s.area())


#3.2
class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    def go(self):
        print("Начинаем движение")
        self.move()

class Car(Transport):
    def move(self):
        print("Едем по дороге на машине")

class Bike(Transport):
    def move(self):
        print("Едем на велосипеде")

for t in (Car(), Bike()):
    t.go()


#3.3
class BaseTestCase(ABC):
    @abstractmethod
    def prepare_data(self):
        pass

    @abstractmethod
    def run_test(self):
        pass

    def run(self):
        self.prepare_data()
        self.run_test()

class LoginTest(BaseTestCase):
    def prepare_data(self):
        print("===LoginTest===")
        print("Готовим пользователя для логина")

    def run_test(self):
        print("Проверяем успешный логин")

class PaymentTest(BaseTestCase):
    def prepare_data(self):
        print("===PaymentTest===")
        print("Готовим данные карты и баланс")

    def run_test(self):
        print("Проверяем успешный платеж")


tests = [LoginTest(), PaymentTest()]
for t in tests:
    t.run()


#4.1
class BaseTest:
    def run(self):
        pass

class APITest(BaseTest):

    def __init__(self, method):
        self.method = method

    def run(self):
        print(f"API тест: проверяем эндпоинт {self.method}")

class UITest(BaseTest):

    def __init__(self, page):
        self.page = page

    def run(self):
        print(f"UI тест: проверяем страницу {self.page}")

def run_all(tests):
    for t in tests:
        t.run()

tests = [
    APITest("/login"),
    UITest("LoginPage"),
    APITest("/users"),
]
run_all(tests)

#4.2
def print_length(obj):
    print(len(obj))

class TestCollection:
    def __init__(self, items):
        self.mas = items

    def __len__(self):
        return len(self.mas)


print_length("Python") #6
print_length([1, 2, 3]) #3
print_length({"a": 1, "b": 2}) #2
print_length(TestCollection([10, 20, 30, 40])) #4
