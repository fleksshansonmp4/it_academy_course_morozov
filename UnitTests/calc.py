import argparse

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def power(a, b):
    return a ** b

operations = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "power": power
}

parser = argparse.ArgumentParser(description="Парсер для калькулятора")

parser.add_argument("-a", type=float, default=1, help="Первое число")
parser.add_argument("-b", type=float, default=1, help="Второе число")
parser.add_argument("-op", choices=["add", "sub", "mul", "div", "power"], default="add", help="Список функций")

args = parser.parse_args()

func = operations.get(args.op)

try:
    print(func(args.a, args.b))
except ZeroDivisionError:
    print("На 0 деление невозможно")