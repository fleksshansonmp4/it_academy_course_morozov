import random

#1
while True:
    print("1.Бросить кубик")
    print("Любая другая клавиша - выход")

    a = input("Выберите действие\n")
    match a:
        case "1":
            print("Бросаем кубик")
            print(f"Выпало число:{random.randint(1, 6)}")
        case _:
            break

#2
password = "".join(random.choices(list("abcdefghijklmnopqrstuvwxyz"), k=8))
print(f"Сгенерированный пароль:{password}")

#3
HTTP = ["GET", "POST", "PUT", "DELETE"]
print(random.choice(HTTP))

#4
tests = ["test_login", "test_logout", "test_add_to_cart", "test_checkout"]
random.shuffle(tests)
print(tests)

#5
users = ["alice", "bob", "carol", "dave", "erin"]
select_users = random.sample(users, k=2)
print(select_users)

#6
def run_flaky_test():
    if random.random() < 0.3:
        return "FAILED"
    return "PASSED"


#7
ticket = random.sample(range(1,50), 6)
print(f"Номер лотерейного билета: {''.join(map(str, ticket,))}")

#8
def generate_test_data(n):
    return random.choices(range(1,100), n)
