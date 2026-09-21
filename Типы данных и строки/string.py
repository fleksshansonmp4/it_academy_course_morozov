#1
fullname = "Иванов Иван Иванович"
fullname = fullname.split(' ')
print(f"{fullname[0]} {fullname[1][0].upper()}. {fullname[2][0].upper()}.")


#2
string = input("Введите строку\n")
string = string.split(' ')
print(f"Количество слов: {len(string)}")


#3
string = input("Введите строку\n")
print(f"Обратная строка: {string[::-1]}")


#4
string = input("Введите строку\n")
string = string.replace(" ", "")
print(f"Без пробелов: {string}")


#5
first_string = input("Введите первую строку\n")
second_string = input("Введите вторую строку\n")
print(first_string.find(second_string))


#6
first_string = input("Введите строку\n")
search_symbol = input("Введите символ для поиска\n")
replace_symbol = input("Введите символ для замены\n")
first_string = first_string.replace(search_symbol, replace_symbol)
print("Результат: ", first_string)


#7
string = input("Введите строку\n")
print("Строка является числом - ", string.isdigit())