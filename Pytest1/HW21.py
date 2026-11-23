from logging import exception

import pytest
from pytest_check import check
import practice_calculator as calc

mycalc = calc.Calculator()


"""Тесты сложение"""

#сложение двух положительных чисел
@pytest.mark.parametrize("num1", [1,2,3])
@pytest.mark.parametrize("num2", [4,5,6])
def test_add_positive_numbers(num1, num2):
    check.is_true(mycalc.add(num1, num2) == num1 + num2)

#сложение числа с нулём
@pytest.mark.parametrize("num1", [1,2,3])
def test_add_with_zero (num1):
    check.is_true(mycalc.add(num1, 0) == num1 + 0)

#сложение отрицательных чисел
@pytest.mark.parametrize("num1", [-1,-2,-3])
@pytest.mark.parametrize("num2", [-4,-5,-6])
def test_add_negative_numbers(num1, num2):
    check.is_true(mycalc.add(num1, num2) == num1 + num2)

#сложение чисел с плавающей точкой
@pytest.mark.parametrize("num1", [2.5,3.6,5.2])
@pytest.mark.parametrize("num2", [1.2,3.4,6.1])
def test_add_float_numbers(num1, num2):
    check.is_true(mycalc.add(num1, num2) == num1 + num2)


"""Тесты вычитание"""

#вычитание положительных чисел
@pytest.mark.parametrize("num1", [9,8,7])
@pytest.mark.parametrize("num2", [3,2,1])
def test_subtract_positive_numbers(num1, num2):
    check.is_true(mycalc.subtract(num1, num2) == num1 - num2)
#проверка отрицательного результата
@pytest.mark.parametrize("num1", [1,2,3])
@pytest.mark.parametrize("num2", [9,8,7])
def test_subtract_negative_result(num1, num2):
    check.is_true(mycalc.subtract(num1, num2) == num1 - num2)
#вычитание одинаковых чисел
@pytest.mark.parametrize("num1", [1,2,3])
def test_subtract_same_numbers(num1, num2):
    check.is_true(mycalc.subtract(num1, num1) == num1 - num1)


"""Тесты умножение"""

#умножение положительных чисел
@pytest.mark.parametrize("num1", [9,8,7])
@pytest.mark.parametrize("num2", [3,2,1])
def test_multiply_positive_numbers(num1, num2):
    check.is_true(mycalc.multiply(num1, num2) == num1 * num2)

#умножение на ноль
@pytest.mark.parametrize("num1", [9,8,7])
def test_multiply_by_zero(num1, num2):
    check.is_true(mycalc.multiply(num1, 0) == num1 * 0)

#умножение отрицательных чисел
@pytest.mark.parametrize("num1", [-9,-8,-7])
@pytest.mark.parametrize("num2", [-3,-2,-1])
def test_multiply_negative_numbers(num1, num2):
    check.is_true(mycalc.multiply(num1, num2) == num1 * num2)

#умножение дробных чисел
@pytest.mark.parametrize("num1", [9.2,8.5,7.3])
@pytest.mark.parametrize("num2", [3.6,2.7,1.2])
def test_multiply_float_numbers(num1, num2):
    check.is_true(mycalc.multiply(num1, num2) == num1 * num2)


"""Деление"""

#деление положительных чисел
@pytest.mark.parametrize("num1", [9,8,7])
@pytest.mark.parametrize("num2", [3,2,1])
def test_divide_positive_numbers(num1, num2):
    check.is_true(mycalc.divide(num1, num2) == num1 / num2)

#деление отрицательных чисел
@pytest.mark.parametrize("num1", [9,-8,-7])
@pytest.mark.parametrize("num2", [-3,2,-1])
def test_divide_negative_numbers(num1, num2):
    check.is_true(mycalc.divide(num1, num2) == num1 / num2)

#результат деления всегда float
@pytest.mark.parametrize("num1", [9,8,7])
@pytest.mark.parametrize("num2", [3,2,1])
def test_divide_result_is_float(num1, num2):
    check.is_true(isinstance(mycalc.divide(num1, num2), float))


"""Возведение в степень"""

