import logging

"""
#1
Настройте логирование через logging.basicConfig() так, чтобы логи записывались в файл app_session.log.
Файл должен очищаться при каждом запуске программы (filemode='w'). Минимальный порог логирования — INFO.
Залогируйте три сообщения: DEBUG, INFO и CRITICAL. Проверьте, какие из них попадут в файл.
"""
logging.basicConfig(
    filename="app_session.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.debug("DEBUG")
logging.info("INFO")
logging.critical("CRITICAL")

"""
#2
Условие: Создайте функцию repeat_string(text, count), которая дублирует строку text указанное количество раз count. 
Напишите два assert: один должен проверять, что text является строкой (str), 
а второй — что count является целым числом (int).
"""

def repeat_string(text, count):
    assert isinstance(text, str), "Передана не строка"
    assert isinstance(count, int), "Передано не число"

    for i in range(0,count):
        print(text)

repeat_string("fffff", 5)

"""
#3
Условие: Настройте систему логирования так, чтобы сообщения уровня INFO и выше записывались в файл combined.log, 
а сообщения уровня ERROR и выше — дублировались в отдельный файл crit_errors.log.
"""
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_info_handler = logging.FileHandler("combiner.log")
file_info_handler.setLevel(logging.INFO)


file_err_handler = logging.FileHandler("crit_errors.log")
file_err_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_info_handler.setFormatter(formatter)
file_err_handler.setFormatter(formatter)

logger.addHandler(file_info_handler)
logger.addHandler(file_err_handler)

logger.debug("DEBUG")
logger.info("INFO")
logger.warning("WARNING")
logger.error("ERROR")
logger.critical("CRITICAL")

"""
#4
Условие: Дан словарь user_data = {"name": "Alice"}. Напишите блок try-except, запрашивающий несуществующий ключ "age". 
При возникновении ошибки KeyError используйте правильный метод логгера для автоматической записи полного 
стека ошибки (Traceback) в консоль.
"""

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.raiseExceptions)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

user_data = {"name": "Alice"}
try:
    a = user_data["age"]
except KeyError:
    logger.exception("Traceback")


"""
#5
Условие: Создайте функцию process_payment(amount). Внутри неё:
1.	С помощью assert проверьте, что amount > 0.
2.	Если assert падает, перехватите эту ошибку AssertionError внутри блока try-except, запишите сообщение со стеком ошибки через logger.exception() и завершите функцию (или верните False).
3.	Если всё в порядке, запишите через logger.info() сообщение "Платеж на сумму X проведен успешно".
"""

def progress_payment(amount):
    try:
        assert amount > 0, "Число должно быть больше нуля"
        logger.info(f"Платеж на сумму {amount} проведен успешно")
    except AssertionError:
        logger.exception("")
        return False

progress_payment(52)