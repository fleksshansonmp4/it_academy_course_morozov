
#1
a = input("Введите строку\n")
for x in range(0,len(a)):
    print(a[x])


#2
a = input("Введите строку\n")
counter = 0
for x in range(0,len(a)):
    if a[x] in 'aouie':
        counter += 1

print(f"Количество гласных букв: {counter}")


#3
a = input("Введите несколько тестовых названий через пробел\n").split(' ')
for x in range(0,len(a)):
    print("Test Case: ",a[x])


#4
password = input("Введите пароль\n")
while password != "admin":
    password = input("Введите пароль\n")
    if password == "admin":
        break

#5
for x in range(1,11):
    if x % 3 == 0:
        continue
    else:
        print(x)


#6
counter = 0
for x in range(1,101):
    counter += x
print(f"Сумма числе от 1 до 100: {counter}")


#7
browser = ["Chrome", "Firefox"]
oc = ["Windows", "Linux"]

for b in browser:
    for o in oc:
        print(f"{b}-{o}")


#8
a = input("Введите строку\n")
for index, value in enumerate(a):
    print(f"{index}: {value}")


#9
a = input("Введите строку\n")
for char in a:
    if char == '@':
        print("Есть @")
        break
else:
    print("Нет @")


#10
a = 10
while a != -1:
    print(a)
    a -= 1


#11
a = input("Введите строку\n")
result = ""
for x in a:
    result += x.upper()

print(result)


#12
a = int(input("Введите число\n"))
while a < 10:
    a = int(input("Введите число\n"))


#13
a = input("Введите строку\n")
words = a.split(' ')
counter = 0
for word in words:
    counter += 1
print("Количество слов в строке", counter)


#14
for x in range(1,20):
    if x > 15:
        break
    else:
        print(x)