#возведение в положительную степень
@pytest.mark.parametrize("num", [9,8,7])
@pytest.mark.parametrize("exp", [3,2,1])
def test_power_positive_exponent(num, exp):
    check.is_true(mycalc.power(num, exp) == num ** exp)

#возведение в нулевую степень
@pytest.mark.parametrize("num", [9,8,7])
def test_power_zero_exponent(num):
    check.is_true(mycalc.power(num, 0) == num ** 0)

#возведение в отрицательную степень
@pytest.mark.parametrize("num", [9,8,7])
@pytest.mark.parametrize("exp", [-3,-2,-1])
def test_power_negative_exponent(num, exp):
    check.is_true(mycalc.power(num, exp) == num ** exp)


"""Процент от числа"""

#расчёт процента от положительного числа
@pytest.mark.parametrize("num", [100, 200, 300])
@pytest.mark.parametrize("per", [10, 20, 30])
def test_percentage_positive_value(num, per):
    check.is_true(mycalc.percentage(num, per) == num / 100 * per)

#0% от числа равен 0
@pytest.mark.parametrize("num", [100, 200, 300])
def test_percentage_zero_percent(num):
    check.is_true(mycalc.percentage(num, 0) == 0)

#100% от числа равно самому числу
@pytest.mark.parametrize("num", [100, 200, 300])
def test_percentage_hundred_percent(num):
    check.is_true(mycalc.percentage(num, 100) == num)


"""История вычислений"""

#у нового калькулятора история пустая
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_history_empty_by_default(new_calc):
    check.is_true(len(new_calc.history) == 0)

#после сложения в истории появляется запись
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_history_after_add(new_calc):
    new_calc.add(2,2)
    check.is_true(new_calc.history == [])

#после нескольких операций история содержит все записи.
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_history_after_multiple_operations(new_calc):
    new_calc.add(2,2)
    new_calc.divide(5,1)
    new_calc.multiply(4,4)
    check.is_true(len(new_calc.history) == 3)

#записи в истории идут в порядке выполнения операций
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_history_order(new_calc):
    new_calc.add(2,2)
    new_calc.subtract(5,1)
    new_calc.multiply(4,4)
    check.is_true(new_calc.history == ["2 + 2 = 4", "5 - 1 = 4", "4 * 4 = 16"])

#после clear_history() история становится пустой
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_clear_history(new_calc):
    new_calc.add(1,1)
    new_calc.clear_history()
    check.is_true(new_calc.history == [])

#изменение списка, полученного из get_history(), не меняет историю калькулятора.
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_get_history_returns_copy(new_calc):
    new_calc.add(1,1)
    history = new_calc.get_history()
    history.append("52 + 52 = 104")
    check.is_true(new_calc.history != history)

#при делении на ноль запись в историю не добавляется.
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_history_not_added_after_error(new_calc):
    try:
        new_calc.divide(5,0)
    except ZeroDivisionError:
        pass
    check.is_true(new_calc.history == [])


"""Проверка ошибок"""

#текст исключения содержит "Деление на ноль".
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_divide_by_zero_error_message(new_calc):
    try:
        new_calc.divide(5, 0)
    except ZeroDivisionError as e:
        check.is_true("Деление на ноль" in str(e))

#передача отрицательного числа в percentage() вызывает ValueError, текст исключения содержит "Процент не может быть отрицательным".
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_percentage_negative_error_message(new_calc):
    try:
        new_calc.percentage(50, -20)
    except ValueError as e:
        check.is_true("Процент не может быть отрицательным" in str(e))

#передача строки в add() вызывает TypeError.
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_invalid_types_add(new_calc):
    try:
        new_calc.add("fgdsgfsdfsgdf", 3)
    except Exception as e:
        check.is_true(type(e) is TypeError)

#передача строки в divide() вызывает TypeError.
@pytest.mark.parametrize("new_calc", [calc.Calculator()])
def test_invalid_types_divide(new_calc):
    try:
        new_calc.divide("fgdsgfsdfsgdf", 3)
    except Exception as e:
        check.is_true(type(e) is TypeError)