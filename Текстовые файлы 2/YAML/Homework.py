import yaml
#1
results = {'test_suite': 'api_tests', 'total': 10, 'passed': 8, 'failed': 2}
with open("test_results.yaml", "w") as f:
    yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False)

#2
results = [{"id": 1, "name": "Sasha", "role": "admin"}]
with open("users.yaml", "w") as f:
    yaml.safe_dump(results, f, default_flow_style=False, sort_keys=False)

#3
with open("test_results.yaml", "r") as f:
    data = yaml.safe_load(f)

complete_tests_percent = data['passed'] / data['total'] * 100
print(complete_tests_percent)

#4
with open("users.yaml", "r") as f:
    data = yaml.safe_load(f)

new_user = {
    "id": 2,
    "name": "Lesha",
    "role": "user"
}
data.append(new_user)

with open("users.yaml", "w") as f:
    yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)

#5
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

with open("5.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False)