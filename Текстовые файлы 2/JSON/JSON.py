import json

#1
results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}
with open("test_results.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

#2
results = [{"id": 1, "name": "Sasha", "role": "admin"}]
with open("users.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

#3
with open("test_results.json", "r") as f:
    data = json.load(f)

print(f"Процент успешно пройденных тестов: {data['passed'] / data['total'] * 100}%")

#4
new_user = [{"id": 2, "name": "Lesha", "role": "user"}]
with open("users.json", "r") as f:
    data = json.load(f)
data.append(new_user)

with open("users.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

#5
def dummy_test(data):
    if data <= 5:
        return True
    else:
        return False

tests = [
(dummy_test(5), True),
(dummy_test(7), True),
(dummy_test(6), False),
(dummy_test(2), True),
(dummy_test(4), False),
(dummy_test(8), True),
(dummy_test(1), False),
]

fail_tests_counter = 0
count_tests = len(tests)

for result, expected in tests:
    try:
        assert result == expected
    except AssertionError as e:
        print(f"Тест не пройден! Ожидается что пароль результат {expected}, " +
              f"но фактический результат {result}")
        fail_tests_counter += 1
        continue
    print("Тест прошёл!")

print(fail_tests_counter)
data = {
    'tests_count' : count_tests,
    'complete_tests_count': count_tests - fail_tests_counter,
    'fail_tests_count': fail_tests_counter,
    'complete_tests_percent': round((count_tests - fail_tests_counter) / count_tests * 100, 2)
}

with open("5.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)