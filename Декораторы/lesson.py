"""
#1
def say_hello(func):
    def wrapper():
        print("Начинается тест")
        func()
    return wrapper

@say_hello
def test():
    print("test")

test()

#2
def repeat_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@repeat_twice
def text():
    print("Привет, Анна!")

text()

#3
def print_result(func):
    def wrapper():
        print(func())
    return wrapper

@print_result
def test():
    return 4

test()

"""

import functools
import time
from time import sleep


#4
def log_test(func):
    @functools.wraps(func)
    def wrapper(user_name):
        print(f"Запуск теста:{func.__name__}")
        res = func(user_name)
        print (f"Тест {func.__name__} завершен")
        print(res)
    return wrapper

def timer(func):
    def wrapper(user_name):
        start = time.time()
        func(user_name)
        end = time.time()
        print(f"Время работы теста{end - start}")
    return wrapper

@timer
@log_test
def test_login(username):
    sleep(1)
    print(f"Проверяем логин:{username}")
    return True

test_login("User123")

"""
#как работает time
start_time = time.time()

sleep(3)

end_time = time.time()

print(end_time - start_time)
"""