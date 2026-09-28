#1
import functools
import time
from time import sleep

def retry(times):
    def decorator(func):
        def wrapper():
            result = func()
            for i in range(times):
                result = func()
                if result == "PASSED":
                    return f"Успешно! попытка номер: {i+1}"
                else:
                    print("Не успешно! попытка номер:", i+1)
            return "Попыток больше нет"
        return wrapper
    return decorator


@retry(times=3)
def flaky_test():
    if time.time() % 2 < 1:
        return "FAILURE"
    return "PASSED"

print(flaky_test())

print ("--------------------------------------------------------------------------------------------------------------")
#2
user_one = "user"
user_two = "admin"

def require_role(user_role):
    def decorator(func):
        def wrapper(*args):
            if args[0] == user_role:
                return func(*args)
            else:
                print("Ошибка: Требуется роль admin, текущая: ", user_role)
                return None
        return wrapper
    return decorator

@require_role("admin")
def admin_test(*args):
    print("Выполняется админский тест")
    return "Success"

print("Попытка с ролью user")
admin_test(user_one)
print("Попытка с ролью admin")
admin_test(user_two)

print ("--------------------------------------------------------------------------------------------------------------")
#3
def timer(func):
    @functools.wraps(func)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__} выполнился за {end_time - start_time} сек.")
    return wrapper

@timer
def slow_test():
    time.sleep(1)
    return "OK"

slow_test()

print ("--------------------------------------------------------------------------------------------------------------")
#4
def wait_with_retry_until(timeout, interval):
    def decorator(func):
        def wrapper():
            counter = 1
            start_time = time.time()
            while True:
                if func():
                    print(f"Попытка {counter}: успешно\nЭлемент найден")
                    return
                print(f"Попытка {counter}: неуспешн")
                if time.time() - start_time > timeout:
                    print("Таймаут")
                    return
                counter += 1
                time.sleep(interval)
        return wrapper
    return decorator

@wait_with_retry_until(timeout=10, interval=0.5)
def element_visible():
    return time.time() % 3 > 2  # имитация появления элемента

element_visible()

print ("--------------------------------------------------------------------------------------------------------------")
#5
def cache_results(func):
    cache = {}
    def wrapper(*args):
        key = args[0]
        if key in cache:
            return cache[key]
        result = func(*args)
        cache[key] = result
        return result
    return wrapper


@cache_results
def expensive_calculation(n):
    print(f"Вычисляем для {n}")
    sleep(1)
    return n * n

print(expensive_calculation(5)) #медленно считает
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(5)) #быстро возвращает из кеша
print(expensive_calculation(6)) #медленно считает
print(expensive_calculation(6)) #быстро возвращает из кеша

print ("--------------------------------------------------------------------------------------------------------------")
#6
def validate_params(schema):
    def decorator(func):
        def wrapper(**kwargs):
            for param_name, expected_type in schema.items():
                if type(kwargs[param_name]) != expected_type:
                    return f"{param_name} должен быть {expected_type. __name__}"
            return func(**kwargs)
        return wrapper
    return decorator


@validate_params({"username": str, "age": int})
def create_user(**kwargs):
    return f"Пользователь {kwargs['username']} создан"

print(create_user(username="test", age=25))
print(create_user(username="test", age='25'))
print ("--------------------------------------------------------------------------------------------------------------")
#7
LOG_LEVEL = "ERROR"
LOG_LEVELS = {"INFO": 1, "DEBUG": 2, "ERROR": 3}
def conditional_log(min_level="INFO"):
    def decorator(func):
        def wrapper (*args, **kwargs):
            if LOG_LEVELS[LOG_LEVEL] >= LOG_LEVELS[min_level]:
                print(f"[{min_level}] {func.__name__}")
        return wrapper
    return decorator

@conditional_log("DEBUG")
def debug_test():
    return "debug_result"

debug_test()
