import math
pi = math.pi

#1
r = 7
print(f"Площадь круга радиусом {r}: {pi * pow(r,2)}")

#2
number = 9.8
print(f"Наибольшее целое число, не превышающее число {number}: {math.floor(number)}")

#3
sin = 45
print(f"Синус {sin} градусов: {math.sin(math.radians(sin))}")

#4
number = 144
print(f"Квадратный корень из числа {number}: {math.sqrt(number)}")

#5
first_number = 270
second_number = 192
print(f"Наибольший общий делитель чисел {first_number} и {second_number}: "
      f"{math.gcd(first_number, second_number)}")

#6
pw = 3
print(f"Значение е в степени {pw}: {math.exp(pw)}")

#7
number = 8
print(f"Факториал числа {number}: {math.factorial(number)}")

#8
start_number = 2
end_number = 256
print(f"Степень, в которую нужно возвести {start_number}, чтобы получить {end_number}: {math.log(256, 2)}")

#9
number = 3.14159
print(f"Ближайшее целое число к {number}: {math.ceil(number)}")

#10
def tang(a):
    return math.tan(math.radians(a))