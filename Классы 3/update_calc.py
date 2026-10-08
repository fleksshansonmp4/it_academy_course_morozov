def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def square(a,b ):
    return a ** b

while True:
    try:
        a = float(input("Введите первое число\n"))
        b = float(input("Введите первое число\n"))
    except ValueError:
        print("Вы ввели не число! Пожалуйста повторите ввод")
        continue

    point = input("Выберите операцию (Введите +, -, *, / или ^):")

    match point:
        case '+':
            print("Вы выбрали сложение")
            print("Результат: ",sum(a,b))
        case '-':
            print("Вы выбрали вычитание")
            print("Результат: ",sub(a, b))
        case '*':
            print("Вы выбрали умножение")
            print("Результат: ",mul(a, b))
        case '/':
            print("Вы выбрали деление")
            try:
                print("Результат: ",div(a, b))
            except ZeroDivisionError:
                print("Делить на 0 нельзя")
        case '^':
            print("Вы выбрали возведение в степень")
            print("Результат: ",square(a, b))
        case _:
            print("Неккоректная операция")
            print("Результат: None")