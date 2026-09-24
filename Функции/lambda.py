#2.1
func = lambda a : a["status"] == "passed"
test_results = [
    {"name": "login_test", "status": "passed", "duration": 2.1},
    {"name": "payment_test", "status": "failed", "duration": 3.5},
    {"name": "logout_test", "status": "passed", "duration": 1.2}
]

filter_results = list(filter(func, test_results))
print("Успешные тесты: ", [name["name"] for name in filter_results])

#2.2
func = lambda a: sorted(a, key= lambda t: t["duration"])

tests = [
    {"name": "complex_test", "duration": 5.2},
    {"name": "simple_test", "duration": 1.1},
    {"name": "medium_test", "duration": 3.4}
]

print("Тесты по времени выполнения:", func(tests))

#2.3
func = lambda s: "@" in s and (s.endswith(".com") or s.endswith(".ru"))
emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]
filter_results = list(filter(func, emails))
print("Валидные email:", filter_results)