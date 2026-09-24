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
    a = input("Введите первое число\n")
    b = input("Введите второе число\n")
    if not (a.isdigit() or b.isdigit()):
        print("Одно из чисел введено неккоректно")
        continue

    a = float(a)
    b = float(b)
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
            if b == 0.0:
                print('Второе число равно 0, деление невозможно')
            print("Результат: ",div(a, b))
        case '^':
            print("Вы выбрали возведение в степень")
            print("Результат: ",square(a, b))
        case _:
            print("Неккоректная операция")
            print("Результат: None")