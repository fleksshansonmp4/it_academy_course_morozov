#1
username = input("Введите имя пользователя\n")
print(type(username))


#2
number = input("Введите целое число\n")
number = int(number)
print(number, type(number))


#3
number = input("Введите число с точкой\n")
number = float(number)
print(number, type(number))


#4
first_number = input("Введите первое число\n")
second_number = input("Введите второе число\n")
first_number = int(first_number)
second_number = int(second_number)
print (first_number + second_number)


#5
words = input("Введите строку из нескольких слов через пробел\n")
words = words.split(' ')
print(words, type(words))


#6
string = input("Введите любую строку\n")
print ("Длинна строки:", len(string))


#7
string = input("Введите что-либо\n")
string = bool(string)
print (string)


#8
first_string = input("Введите первую строку\n")
second_string = input("Введите вторую строку\n")
print(first_string + second_string)


#9
string = input("Введите строку\n")
number = input("Введите число\n")
number = int(number)
print("Символ под номером ", number, ": ", string[number])


#10
string = input("Введите строку\n")
print(string.isdigit())
















